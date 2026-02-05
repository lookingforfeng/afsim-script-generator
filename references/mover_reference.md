# AFSIM Mover 类型完整参考

本文档包含所有 AFSIM 2.9.0 mover 类型的完整参考信息。

## 目录

1. [路由类型 Movers](#路由类型-movers)
2. [制导类型 Movers](#制导类型-movers)
3. [空间类型 Movers](#空间类型-movers)
4. [六自由度类型 Movers](#六自由度类型-movers)
5. [特殊类型 Movers](#特殊类型-movers)

---

## 路由类型 Movers

基于数学模型的简化 mover，通过航路点定义路径。

### WSF_AIR_MOVER - 空中运动器

**用途**: 固定翼飞机、无人机等空中平台

**关键参数**:
```
mover WSF_AIR_MOVER
    update_interval 0 sec                    # 更新间隔，默认: 0
    maximum_speed 250 m/sec                  # 最大速度，必须>0
    minimum_speed 50 m/sec                   # 最小速度，必须≥0，默认: 0.0
    default_radial_acceleration 3.0 g        # 默认径向加速度，默认: 6g
    default_linear_acceleration 2.0 g        # 默认线性加速度，默认: 6g
    default_climb_rate 10 m/sec              # 默认爬升率
    default_dive_rate 10 m/sec               # 默认下降率
    maximum_climb_rate 15 m/sec              # 最大爬升率
    maximum_flight_path_angle 30 deg         # 最大飞行路径角，默认: 0
    bank_angle_limit 60 deg                  # 滚转角限制，0-85度，默认: 0
    turn_rate_limit 15 deg/sec               # 转弯率限制，必须>0
    heading_pursuit_gain 5.0                 # 航向追踪增益，默认: 5
    at_end_of_path extrapolate               # 路径结束行为
end_mover
```

**路径结束行为**:
- `extrapolate` - 继续当前状态（默认）
- `stop` - 停止
- `remove` - 移除平台

**注意事项**:
- 水平运动连续，垂直转换（高度变化）是瞬时的
- 径向加速度 ≠ 载荷因子。2g转弯时，径向加速度 = g × sqrt(n²-1) = 1.732g

---

### WSF_ROTORCRAFT_MOVER - 旋翼机运动器

**用途**: 直升机、旋翼无人机

**关键参数**:
```
mover WSF_ROTORCRAFT_MOVER
    update_interval 0 sec
    maximum_ground_speed 100 m/sec           # 最大地速
    maximum_rate_of_climb 15 m/sec           # 最大爬升率
    maximum_total_acceleration 2.0 g         # 最大总加速度
    maximum_attitude_rate 30 deg/sec         # 最大姿态变化率
    weathercock_speed 10 m/sec               # 风标速度
end_mover
```

**特点**:
- 支持悬停（速度为0）
- 航向与速度方向解耦
- 具有风标效应（低速时航向自动对准速度方向）

---

### WSF_GROUND_MOVER - 地面运动器

**用途**: 地面车辆、坦克

**关键参数**:
```
mover WSF_GROUND_MOVER
    update_interval 0 sec
    maximum_speed 30 m/sec
    minimum_speed 0 m/sec
    default_radial_acceleration 1.5 g
    turn_rate_limit 20 deg/sec
    on_road                                  # 限制不滚转
    # 或 off_road                            # 允许滚转
end_mover
```

**特点**:
- 地形跟随
- 可选择道路模式或越野模式

---

### WSF_SURFACE_MOVER - 水面运动器

**用途**: 舰船、水面平台

**关键参数**:
```
mover WSF_SURFACE_MOVER
    update_interval 0 sec
    maximum_speed 20 m/sec
    minimum_speed 0 m/sec
    default_radial_acceleration 0.5 g
    turn_rate_limit 5 deg/sec
end_mover
```

**特点**:
- 俯仰和滚转设为零
- 自动跟随水面

---

### WSF_SUBSURFACE_MOVER - 水下运动器

**用途**: 潜艇、鱼雷、水下无人航行器

**关键参数**:
```
mover WSF_SUBSURFACE_MOVER
    update_interval 0 sec
    maximum_speed 25 m/sec
    minimum_speed 5 m/sec
    default_radial_acceleration 1.0 g
    maximum_depth 500 m                      # 最大下潜深度
end_mover
```

---

### WSF_KINEMATIC_MOVER - 运动学运动器

**用途**: 通用运动学模型，提供平滑的水平和垂直运动

**关键参数**:
```
mover WSF_KINEMATIC_MOVER
    initial_speed 100 m/sec
    target_speed 200 m/sec
    initial_flight_path_angle 0 deg
    maximum_linear_acceleration 0.25 g       # 默认: 0.25g
    maximum_radial_acceleration 8.0 g        # 默认: 8.0g
    maximum_body_roll_rate 180 deg/sec       # 默认: 180 deg/sec
    maximum_body_turn_rate 45 deg/sec        # 默认: 45 deg/sec
    velocity_pursuit_gain 4.0                # 默认: 4.0
    proportional_navigation_gain 40.0        # 默认: 40.0
    prefer_canopy_up true                    # 保持座舱朝上
    bank_to_turn true                        # 转弯时倾斜
end_mover
```

**特点**:
- 垂直加速度被建模（不是瞬时的）
- 不需要气动、质量或推进系统
- 适合快速原型开发

---

## 制导类型 Movers

### WSF_GUIDED_MOVER - 制导运动器

**用途**: 制导导弹、火箭

**关键参数**:
```
mover WSF_GUIDED_MOVER
    update_interval 0 sec
    integration_timestep 0.01 sec            # 积分时间步长
    coordinate_frame ECEF                    # 坐标系: ECI 或 ECEF
    thrust_vectoring_angle_limit 0 deg       # 推力矢量角限制
    divert_thrust 0 N                        # 侧向推力

    # PID 控制器
    proportional_gain 3.0
    integral_gain 0.0
    derivative_gain 0.0
    maximum_acceleration 20 g

    # 多级推进
    stage 1
        thrust 50000 N
        fuel_mass 100 kg
        burn_rate 10 kg/sec
        ignition_time 0 sec
        burnout_time 10 sec
    end_stage
end_mover
```

**特点**:
- 3自由度点质量模型
- 支持多级推进系统
- PID 控制器用于制导

---

### WSF_UNGUIDED_MOVER - 非制导运动器

**用途**: 自由落体炸弹、非制导火箭

**关键参数**:
```
mover WSF_UNGUIDED_MOVER
    update_interval 0 sec
    integration_timestep 0.01 sec
    coordinate_frame ECEF
end_mover
```

---

### WSF_PARABOLIC_MOVER - 抛物线运动器

**用途**: 弹道导弹、炮弹

**关键参数**:
```
mover WSF_PARABOLIC_MOVER
    update_interval 0 sec
    maximum_range 50000 m
    time_of_flight 120 sec
end_mover
```

---

## 空间类型 Movers

### WSF_SPACE_MOVER - 空间运动器

**用途**: 卫星、空间飞行器（简化轨道模型）

**关键参数**:
```
mover WSF_SPACE_MOVER
    update_interval 0 sec
    propagator kepler                        # 轨道传播器

    # 开普勒轨道根数
    semi_major_axis 7000 km
    eccentricity 0.001
    inclination 45 deg
    right_ascension 0 deg
    argument_of_perigee 0 deg
    true_anomaly 0 deg
end_mover
```

---

### WSF_NORAD_SPACE_MOVER - NORAD 空间运动器

**用途**: 使用 TLE（两行轨道根数）数据的卫星

**关键参数**:
```
mover WSF_NORAD_SPACE_MOVER
    update_interval 0 sec
    tle_file satellite_tle.txt               # TLE 数据文件
    satellite_name "ISS"                     # 卫星名称
end_mover
```

---

### WSF_INTEGRATING_SPACE_MOVER - 积分空间运动器

**用途**: 高精度数值积分轨道传播

**关键参数**:
```
mover WSF_INTEGRATING_SPACE_MOVER
    update_interval 0 sec
    integration_timestep 1 sec
    gravity_model EGM96                      # 重力模型
    atmospheric_drag true                    # 大气阻力
    solar_radiation_pressure true            # 太阳辐射压
end_mover
```

---

## 六自由度类型 Movers

### WSF_RIGID_BODY_SIX_DOF_MOVER - 刚体六自由度

**用途**: 高保真飞行器仿真

**关键参数**:
```
mover WSF_RIGID_BODY_SIX_DOF_MOVER
    update_interval 0 sec
    integration_timestep 0.01 sec
    mass 15000 kg
    inertia_xx 50000 kg*m^2
    inertia_yy 80000 kg*m^2
    inertia_zz 120000 kg*m^2
end_mover
```

---

### WSF_POINT_MASS_SIX_DOF_MOVER - 点质量六自由度

**用途**: 简化的六自由度模型

---

### WSF_P6DOF_MOVER - P-6DOF 运动器

**用途**: 基于物理的高级六自由度模型

---

## 特殊类型 Movers

### WSF_TSPI_MOVER - TSPI 运动器

**用途**: 回放轨迹数据（时间-空间-位置-信息）

**关键参数**:
```
mover WSF_TSPI_MOVER
    tspi_file trajectory_data.txt            # 轨迹数据文件
end_mover
```

---

### WSF_OFFSET_MOVER - 偏移运动器

**用途**: 相对于另一平台保持固定偏移

**关键参数**:
```
mover WSF_OFFSET_MOVER
    reference_platform parent_aircraft
    offset_x 10 m
    offset_y 5 m
    offset_z -2 m
end_mover
```

---

### WSF_HYBRID_MOVER - 混合运动器

**用途**: 可在路由和跟随模式间切换

---

### WSF_FORMATION_FLYER - 编队飞行器

**用途**: 保持编队飞行

---

### WSF_TOWED_MOVER - 拖曳运动器

**用途**: 被拖曳的物体（如拖曳式诱饵）

---

### WSF_STRAIGHT_LINE_MOVER - 直线运动器

**用途**: 简单直线飞行

---

### WSF_ROAD_MOVER - 道路运动器

**用途**: 沿道路网络移动

**关键参数**:
```
mover WSF_ROAD_MOVER
    maximum_speed 25 m/sec
    road_network city_roads                  # 道路网络名称
end_mover
```

---

### WSF_FIRES_MOVER - 火力运动器

**用途**: 炮弹、火箭弹

---

### WSF_TBM_MOVER - 战术弹道导弹运动器

**用途**: 战术弹道导弹

---

### WSF_BRAWLER_MOVER - Brawler 运动器

**用途**: 快速近似战斗模型

---

### WSF_ARGO8_MOVER - ARGO8 运动器

**用途**: 特殊的气动模型

---

## 通用命令

所有 Route Mover 共享的命令：

```
use_route <route-name>                       # 使用指定路由
at_end_of_path [extrapolate|stop|remove]     # 路径结束行为
start_at <label>                             # 起始航点标签
start_time <time>                            # 开始移动时间
altitude_offset <length>                     # 高度偏移
path_variance_radius <length>                # 路径变化半径
speed_variance_percent <percent>             # 速度变化百分比
```

---

## 使用场景推荐

| 场景 | 推荐 Mover |
|------|-----------|
| 固定翼飞机 | WSF_AIR_MOVER |
| 直升机 | WSF_ROTORCRAFT_MOVER |
| 地面车辆 | WSF_GROUND_MOVER |
| 舰船 | WSF_SURFACE_MOVER |
| 潜艇 | WSF_SUBSURFACE_MOVER |
| 制导导弹 | WSF_GUIDED_MOVER |
| 炸弹 | WSF_UNGUIDED_MOVER |
| 弹道导弹 | WSF_TBM_MOVER 或 WSF_PARABOLIC_MOVER |
| 卫星 | WSF_SPACE_MOVER 或 WSF_NORAD_SPACE_MOVER |
| 编队飞行 | WSF_FORMATION_FLYER |
| 轨迹回放 | WSF_TSPI_MOVER |
| 快速原型 | WSF_KINEMATIC_MOVER |

---

## 重要提示

1. **所有数值参数必须带单位**（如 `100 m/sec`，不能只写 `100`）
2. **径向加速度 ≠ 载荷因子**
3. **默认值命令** vs **最大值命令**：
   - 默认值：除非在路径或脚本中另有规定时使用
   - 最大值：整个仿真过程中不会超过的总体限制
4. **路径结束行为**很重要，选择合适的 `at_end_of_path` 选项