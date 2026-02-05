# AFSIM Script Examples

## 重要提醒
- 文件扩展名必须是 `.txt`
- 所有数值参数必须带单位
- 所有代码块必须有结束标记

## Example 1: 简单的固定翼无人机巡航

```
# File: uav_patrol.txt

file_path .
log_file uav_patrol.log

platform_type fixed_wing_uav WSF_PLATFORM
    side blue
    category uav

    mover WSF_AIR_MOVER
        maximum_speed 100 m/sec
        minimum_speed 30 m/sec
        default_radial_acceleration 2.0 g
        default_climb_rate 10 m/sec
    end_mover
end_platform_type

platform my_uav fixed_wing_uav
    side blue

    route
        position 0.0 0.0 1000.0
            speed 80 m/sec
        position 10000.0 0.0 1000.0
            speed 80 m/sec
        position 10000.0 10000.0 1000.0
            speed 80 m/sec
        position 0.0 10000.0 1000.0
            speed 80 m/sec
    end_route

    heading 90 deg
end_platform

end_time 3600 sec
```

## Example 2: 使用经纬度坐标的路径

```
# File: geo_route.txt

file_path .
log_file geo_route.log

platform_type aircraft WSF_PLATFORM
    side blue

    mover WSF_AIR_MOVER
        maximum_speed 250 m/sec
        minimum_speed 50 m/sec
        default_radial_acceleration 3.0 g
    end_mover
end_platform_type

platform my_aircraft aircraft
    side blue

    route
        # 北京
        position 39.90n 116.40e altitude 5000 m msl
            speed 200 m/sec
        # 上海
        position 31.23n 121.47e altitude 5000 m msl
            speed 200 m/sec
    end_route

    heading 180 deg
end_platform

end_time 7200 sec
```

## Example 3: 多平台场景

```
# File: multi_platform.txt

file_path .
log_file multi_platform.log

# 定义平台类型
platform_type fighter WSF_PLATFORM
    side blue
    category aircraft

    mover WSF_AIR_MOVER
        maximum_speed 500 m/sec
        minimum_speed 100 m/sec
        default_radial_acceleration 5.0 g
    end_mover
end_platform_type

platform_type bomber WSF_PLATFORM
    side blue
    category aircraft

    mover WSF_AIR_MOVER
        maximum_speed 300 m/sec
        minimum_speed 80 m/sec
        default_radial_acceleration 2.0 g
    end_mover
end_platform_type

# 创建平台实例
platform fighter_1 fighter
    side blue
    route
        position 0.0 0.0 8000.0
            speed 400 m/sec
        position 50000.0 0.0 8000.0
            speed 400 m/sec
    end_route
    heading 90 deg
end_platform

platform bomber_1 bomber
    side blue
    route
        position 0.0 5000.0 6000.0
            speed 250 m/sec
        position 50000.0 5000.0 6000.0
            speed 250 m/sec
    end_route
    heading 90 deg
end_platform

end_time 1800 sec
```