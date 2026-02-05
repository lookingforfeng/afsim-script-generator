# AFSIM 命令完整参考

本文档包含 AFSIM 2.9.0 所有主要命令的完整语法参考。

## 目录

1. [Platform 命令](#platform-命令)
2. [Route 命令](#route-命令)
3. [Sensor 命令](#sensor-命令)
4. [Weapon 命令](#weapon-命令)
5. [Processor 命令](#processor-命令)
6. [仿真控制命令](#仿真控制命令)

---

## Platform 命令

### 基本语法

**创建平台实例**:
```
platform <platform-name> <platform-type-name>
   ... platform commands ...
end_platform
```

**创建平台类型**:
```
platform_type <new-type-name> <source-type-name>
   ... platform commands ...
end_platform_type
```

**编辑现有平台**:
```
edit platform <platform-name>
   ... platform commands ...
end_platform
```

### 必需参数

- `<platform-name>` - 平台实例名称（唯一，建议小写）
- `<platform-type-name>` - 平台类型（如 WSF_PLATFORM 或自定义类型）

### 基本属性

```
side <side-name>                         # 阵营（如 blue, red）
icon <icon-name>                         # 显示图标
marking <marking-name>                   # 标记文本
category <category-name>                 # 类别分类
clear_categories                         # 清除所有类别
spatial_domain [land|air|surface|subsurface|space]
                                        # 空间域
```

### 位置和方向

```
position <latitude> <longitude>          # 纬度和经度
mgrs_coordinate <MGRS-value>             # 军事网格参考系统坐标
altitude <length-value> [agl|msl]        # 高度（地面或海平面）
heading <angle-value>                    # 航向角度
geo_point <name> <lat> <lon> <alt>       # 命名地理点
```

**示例**:
```
position 35.5n 120.3w
altitude 10000 ft msl
heading 90 deg
```

### 质量属性

```
empty_mass <mass-value>                  # 空载质量，默认: 0 kg
fuel_mass <mass-value>                   # 燃料质量，默认: 0 kg
payload_mass <mass-value>                # 载荷质量，默认: 0 kg
```

### 签名特征

```
acoustic_signature <value>               # 声学签名
infrared_signature <value>               # 红外签名，默认: 1000 w/sr
radar_signature <value>                  # 雷达签名，默认: 1000 m²
optical_signature <value>                # 光学签名
optical_reflectivity <value>             # 光学反射率，默认: 1.0
inherent_contrast <value>                # 固有对比度
```

### 物理尺寸

```
length <length-value>                    # 长度
width <length-value>                     # 宽度
height <length-value>                    # 高度
```

### 生存能力

```
indestructible                           # 不可摧毁
destructible                             # 可摧毁（默认）
on_broken [remove|disable|disabled_but_movable]
                                        # 损坏后行为，默认: remove
initial_damage_factor <value>            # 初始损伤因子（0-1），默认: 0.0
concealment_factor <value>               # 隐蔽因子（0-1），默认: 0.0
```

### 时间控制

```
creation_time <time-value>               # 创建时间，默认: 0 sec
```

### 组件定义

```
mover <type>
   ... mover commands ...
end_mover

route
   ... route commands ...
end_route

sensor <name> <type>
   ... sensor commands ...
end_sensor

weapon <name> <type>
   ... weapon commands ...
end_weapon

processor <name> <type>
   ... processor commands ...
end_processor
```

### 完整示例

```
platform fighter-1 F16
   side blue
   icon fighter
   category aircraft
   position 35.5n 120.3w
   altitude 10000 ft msl
   heading 90 deg
   creation_time 0 sec

   empty_mass 8500 kg
   fuel_mass 3000 kg

   radar_signature 5 m^2
   infrared_signature 800 w/sr

   mover WSF_AIR_MOVER
      maximum_speed 500 m/sec
      minimum_speed 50 m/sec
      default_radial_acceleration 5.0 g
   end_mover

   route
      navigation
         position 35.5n 120.3w
         speed 450 kts
         altitude 10000 ft msl

         position 36.0n 121.0w
         speed 500 kts
      end_navigation
   end_route
end_platform
```

---

## Route 命令

### 基本语法

```
route
   navigation
      ... navigation commands ...
   end_navigation
end_route
```

或定义可重用路线:
```
route <name>
   navigation
      ... commands ...
   end_navigation
end_route
```

### 位置定义（开始新航点）

```
position <latitude> <longitude>          # 绝对位置
mgrs_coordinate <MGRS-value>             # MGRS坐标
offset <x-offset> <y-offset> <units>     # 相对偏移
turn_left <angle-value>                  # 左转指定角度
turn_right <angle-value>                 # 右转指定角度
turn_to_heading <angle-value>            # 转向指定航向
```

### 航点标记和控制

```
label <string>                           # 为航点添加标签
goto <string>                            # 跳转到标记的航点
```

### 速度和加速度

```
speed <speed-value>                      # 航点速度
linear_acceleration <accel-value>        # 线性加速度
radial_acceleration <accel-value>        # 径向加速度（转弯）
bank_angle_limit <angle-value>           # 最大倾斜角
turn_g_limit <accel-value>               # 最大转弯G载荷
```

### 高度控制

```
altitude <length-value> [agl|msl]        # 高度（默认: msl用于空中）
depth <length-value>                     # 水下深度
climb_rate <speed-value>                 # 爬升率
dive_rate <speed-value>                  # 下降率
maximum_flight_path_angle <angle-value>  # 最大飞行路径角
```

### 航向控制

```
heading <angle-value>                    # 航向（仅单点路线有效）
turn [left|right|shortest]               # 转向方向，默认: shortest
```

### 航点行为

```
pause_time <time-value>                  # 到达后暂停时间
execute <script-name> <callback-name>    # 执行脚本
extrapolate                              # 到达终点后继续当前状态
stop                                     # 到达终点后停止
remove                                   # 到达终点后移除平台
```

### 航点切换

```
switch_on_passing                        # 经过航点时切换（默认）
switch_on_approach                       # 接近航点时切换
```

### 完整示例

```
route
   navigation
      label start
      position 35.0n 120.0w
      speed 300 kts
      altitude 5000 ft msl
      climb_rate 1000 ft/min

      position 35.5n 120.5w
      speed 350 kts
      altitude 10000 ft msl
      radial_acceleration 3.0 g

      label waypoint2
      position 36.0n 121.0w
      speed 400 kts
      altitude 15000 ft msl
      pause_time 30 sec

      position 36.5n 121.5w
      speed 300 kts
      altitude 5000 ft msl
      dive_rate 2000 ft/min
   end_navigation
end_route
```

---

## Sensor 命令

### 基本语法

```
sensor <sensor-name> <sensor-type>
   ... sensor commands ...
end_sensor
```

### 常用传感器类型

- `WSF_RADAR_SENSOR` - 雷达传感器
- `WSF_IRST_SENSOR` - 红外搜索跟踪传感器
- `WSF_ESM_SENSOR` - 电子支援措施传感器
- `WSF_EO_SENSOR` - 光电传感器
- `WSF_ACOUSTIC_SENSOR` - 声学传感器
- `WSF_MAD_SENSOR` - 磁异常探测器

### 通用参数

```
location <x> <y> <z>                     # 传感器位置（相对平台）
frame_time <time-value>                  # 帧时间
minimum_range <length-value>             # 最小探测距离
maximum_range <length-value>             # 最大探测距离
field_of_view <angle-value>              # 视场角
```

### 雷达传感器特定参数

```
scan_mode [azimuth|elevation|both]       # 扫描模式
scan_rate <angle-rate-value>             # 扫描速率
antenna_pattern <pattern-name>           # 天线模式
transmitter_power <power-value>          # 发射功率
receiver_sensitivity <value>             # 接收灵敏度
```

### 示例

```
sensor main_radar WSF_RADAR_SENSOR
   location 0 0 -2 ft
   frame_time 10 sec
   minimum_range 0 nm
   maximum_range 160 nm
   scan_mode azimuth
   scan_rate 60 deg/sec
   antenna_pattern radar_antenna_pattern
   transmitter_power 1000 kW
end_sensor
```

---

## Weapon 命令

### 基本语法

```
weapon <weapon-name> <weapon-type>
   ... weapon commands ...
end_weapon
```

### 常用武器类型

- `WSF_AIR_TO_AIR_MISSILE` - 空对空导弹
- `WSF_AIR_TO_GROUND_MISSILE` - 空对地导弹
- `WSF_BOMB` - 炸弹
- `WSF_GUN` - 机炮
- `WSF_JAMMER` - 干扰器

### 通用参数

```
location <x> <y> <z>                     # 武器位置（相对平台）
quantity <number>                        # 武器数量
reload_time <time-value>                 # 重装时间
firing_interval <time-value>             # 发射间隔
maximum_range <length-value>             # 最大射程
minimum_range <length-value>             # 最小射程
```

### 导弹特定参数

```
seeker_type [radar|infrared|laser]       # 导引头类型
seeker_fov <angle-value>                 # 导引头视场
max_g <accel-value>                      # 最大机动过载
burnout_time <time-value>                # 发动机燃尽时间
```

### 示例

```
weapon aim120 WSF_AIR_TO_AIR_MISSILE
   location 0 -5 -1 ft
   quantity 4
   firing_interval 2 sec
   maximum_range 50 nm
   minimum_range 1 nm
   seeker_type radar
   seeker_fov 60 deg
   max_g 40 g
   burnout_time 8 sec
end_weapon
```

---

## Processor 命令

### 基本语法

```
processor <processor-name> <processor-type>
   ... processor commands ...
end_processor
```

### 常用处理器类型

- `WSF_SCRIPT_PROCESSOR` - 脚本处理器
- `WSF_TRACK_MANAGER` - 跟踪管理器

### 脚本处理器参数

```
update_interval <time-value>             # 更新间隔

script_variables
   <type> <name> = <value>;
   ...
end_script_variables

script <return-type> <function-name>(<parameters>)
   ... script code ...
end_script

on_initialize
   ... initialization code ...
end_on_initialize

on_update
   ... update code ...
end_on_update
```

### 示例

```
processor status_monitor WSF_SCRIPT_PROCESSOR
   update_interval 30 sec

   script_variables
      WsfPlatform myPlatform = PLATFORM;
      int updateCount = 0;
   end_script_variables

   on_initialize
      print("Processor initialized");
   end_on_initialize

   on_update
      updateCount = updateCount + 1;
      print("Update #", updateCount);
      print("Platform: ", myPlatform.Name());
   end_on_update
end_processor
```

---

## 仿真控制命令

### 基本命令

```
end_time <time-value>                    # 仿真结束时间
```

### 文件路径配置

```
file_path <directory-path>               # 文件路径
log_file <filename>                      # 日志文件名
```

### 事件输出配置

```
event_output
   file <filename>
   enable all
end_event_output
```

### 示例

```
# 文件路径配置
file_path .
log_file simulation.log

# 事件输出
event_output
   file output/events.evt
   enable all
end_event_output

# 仿真时间
end_time 3600 sec
```

---

## 重要提示

### ⚠️ 单位要求

**所有数值参数必须带单位！**

```
# ❌ 错误
maximum_speed 250
altitude 10000
heading 90

# ✅ 正确
maximum_speed 250 m/sec
altitude 10000 ft msl
heading 90 deg
```

### 常用单位

**速度**: `m/sec`, `km/hr`, `kts` (节)
**距离**: `m`, `km`, `ft`, `nm` (海里)
**时间**: `sec`, `min`, `hr`
**角度**: `deg`, `rad`
**加速度**: `g`, `m/sec^2`
**质量**: `kg`, `lb`
**功率**: `W`, `kW`, `MW`

### 结束标记

**所有代码块必须有对应的结束标记！**

```
platform ... end_platform
platform_type ... end_platform_type
mover ... end_mover
route ... end_route
sensor ... end_sensor
weapon ... end_weapon
processor ... end_processor
script_variables ... end_script_variables
on_initialize ... end_on_initialize
on_update ... end_on_update
```