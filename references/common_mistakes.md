# AFSIM 常见错误和最佳实践

## 关键规则（必须遵守）

### 1. 文件扩展名
**错误：** 使用 `.wsf` 扩展名
**正确：** 使用 `.txt` 扩展名

```
# 正确
chengdu_uav_patrol.txt

# 错误
chengdu_uav_patrol.wsf
```

### 2. 所有数值参数必须带单位
**错误：** 只写数字
**正确：** 数字 + 空格 + 单位

```
# 错误
maximum_speed 100
update_interval 30.0
altitude 1000

# 正确
maximum_speed 100 m/sec
update_interval 30.0 sec
altitude 1000 m
```

### 3. 常用单位列表

**速度单位：**
- `m/sec` - 米/秒
- `km/hr` - 千米/小时
- `knots` - 节

**时间单位：**
- `sec` - 秒
- `min` - 分钟
- `hr` - 小时

**距离单位：**
- `m` - 米
- `km` - 千米
- `ft` - 英尺

**角度单位：**
- `deg` - 度
- `rad` - 弧度

**加速度单位：**
- `g` - 重力加速度
- `m/sec^2` - 米/秒²

### 4. 所有代码块必须有结束标记

```
# 正确
platform_type my_type WSF_PLATFORM
    mover WSF_AIR_MOVER
    end_mover
end_platform_type

processor my_proc WSF_SCRIPT_PROCESSOR
    update_interval 1.0 sec
end_processor

# 错误 - 缺少 end_platform_type
platform_type my_type WSF_PLATFORM
    mover WSF_AIR_MOVER
    end_mover
```

### 5. 路由（Route）语法

**正确的路由定义：**
```
route
    position 30.67n 104.07e altitude 1000 m msl
        speed 80 m/sec
    position 30.54n 104.07e altitude 1000 m msl
        speed 80 m/sec
end_route
```

**注意：**
- 不要使用 `loop` 命令（会导致错误）
- 如需循环，在 route 外使用 `at_end_of_path` 参数

### 6. 脚本处理器（Script Processor）

**避免使用不存在的方法：**

```
# 错误 - 这些方法不存在
WsfGeoPoint pos = myUAV.Position();
WsfGeodetic geo = pos.Geodetic();
Time()

# 正确 - 使用简单的 print 语句
on_update
    print("UAV status update");
end_on_update
```

### 7. 位置坐标格式

**经纬度格式：**
```
# 正确
position 30.67n 104.07e altitude 1000 m msl

# 说明：
# 30.67n  - 北纬 30.67 度
# 104.07e - 东经 104.07 度
# altitude 1000 m msl - 海拔 1000 米（平均海平面）
```

**笛卡尔坐标格式：**
```
position 0.0 0.0 1000.0
# X Y Z 坐标（米）
```

### 8. 必需的文件路径设置

```
# 在脚本开头添加
file_path .
log_file simulation.log
```

### 9. Mover 配置常见参数

```
mover WSF_AIR_MOVER
    maximum_speed 100 m/sec
    minimum_speed 30 m/sec
    default_radial_acceleration 2.0 g
    default_climb_rate 10 m/sec
    at_end_of_path extrapolate  # 路径结束后的行为
end_mover
```

### 10. 完整的平台定义模板

```
platform_type my_aircraft WSF_PLATFORM
    side blue
    category aircraft

    mover WSF_AIR_MOVER
        maximum_speed 250 m/sec
        minimum_speed 50 m/sec
        default_radial_acceleration 3.0 g
    end_mover
end_platform_type

platform my_platform my_aircraft
    side blue

    route
        position 0.0 0.0 1000.0
            speed 100 m/sec
        position 10000.0 0.0 1000.0
            speed 100 m/sec
    end_route

    heading 90 deg
end_platform

end_time 3600 sec
```
