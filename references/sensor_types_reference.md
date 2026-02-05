# AFSIM 特殊传感器类型参考

## 概述

AFSIM提供多种特殊传感器类型，每种都有特定的参数和配置。本文档详细说明最常用的特殊传感器类型。

---

## 1. WSF_RADAR_SENSOR - 雷达传感器

### 基本语法
```
sensor <name> WSF_RADAR_SENSOR
   mode <mode-name>
      frame_time <time> sec

      beam <beam-number>
         transmitter
            [transmitter parameters]
         end_transmitter

         receiver
            [receiver parameters]
         end_receiver

         [detection parameters]
      end_beam
   end_mode
end_sensor
```

### Transmitter（发射机）参数

#### 频率参数
```
frequency <frequency-value>              # 工作频率
wavelength <length-value>                # 波长（二选一）
alternate_frequency <id> <frequency>     # 备用频率
bandwidth <frequency-value>              # 频谱带宽（默认：0 Hz）
```

#### 功率参数
```
power <power-value>                      # 发射功率
duty_cycle <real-value>                  # 占空比（默认：1.0）
use_peak_power <boolean>                 # 使用峰值功率
```

#### 脉冲参数
```
pulse_width <time-value>                 # 脉冲宽度
pulse_repetition_frequency <frequency>   # 脉冲重复频率（PRF）
pulse_repetition_interval <time-value>   # 脉冲重复间隔（PRI）
pulse_compression_ratio <db-ratio>       # 脉冲压缩比
```

#### 天线参数
```
antenna_pattern <pattern-name>           # 天线增益方向图
beam_tilt <angle-value>                  # 波束倾斜角
polarization [horizontal | vertical | slant_45 | slant_135 |
             left_circular | right_circular | default]
```

#### 损耗参数
```
internal_loss <db-ratio>                 # 内部损耗
attenuation_model <derived-name>         # 衰减模型
propagation_model <derived-name>         # 传播模型
check_terrain_masking <boolean>          # 地形遮蔽检查（默认：on）
```

### Receiver（接收机）参数

#### 频率和带宽
```
frequency <frequency-value>              # 接收频率
bandwidth <frequency-value>              # 接收带宽
instantaneous_bandwidth <frequency>      # 瞬时带宽
```

#### 天线参数
```
antenna_pattern <pattern-name>           # 天线增益方向图
antenna_ohmic_loss <db-ratio>            # 天线欧姆损耗（默认：0 dB）
beam_tilt <angle-value>                  # 波束倾斜角
```

#### 噪声和检测
```
noise_figure <db-ratio>                  # 噪声系数
noise_power <power-value>                # 噪声功率
detection_threshold <db-ratio>           # 检测门限（默认：3 dB）
internal_loss <db-ratio>                 # 内部损耗
```

### 检测模型参数

#### Swerling目标模型
```
swerling_case [0 | 1 | 2 | 3 | 4]        # Swerling目标模型
number_of_pulses_integrated <integer>    # 积分脉冲数（默认：1）
probability_of_false_alarm <pfa>         # 虚警概率（默认：1.0e-6）
detector_law [linear | square | log]     # 检测器类型（默认：linear）
```

#### 性能参数
```
one_m2_detect_range <length-value>       # 1平方米目标检测距离
range_product <area-value>               # 距离乘积
adjustment_factor <db-ratio>             # 调整因子（默认：0.0 dB）
operating_loss <db-ratio>                # 工作损耗（默认：0.0 dB）
```

### 完整示例
```
antenna_pattern RADAR_ANTENNA
  constant_pattern
     peak_gain 28 dB
     azimuth_beamwidth 4 deg
     elevation_beamwidth 10 deg
  end_constant_pattern
end_antenna_pattern

sensor my_radar WSF_RADAR_SENSOR
   mode search
      frame_time 10 sec

      beam 1
         azimuth_beamwidth 4 deg
         elevation_beamwidth 10 deg

         transmitter
            antenna_pattern RADAR_ANTENNA
            antenna_tilt 5 deg
            power 500 kw
            pulse_width 2.0e-6 sec
            pulse_repetition_frequency 400 hz
            frequency 1285 mhz
         end_transmitter

         receiver
            antenna_pattern RADAR_ANTENNA
            antenna_tilt 5 deg
            bandwidth 1 mhz
            internal_loss 19 dB
            noise_figure 3 dB
         end_receiver

         swerling_case 1
         number_of_pulses_integrated 44
         detector_law square
         probability_of_false_alarm 1.0e-6

         azimuth_error_sigma 0.5 deg
         elevation_error_sigma 0.0 deg
         range_error_sigma 1.2 nm

         one_m2_detect_range 160 nm
      end_beam
   end_mode
end_sensor
```

---

## 2. WSF_ESM_SENSOR - ESM传感器（电子支援措施）

### 基本语法
```
sensor <name> WSF_ESM_SENSOR
   mode <mode-name>
      frame_time <time> sec

      frequency_band <lower-freq> <upper-freq>
         [band parameters]

      receiver
         [receiver parameters]
      end_receiver

      [detection parameters]
   end_mode
end_sensor
```

### 频段定义
```
frequency_band <lower-frequency> <upper-frequency>
   dwell_time <time-value>               # 驻留时间
   revisit_time <time-value>             # 重访时间
```
- 可定义多个频段
- 用于扫描-扫描模型

### 检测灵敏度

#### 基本灵敏度
```
detection_sensitivity <db-power>         # 检测灵敏度（连续波和脉冲相同）
continuous_detection_sensitivity <db-power>  # 连续波检测灵敏度
pulsed_detection_sensitivity <db-power>  # 脉冲检测灵敏度
```

#### 频率相关灵敏度表
```
detection_sensitivities
   frequency <frequency-1> <db-power-1>
   frequency <frequency-2> <db-power-2>
   ...
end_detection_sensitivities
```

或按信号类型分类：
```
detection_sensitivities
   signal_type continuous
      frequency <frequency-1> <db-power-1>
      frequency <frequency-2> <db-power-2>
   signal_type pulsed
      frequency <frequency-1> <db-power-1>
      frequency <frequency-2> <db-power-2>
end_detection_sensitivities
```

### 检测门限

#### 基本门限
```
detection_threshold <db-ratio>           # 信噪比门限（默认：3.0 dB）
continuous_detection_threshold <db-ratio>  # 连续波信噪比门限
pulsed_detection_threshold <db-ratio>    # 脉冲信噪比门限
```

#### 频率相关门限表
```
detection_thresholds
   signal_type continuous
      frequency <frequency-1> <db-ratio-1>
      frequency <frequency-2> <db-ratio-2>
   signal_type pulsed
      frequency <frequency-1> <db-ratio-1>
      frequency <frequency-2> <db-ratio-2>
end_detection_thresholds
```

### 检测概率
```
detection_probability
   signal <db-ratio-1> pd <pd-value-1>
   signal <db-ratio-2> pd <pd-value-2>
   ...
end_detection_probability
```
- `<db-ratio>`: 接收信号功率与检测灵敏度的比值
- `<pd-value>`: 相应的检测概率（0-1之间）
- 使用线性插值

### 扫描-扫描模型
```
scan_on_scan_model <boolean>             # 概率扫描-扫描模型（默认：off）
```
- 关闭时：假设目标发射机直接指向ESM，ESM正在检测目标频率
- 开启时：概率性考虑发射机旋转和ESM频率扫描的时间效应

### 误差参数

#### 基本误差
```
azimuth_error_sigma <angle-value>        # 方位误差标准差
elevation_error_sigma <angle-value>      # 俯仰误差标准差
range_error_sigma <length-value>         # 距离误差标准差
```

#### 频率相关误差表
```
azimuth_error_sigma_table
   frequency <frequency-1> <error-sigma-1>
   frequency <frequency-2> <error-sigma-2>
end_azimuth_error_sigma_table

elevation_error_sigma_table
   frequency <frequency-1> <error-sigma-1>
   frequency <frequency-2> <error-sigma-2>
end_elevation_error_sigma_table

range_error_sigma_table
   frequency <frequency-1> <error-sigma-1>
   frequency <frequency-2> <error-sigma-2>
end_range_error_sigma_table
```

### 测距参数
```
ranging_time <time-value>                # 经过指定时间后添加距离信息
ranging_time_track_quality <quality>     # 测距后的航迹质量（0-1）
```

### 目标类型报告
```
reported_target_type
   default_time_to_declare <time-value>  # 默认：0 sec
   default_time_to_reevaluate <time-value>  # 默认：0 sec

   type <target_type>
      time_to_declare <time-value>
      time_to_reevaluate <time-value>
      report_type <type-name> <probability>
      report_type <type-name> emitter <emitter-name>

   default_type
      time_to_declare <time-value>
      time_to_reevaluate <time-value>
      report_type <type-name> <probability>
      report_truth
end_reported_target_type
```

### 发射机类型报告
```
reported_emitter_type
   default_time_to_declare <time-value>
   default_time_to_reevaluate <time-value>

   type <emitter_type>
      time_to_declare <time-value>
      time_to_reevaluate <time-value>
      report_type <type-name> <probability>

   default_type
      report_truth
end_reported_emitter_type
```

### 完整示例
```
sensor my_esm WSF_ESM_SENSOR
   mode passive_detection
      frame_time 5 sec

      # 定义多个频段
      frequency_band 1000 mhz 2000 mhz
         dwell_time 0.1 sec
         revisit_time 1.0 sec

      frequency_band 8000 mhz 12000 mhz
         dwell_time 0.1 sec
         revisit_time 1.0 sec

      receiver
         antenna_pattern omni_pattern
         internal_loss 2 dB
      end_receiver

      # 检测灵敏度
      continuous_detection_sensitivity -80.0 dBm
      pulsed_detection_sensitivity -75.0 dBm

      # 检测门限
      detection_threshold 3.0 dB

      # 扫描-扫描模型
      scan_on_scan_model true

      # 误差参数
      azimuth_error_sigma 2.0 deg
      elevation_error_sigma 5.0 deg

      # 测距
      ranging_time 10.0 sec
      ranging_time_track_quality 0.8

      # 报告设置
      reports_location
      reports_frequency
   end_mode

   # 发射机类型报告
   reported_emitter_type
      default_time_to_declare 2.0 sec
      default_type
         report_truth
   end_reported_emitter_type
end_sensor
```

---

## 3. WSF_EOIR_SENSOR - 光电/红外传感器

### 基本语法
```
sensor <name> WSF_EOIR_SENSOR
   mode <mode-name>
      frame_time <time> sec

      [resolution parameters]
      [band parameters]
      [atmospheric parameters]
      [detection parameters]

      receiver
         [receiver parameters]
      end_receiver
   end_mode
end_sensor
```

### 分辨率和像素

#### 方式1：角分辨率
```
angular_resolution <angle-value>         # 像素张角
```

#### 方式2：像素数量
```
pixel_count <horizontal> <vertical>      # 图像宽度和高度（像素）
```
- 如果指定pixel_count，角分辨率由FOV/像素数计算
- 必须指定`angular_resolution`或`pixel_count`之一

### 波段选择
```
band [visual | short | medium | long | very_long]
```
- **visual**: 380-760 nm（可见光）
- **short**: 1-3 μm（短波红外）
- **medium**: 3-5 μm（中波红外）
- **long**: 8-12 μm（长波红外）
- **very_long**: 15-30 μm（超长波红外）

### 大气参数

#### 大气衰减
```
atmospheric_attenuation <value> per <length-value>
```
- 海平面单位距离衰减的信号分数（0到1之间）
- 随高度变化自动调整空气密度
- 默认：0.0 per meter

#### 背景辐射
```
background_radiance <value> <power-units>/<angle-units>/<area-units>
```
或分别设置地平线上下：
```
background_radiance_above_horizon <value> <units>
background_radiance_below_horizon <value> <units>
background_transition_angle <lower-angle> <upper-angle>
```
- 过渡角度相对于地平线的局部角度
- 正值在地平线以上，负值在地平线以下
- 在过渡区域内线性插值

### 检测参数
```
detection_threshold <value>              # 信噪比门限（必须指定）
noise_equivalent_irradiance <value> <power-units>/<area-units>  # NEI（必须指定）
```

### Receiver参数
```
receiver
   antenna_pattern <pattern-name>        # 伪天线方向图
   internal_loss <db-ratio>              # 附加恒定损耗（默认：0 dB）
end_receiver
```

### 红外传感器示例
```
sensor my_ir_sensor WSF_EOIR_SENSOR
   mode ir_search
      frame_time 1.0 sec

      azimuth_field_of_view 60.0 deg
      elevation_field_of_view 45.0 deg

      pixel_count 640 480

      band medium  # 3-5 μm中波红外

      atmospheric_attenuation 0.0001 per meter

      background_radiance_above_horizon 100.0 W/sr/m^2
      background_radiance_below_horizon 300.0 W/sr/m^2
      background_transition_angle -5.0 deg 5.0 deg

      detection_threshold 5.0
      noise_equivalent_irradiance 1.0e-8 W/m^2

      receiver
         antenna_pattern ir_window_pattern
         internal_loss 2.0 dB
      end_receiver
   end_mode
end_sensor
```

### 可见光传感器示例
```
sensor my_eo_sensor WSF_EOIR_SENSOR
   mode visual_search
      frame_time 0.5 sec

      azimuth_field_of_view 30.0 deg
      elevation_field_of_view 20.0 deg

      angular_resolution 0.001 deg

      band visual  # 380-760 nm可见光

      atmospheric_attenuation 0.00005 per meter

      background_radiance 500.0 W/sr/m^2

      detection_threshold 3.0
      noise_equivalent_irradiance 5.0e-9 W/m^2

      receiver
         internal_loss 1.0 dB
      end_receiver
   end_mode
end_sensor
```

---

## 通用传感器参数

所有传感器类型都支持以下通用参数：

### 视场角（FOV）
```
azimuth_field_of_view <angle-value>      # 方位视场
elevation_field_of_view <angle-value>    # 俯仰视场
azimuth_beamwidth <angle-value>          # 方位波束宽度
elevation_beamwidth <angle-value>        # 俯仰波束宽度
```

### 误差参数
```
azimuth_error_sigma <angle-value>        # 方位误差标准差
elevation_error_sigma <angle-value>      # 俯仰误差标准差
range_error_sigma <length-value>         # 距离误差标准差
```

### 报告选项
```
reports_range                            # 报告距离
reports_range_rate                       # 报告距离变化率
reports_bearing                          # 报告方位
reports_elevation                        # 报告仰角
reports_location                         # 报告位置
reports_frequency                        # 报告频率（ESM）
reports_signal_to_noise                  # 报告信噪比
```

### 轨迹管理
```
filter <filter-type>                     # 滤波器类型
   [filter parameters]
end_filter

hits_to_establish_track <m> <n>          # m/n规则建立航迹
hits_to_maintain_track <m> <n>           # m/n规则维持航迹
```

### 处理器链接
```
processor <processor-name>               # 链接到处理器
```

---

## 传感器类型对比

| 传感器类型 | 主要用途 | 关键参数 | 检测方式 |
|-----------|---------|---------|---------|
| **WSF_RADAR_SENSOR** | 主动雷达探测 | 发射功率、PRF、脉冲宽度 | 主动发射接收 |
| **WSF_ESM_SENSOR** | 被动RF检测 | 检测灵敏度、频段 | 被动接收 |
| **WSF_EOIR_SENSOR** | 光电/红外成像 | 像素数、波段、NEI | 被动成像 |

---

## 最佳实践

### 1. 雷达传感器
- 合理设置发射功率和PRF
- 使用适当的Swerling模型
- 考虑地形遮蔽效应
- 设置合理的虚警概率

### 2. ESM传感器
- 定义覆盖目标频段
- 设置合理的检测灵敏度
- 使用扫描-扫描模型提高真实性
- 考虑测距时间

### 3. 光电/红外传感器
- 选择合适的波段
- 设置合理的背景辐射
- 考虑大气衰减效应
- 使用足够的像素分辨率

### 4. 通用建议
- 始终设置误差参数
- 使用合适的滤波器
- 设置合理的航迹建立/维持规则
- 链接到适当的处理器

---

## 参考

- 完整API: `script_api_reference.md`
- 使用示例: `examples.md`
- 命令参考: `commands_reference.md`
- Mover类型: `mover_reference.md`
