# AFSIM 脚本语法关键规则速查

## 🚨 必读：脚本编写前检查清单

### 1. 输出函数
```
✅ 正确：print(TIME_NOW, " [", PLATFORM.Name(), "] Message");
❌ 错误：cout << TIME_NOW << " [" << PLATFORM.Name() << "] Message" << endl;
```
**规则：** AFSIM 使用 `print()` 函数，不支持 C++ 的 `cout`

### 2. 处理器事件语法
```
✅ 正确：
on_initialize
   startTime = TIME_NOW;
   waypointCount = 0;
end_on_initialize

❌ 错误：
on_initialize
   script
      startTime = TIME_NOW;
   end_script
end_on_initialize
```
**规则：** `on_initialize` 和 `on_update` 中直接写代码，不需要 `script/end_script` 包裹

### 3. 天线方向图定义
```
✅ 正确：
antenna_pattern RADAR_PATTERN
   constant_pattern
      peak_gain 35 db
      azimuth_beamwidth 60 deg
      elevation_beamwidth 60 deg
   end_constant_pattern
end_antenna_pattern

❌ 错误：
antenna_pattern RADAR_PATTERN
   azimuth_beamwidth 60 deg
   elevation_beamwidth 60 deg
   gain 35 db
end_antenna_pattern
```
**规则：** 天线参数必须在 `constant_pattern` 子块中定义

### 4. 脉冲宽度单位
```
✅ 正确：pulse_width 1.0e-6 sec
❌ 错误：pulse_width 1.0 microsec
```
**规则：** 使用科学计数法的秒，不支持 `microsec` 单位

### 5. WSF_AIR_MOVER 支持的参数
```
✅ 正确：
mover WSF_AIR_MOVER
   maximum_speed 600 m/sec
   minimum_speed 100 m/sec
   default_radial_acceleration 9.0 g
end_mover

❌ 错误：
mover WSF_AIR_MOVER
   maximum_speed 600 m/sec
   default_climb_rate 250 m/sec      # 不支持
   default_descent_rate 200 m/sec    # 不支持
end_mover
```
**规则：** WSF_AIR_MOVER 不支持 `default_climb_rate` 和 `default_descent_rate`

### 6. 不支持的运算符和函数
```
❌ 不支持：
- fmod(x, y)                          # 取模函数
- condition ? true_val : false_val    # 三元运算符
- int(value)                          # 类型转换
- x % y                               # 模运算符

✅ 替代方案：
# 定时报告（每60秒）
double lastReportTime = 0.0;
if (TIME_NOW - lastReportTime >= 60.0)
{
   print("Status report");
   lastReportTime = TIME_NOW;
}

# 条件输出
if (radar.IsTurnedOn())
{
   print("Radar: ON");
}
else
{
   print("Radar: OFF");
}
```

## 📋 完整的处理器模板

```
processor PATROL_PROCESSOR WSF_SCRIPT_PROCESSOR
   update_interval 1.0 sec

   script_variables
      int waypointCount = 0;
      double startTime = 0.0;
      double lastReportTime = 0.0;
   end_script_variables

   on_initialize
      startTime = TIME_NOW;
      lastReportTime = TIME_NOW;

      # Turn on radar
      WsfSensor radar = PLATFORM.Sensor("RADAR_NAME");
      if (radar != null)
      {
         radar.TurnOn();
         print(TIME_NOW, " [", PLATFORM.Name(), "] Radar turned ON");
      }
   end_on_initialize

   on_update
      # Status report every 60 seconds
      if (TIME_NOW - lastReportTime >= 60.0)
      {
         print(TIME_NOW, " [", PLATFORM.Name(), "] Status:");
         print("  Position: ", PLATFORM.Latitude(), " deg, ", PLATFORM.Longitude(), " deg");
         print("  Altitude: ", PLATFORM.Altitude(), " m");
         print("  Speed: ", PLATFORM.Speed(), " m/s");

         lastReportTime = TIME_NOW;
      }
   end_on_update
end_processor
```

## 📡 完整的雷达传感器模板

```
# 1. 定义天线方向图
antenna_pattern RADAR_ANTENNA_PATTERN
   constant_pattern
      peak_gain 35 db
      azimuth_beamwidth 60 deg
      elevation_beamwidth 60 deg
   end_constant_pattern
end_antenna_pattern

# 2. 定义雷达传感器
sensor AESA_RADAR WSF_RADAR_SENSOR
   frame_time 1.0 sec

   transmitter
      frequency 10.0 ghz
      power 10.0 kw
      pulse_width 1.0e-6 sec
      pulse_repetition_frequency 10000 hz
      antenna_pattern RADAR_ANTENNA_PATTERN
   end_transmitter

   receiver
      noise_figure 3.0 db
      bandwidth 1.0 mhz
   end_receiver

   swerling_case 1
   number_of_pulses_integrated 10
   one_m2_detect_range 100 nm
end_sensor
```

## 🛩️ 完整的平台类型模板

```
platform_type J20_FIGHTER WSF_PLATFORM
   side blue
   category aircraft

   mover WSF_AIR_MOVER
      maximum_speed 600 m/sec
      minimum_speed 100 m/sec
      default_radial_acceleration 9.0 g
   end_mover

   sensor AESA_RADAR RADAR_SENSOR_NAME
      on
   end_sensor

   processor MISSION_PROCESSOR WSF_SCRIPT_PROCESSOR
      update_interval 1.0 sec

      script_variables
         double startTime = 0.0;
      end_script_variables

      on_initialize
         startTime = TIME_NOW;
         print(TIME_NOW, " [", PLATFORM.Name(), "] Initialized");
      end_on_initialize

      on_update
         print(TIME_NOW, " [", PLATFORM.Name(), "] Update");
      end_on_update
   end_processor
end_platform_type
```

## ⚠️ 常见错误总结

| 错误类型 | 错误写法 | 正确写法 |
|---------|---------|---------|
| 输出函数 | `cout << "text" << endl;` | `print("text");` |
| 处理器事件 | `on_initialize script ... end_script` | `on_initialize ... end_on_initialize` |
| 天线方向图 | 直接定义参数 | 使用 `constant_pattern` 子块 |
| 脉冲宽度 | `1.0 microsec` | `1.0e-6 sec` |
| 三元运算符 | `x ? a : b` | `if (x) { a } else { b }` |
| 取模函数 | `fmod(x, y)` | 使用时间差比较 |
| 类型转换 | `int(value)` | 避免使用，直接用 double |
| 模运算符 | `x % y` | 使用时间差比较 |

## 🎯 脚本编写检查清单

生成脚本前，确保：
- [ ] 使用 `.txt` 文件扩展名
- [ ] 所有数值都带单位
- [ ] 使用 `print()` 而不是 `cout`
- [ ] `on_initialize` 和 `on_update` 不使用 `script` 包裹
- [ ] 天线方向图使用 `constant_pattern` 子块
- [ ] 脉冲宽度使用科学计数法（如 `1.0e-6 sec`）
- [ ] 不使用三元运算符、fmod、类型转换、模运算符
- [ ] WSF_AIR_MOVER 不使用 climb_rate/descent_rate
- [ ] 所有代码块都有对应的 `end_*` 标记
- [ ] 坐标格式使用 `30.67n 104.07e` 格式

## 📝 快速参考

### 支持的数据类型
```
int, double, string, bool
WsfPlatform, WsfSensor, WsfWeapon, WsfTrack
Array<T>, Map<K,V>
```

### 支持的控制结构
```
if (condition) { } else { }
for (int i = 0; i < n; i++) { }
foreach (type item in collection) { }
while (condition) { }
```

### 支持的运算符
```
算术：+  -  *  /
比较：==  !=  <  >  <=  >=
逻辑：&&  ||  !
赋值：=  +=  -=  *=  /=
```

### 全局变量
```
PLATFORM      # 当前平台
PROCESSOR     # 当前处理器
SENSOR        # 当前传感器
TIME_NOW      # 当前仿真时间
MESSAGE       # 当前消息
```

### 常用 API 方法
```
# WsfPlatform
PLATFORM.Name()
PLATFORM.Latitude()
PLATFORM.Longitude()
PLATFORM.Altitude()
PLATFORM.Speed()
PLATFORM.Heading()
PLATFORM.Sensor(string name)

# WsfSensor
sensor.IsTurnedOn()
sensor.TurnOn()
sensor.TurnOff()
sensor.Name()
```
