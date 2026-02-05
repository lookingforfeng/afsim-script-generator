---
name: afsim-script-generator
description: Generate and execute AFSIM (Advanced Framework for Simulation, Integration and Modeling) scripts. Use when the user needs to: (1) Create AFSIM/WSF scenario scripts, (2) Generate simulation scripts with proper syntax, (3) Run AFSIM simulations using mission.exe, (4) Debug or fix AFSIM script syntax errors, (5) Work with AFSIM scripting language, or (6) Execute and validate AFSIM simulation outputs. Supports complete AFSIM 2.9.0 scripting language syntax including platforms, sensors, weapons, behaviors, and mission scenarios.
---

# AFSIM Script Generator

Expert system for generating syntactically correct AFSIM 2.9.0 scripts and executing them using mission.exe.

---

## 📚 Quick Navigation

### 🚨 Start Here (CRITICAL)
- [Critical Rules](#-critical-rules) - **READ FIRST** - Common mistakes that cause failures
- [Quick Start Guide](#-quick-start-guide) - Get started in 4 steps

### 📖 Core References
- [File Structure](#-file-structure-reference) - Standard AFSIM script structure
- [Mover Types](#-mover-types-reference) - All 22+ mover types with parameters
- [Script API](#-script-api-reference) - WsfPlatform, WsfSensor, WsfWeapon classes
- [Commands](#-commands-reference) - Platform, route, sensor, weapon commands
- [Message Types](#-message-types-reference) - WsfMessage system and all message types
- [Sensor Types](#-sensor-types-reference) - Radar, ESM, EO/IR sensor parameters
- [Examples](#-examples-reference) - Complete working examples

### 🔧 Advanced Topics
- [Script Execution](#-script-execution) - Running scripts with mission.exe
- [Troubleshooting](#-troubleshooting) - Common errors and solutions

---

## 🚨 Critical Rules

**MUST READ BEFORE GENERATING ANY SCRIPT**

### Rule 1: File Extension
```
✅ CORRECT: my_script.txt
❌ WRONG:   my_script.wsf
```
**AFSIM scripts MUST use `.txt` extension, NOT `.wsf`**

### Rule 2: Units Required
```
✅ CORRECT: speed 100 m/sec
❌ WRONG:   speed 100

✅ CORRECT: altitude 5000 ft
❌ WRONG:   altitude 5000

✅ CORRECT: update_interval 1.0 sec
❌ WRONG:   update_interval 1.0
```
**ALL numeric parameters MUST include units**

### Rule 3: End Tags Required
```
✅ CORRECT:
mover WSF_AIR_MOVER
   maximum_speed 500 m/sec
end_mover

❌ WRONG:
mover WSF_AIR_MOVER
   maximum_speed 500 m/sec
# Missing end_mover!
```
**Every block MUST have its corresponding `end_*` tag**

### Rule 4: Coordinate Format
```
✅ CORRECT: position 38:44:52.3n 90:21:36.4w
❌ WRONG:   position 38.44.52.3n 90.21.36.4w
```
**Use colon `:` to separate degrees:minutes:seconds**

### Rule 5: Script API Methods
```
✅ CORRECT: PLATFORM.Name()
✅ CORRECT: PLATFORM.Latitude()
✅ CORRECT: PLATFORM.Altitude()

❌ WRONG: Position()      # Does not exist
❌ WRONG: Geodetic()      # Does not exist
❌ WRONG: Time()          # Use TIME_NOW instead
```
**Only use documented API methods from script_api_reference.md**

**For complete error list:** See `references/common_mistakes.md`

---

## ⚙️ Configuration

### config.txt - AFSIM Installation Directory

**Location:** `config.txt` in skill root directory

The skill uses a configuration file to locate your AFSIM installation. This makes it portable across different computers.

**Configuration File:**
```
# AFSIM Installation Directory
AFSIM_INSTALL_DIR=D:\Program Files\afsim2.9.0
```

**Derived Paths:**
- **mission.exe**: `{AFSIM_INSTALL_DIR}/bin/mission.exe`
- **Documentation**: `{AFSIM_INSTALL_DIR}/documentation/html/docs`

**To use on a different computer:**
1. Open `config.txt`
2. Update `AFSIM_INSTALL_DIR` to your AFSIM installation path
3. Save the file

All paths (mission.exe, documentation) are automatically derived from this setting.

### Documentation Directory - Ultimate Reference

**Location:** `{AFSIM_INSTALL_DIR}/documentation/html/docs`

The AFSIM documentation directory contains **1602 HTML files** with complete, authoritative information about every AFSIM feature.

**When to use:**
- ✅ Need to confirm very specific details
- ✅ Looking for obscure parameters or options
- ✅ Want to see official examples
- ✅ Need to verify edge cases

**When NOT to use:**
- ❌ For common tasks (use skill references instead)
- ❌ For quick lookups (use SKILL.md navigation)
- ❌ For examples (use examples.md)

**Think of it as:** The ultimate fallback reference when skill documentation doesn't cover a specific detail.

---

## 🚀 Quick Start Guide

### Step 1: Understand Requirements
Ask the user about:
- **Scenario type**: Air-to-air, air-to-ground, ISR, naval, etc.
- **Platforms**: Aircraft, ships, ground vehicles, satellites
- **Sensors**: Radar, ESM, EO/IR, etc.
- **Weapons**: Missiles, bombs, guns
- **Mission timeline**: Duration, key events
- **Output needs**: Event logs, tracks, engagement results

### Step 2: Generate Script
1. **Start with file structure** (see [File Structure Reference](#-file-structure-reference))
2. **Define platform types** with movers (see [Mover Types](#-mover-types-reference))
3. **Add sensors/weapons** (see [Commands Reference](#-commands-reference))
4. **Create platform instances** with routes
5. **Add processors** for behaviors (see [Script API](#-script-api-reference))
6. **Set simulation end time**

### Step 3: Execute Script
```bash
python scripts/run_mission.py <script_file.txt> [options]
```

Options:
- `-es` - Event-stepped (default)
- `-rt` - Real-time frame-stepped
- `-fs` - Non-realtime frame-stepped
- `-fio` - Flush output
- `-sm` - Suppress messages

### Step 4: Validate and Iterate
- Check mission.exe output for errors
- Verify simulation results
- Adjust script and re-run as needed

---

## 📁 File Structure Reference

**Location:** `references/file_structure.md`

Standard AFSIM script structure:

```
# Header comments
script_interface
   debug
end_script_interface

# Output configuration
event_output
   file output/simulation.evt
   enable all
end_event_output

# Reusable definitions
antenna_pattern [name] [...]
sensor [name] [type] [...]
weapon [name] [type] [...]

# Platform types
platform_type [name] WSF_PLATFORM
   mover [type]
      [parameters]
   end_mover

   sensor [name] [type]
      [parameters]
   end_sensor

   processor [name] [type]
      [parameters]
   end_processor
end_platform_type

# Platform instances
platform [instance-name] [type]
   side [blue|red|white]

   route
      position [lat] [lon] altitude [alt] speed [speed]
   end_route
end_platform

# Simulation control
end_time [duration] sec
```

**For complete structure guide:** Read `references/file_structure.md`

---

## 🚁 Mover Types Reference

**Location:** `references/mover_reference.md`

AFSIM supports 22+ mover types for different platform categories:

### Air Movers
- **WSF_AIR_MOVER** - Standard fixed-wing aircraft
- **WSF_HELO_MOVER** - Helicopters and rotorcraft
- **WSF_GUIDED_MOVER** - Guided missiles and munitions

### Ground Movers
- **WSF_GROUND_MOVER** - Ground vehicles
- **WSF_RAIL_MOVER** - Rail-based systems

### Naval Movers
- **WSF_SURFACE_MOVER** - Surface ships
- **WSF_SUBSURFACE_MOVER** - Submarines

### Space Movers
- **WSF_ORBITAL_MOVER** - Satellites and orbital platforms
- **WSF_BALLISTIC_MOVER** - Ballistic missiles

### Special Movers
- **WSF_STATIONARY_MOVER** - Fixed installations
- **WSF_SCRIPTED_MOVER** - Custom movement logic

**Example:**
```
mover WSF_AIR_MOVER
   maximum_speed 500 m/sec
   minimum_speed 100 m/sec
   default_radial_acceleration 5.0 g
   default_climb_rate 50 m/sec
end_mover
```

**For complete mover reference:** Read `references/mover_reference.md`

---

## 🔧 Script API Reference

**Location:** `references/script_api_reference.md`

### Core Classes

#### WsfPlatform
Platform access and control:
```
string Name()                    # Get platform name
string Type()                    # Get platform type
double Latitude()                # Get latitude (deg)
double Longitude()               # Get longitude (deg)
double Altitude()                # Get altitude (m)
double X(), Y(), Z()             # Get XYZ position (m)
double Heading()                 # Get heading (deg)
double Speed()                   # Get speed (m/s)
WsfSensor Sensor(string name)    # Get sensor by name
WsfWeapon Weapon(string name)    # Get weapon by name
WsfProcessor Processor(string)   # Get processor by name
int SensorCount()                # Number of sensors
WsfSensor SensorEntry(int i)     # Get sensor by index
```

#### WsfSensor
Sensor access and control:
```
string Name()                    # Get sensor name
string Type()                    # Get sensor type
bool IsTurnedOn()                # Check if sensor is on
void TurnOn()                    # Turn sensor on
void TurnOff()                   # Turn sensor off
```

#### WsfWeapon
Weapon access and control:
```
string Name()                    # Get weapon name
string Type()                    # Get weapon type
int QuantityRemaining()          # Get remaining quantity
bool Fire(WsfTrack target)       # Fire at target
```

#### WsfTrack
Track information:
```
WsfTrackId TrackId()             # Get track ID
string TargetName()              # Get target name
double Latitude()                # Get track latitude
double Longitude()               # Get track longitude
double Altitude()                # Get track altitude
double Range()                   # Get range to track
bool LocationValid()             # Check if location valid
```

#### Array<T> and Map<K,V>
Collections:
```
# Array methods
void PushBack(T value)           # Add element
T Get(int index)                 # Get element
int Size()                       # Get size
ArrayIterator GetIterator()      # Get iterator

# Map methods
void Insert(K key, V value)      # Insert key-value pair
V Get(K key)                     # Get value by key
bool Contains(K key)             # Check if key exists
int Size()                       # Get size
```

### Global Variables
```
PLATFORM                         # Current platform
PROCESSOR                        # Current processor
SENSOR                           # Current sensor
TRACK                            # Current track
MESSAGE                          # Current message
TIME_NOW                         # Current simulation time
```

**For complete API reference:** Read `references/script_api_reference.md`

---

## 📋 Commands Reference

**Location:** `references/commands_reference.md`

### Platform Commands
```
platform [name] [type]
   side [blue|red|white|...]
   position [lat] [lon] altitude [alt]
   command_chain [name] [commander|SELF]

   route
      position [lat] [lon] altitude [alt] speed [speed]
   end_route

   sensor [name]
      on  # or off
   end_sensor

   weapon [name]
      quantity [number]
      firing_interval [time] sec
   end_weapon
end_platform
```

### Route Commands
```
route
   position [lat] [lon] altitude [alt] speed [speed]
   position [lat] [lon] altitude [alt] agl speed [speed]
   position [lat] [lon]  # Uses previous altitude/speed
end_route
```

### Sensor Commands
```
sensor [name] [type]
   frame_time [time] sec
   location [x] [y] [z]
   minimum_range [range] nm
   maximum_range [range] nm
   processor [processor-name]
end_sensor
```

### Weapon Commands
```
weapon [name] [type]
   launched_platform_type [type]
   weapon_effects [effects-name]
   category [category-name]
end_weapon
```

### Processor Commands
```
processor [name] [type]
   update_interval [time] sec

   script_variables
      [type] [name] = [value];
   end_script_variables

   script [return-type] [name]([parameters])
      # Script code
   end_script

   on_initialize
      # Initialization code
   end_on_initialize

   on_update
      # Update code
   end_on_update
end_processor
```

**For complete commands reference:** Read `references/commands_reference.md`

---

## 📨 Message Types Reference

**Location:** `references/message_types_reference.md`

AFSIM消息系统用于平台、传感器、处理器之间的通信。

### 核心消息类型

#### WsfMessage (基类)
所有消息的基类：
```javascript
string Originator()                      // 消息发起平台
string Type()                            // 消息类型
int Priority()                           // 消息优先级
void SetAuxData(string name, value)      // 设置辅助数据
```

#### WsfTrackMessage
传递轨迹信息：
```javascript
WsfTrack Track()                         // 获取轨迹
void SetTrack(WsfTrack aTrack)           // 设置轨迹
```

#### WsfControlMessage
发送控制命令：
```javascript
void SetFunction(string aFunction)       // 设置功能
void SetResource(string aResource)       // 设置资源
void SetTrack(WsfTrack aTrack)           // 设置关联轨迹
```

#### WsfStatusMessage
报告状态：
```javascript
void SetStatus(string aStatus)           // 设置状态
void SetSystemName(string aSystemName)   // 设置系统名称
```

#### WsfBMTrackMessage
战场管理轨迹（功能最丰富）：
```javascript
void SetLLA(double lat, double lon, double alt)  // 设置位置
void SetIFFFriendly()                    // 设置IFF为友方
void SetTrackingStatusNormal()           // 设置跟踪状态
```

### 消息处理示例
```javascript
on_message
   type WSF_TRACK_MESSAGE
      script
         WsfTrackMessage msg = (WsfTrackMessage)MESSAGE;
         WsfTrack track = msg.Track();
         // 处理轨迹消息
      end_script

   type WSF_CONTROL_MESSAGE
      script
         WsfControlMessage msg = (WsfControlMessage)MESSAGE;
         // 处理控制消息
      end_script
end_on_message
```

**For complete message types reference:** Read `references/message_types_reference.md`

---

## 📡 Sensor Types Reference

**Location:** `references/sensor_types_reference.md`

AFSIM提供多种特殊传感器类型，每种都有特定的参数和配置。

### WSF_RADAR_SENSOR - 雷达传感器

主动雷达探测传感器：

**关键参数：**
```
transmitter
   frequency <frequency>                 // 工作频率
   power <power>                         // 发射功率
   pulse_width <time>                    // 脉冲宽度
   pulse_repetition_frequency <freq>     // PRF
   antenna_pattern <pattern-name>        // 天线方向图
end_transmitter

receiver
   noise_figure <db-ratio>               // 噪声系数
   bandwidth <frequency>                 // 接收带宽
end_receiver

swerling_case [0|1|2|3|4]                // Swerling目标模型
number_of_pulses_integrated <integer>    // 积分脉冲数
one_m2_detect_range <length>             // 1平方米目标检测距离
```

### WSF_ESM_SENSOR - ESM传感器

被动RF检测传感器（RWR、SIGINT、ELINT）：

**关键参数：**
```
frequency_band <lower-freq> <upper-freq>
   dwell_time <time>                     // 驻留时间
   revisit_time <time>                   // 重访时间

continuous_detection_sensitivity <db-power>  // 连续波灵敏度
pulsed_detection_sensitivity <db-power>      // 脉冲灵敏度
detection_threshold <db-ratio>           // 信噪比门限
scan_on_scan_model <boolean>             // 扫描-扫描模型
ranging_time <time>                      // 测距时间
```

### WSF_EOIR_SENSOR - 光电/红外传感器

光学或红外成像传感器：

**关键参数：**
```
pixel_count <horizontal> <vertical>      // 像素数量
band [visual|short|medium|long|very_long]  // 波段选择
atmospheric_attenuation <value> per <length>  // 大气衰减
background_radiance <value> <units>      // 背景辐射
detection_threshold <value>              // 信噪比门限
noise_equivalent_irradiance <value> <units>  // NEI
```

### 传感器类型对比

| 传感器 | 用途 | 检测方式 | 关键参数 |
|-------|------|---------|---------|
| **RADAR** | 主动雷达 | 主动发射接收 | 功率、PRF、脉冲宽度 |
| **ESM** | 被动RF | 被动接收 | 灵敏度、频段 |
| **EOIR** | 光电/红外 | 被动成像 | 像素、波段、NEI |

**For complete sensor types reference:** Read `references/sensor_types_reference.md`

---

## 📝 Examples Reference

**Location:** `references/examples.md`

### Example 1: Basic Air Platform
Simple aircraft with route and script processor

### Example 2: Strike Mission
Complete scenario with sensors, weapons, track sharing, and engagement logic

### Example 3: Ground Patrol
Ground vehicle with patrol route

### Example 4: Naval Platform
Surface ship with radar sensor

### Common Patterns
- Script variables declaration
- Looping through collections
- Conditional logic
- Message handling
- Accessing platform components

**For complete examples:** Read `references/examples.md`

---

## ⚙️ Script Execution

### Configuration

The skill reads AFSIM installation directory from `config.txt`:
```
AFSIM_INSTALL_DIR=D:\Program Files\afsim2.9.0
```

All paths are derived from this:
- **mission.exe**: `{AFSIM_INSTALL_DIR}/bin/mission.exe`
- **Documentation**: `{AFSIM_INSTALL_DIR}/documentation/html/docs`

### Using run_mission.py
```bash
# Basic execution
python scripts/run_mission.py my_script.txt

# With options
python scripts/run_mission.py my_script.txt -es -fio

# Real-time mode
python scripts/run_mission.py my_script.txt -rt
```

The script will:
1. Load configuration from `config.txt`
2. Verify mission.exe exists
3. Display configuration paths
4. Execute the script
5. Capture and display output

### Execution Modes
- **Event-stepped (-es)**: Default, fastest execution
- **Real-time (-rt)**: Runs in real-time with frame stepping
- **Frame-stepped (-fs)**: Non-realtime frame stepping

### Output Files
Scripts generate output in the `output/` directory:
- `.evt` - Event log files
- `.rep` - Binary replay files
- Console output from mission.exe

### Troubleshooting Configuration

**Problem:** mission.exe not found
- **Solution:**
  1. Open `config.txt`
  2. Verify `AFSIM_INSTALL_DIR` points to your AFSIM installation
  3. Check that `{AFSIM_INSTALL_DIR}/bin/mission.exe` exists

**Problem:** Different computer, different path
- **Solution:**
  1. Copy the entire skill directory
  2. Update `AFSIM_INSTALL_DIR` in `config.txt`
  3. Everything else works automatically

---

## 🔍 Troubleshooting

### Syntax Errors

**Problem:** "Unexpected token" or "Parse error"
- **Solution:** Check `references/common_mistakes.md` for common syntax errors
- Verify all blocks have `end_*` tags
- Check coordinate format (use `:` not `.`)
- Ensure all numbers have units

**Problem:** "Unknown command"
- **Solution:** Verify command syntax in `references/commands_reference.md`
- Check spelling and capitalization
- Ensure command is in correct context

### Execution Errors

**Problem:** mission.exe not found
- **Solution:** Verify path is `D:\Program Files\afsim2.9.0\bin\mission.exe`
- Check file permissions
- Ensure AFSIM 2.9.0 is installed

**Problem:** Script file not found
- **Solution:** Use `.txt` extension, not `.wsf`
- Check file path is correct
- Ensure file exists in specified location

### Runtime Errors

**Problem:** Platform not moving
- **Solution:** Check mover parameters in `references/mover_reference.md`
- Verify route has valid waypoints
- Ensure speed is specified with units

**Problem:** Sensor not detecting
- **Solution:** Verify sensor is turned on
- Check sensor range and parameters
- Ensure target is within sensor coverage

**Problem:** Script variables not working
- **Solution:** Declare variables in `script_variables` block
- Check variable types match usage
- Verify semicolons after declarations

---

## 📚 Complete Reference Library

All reference files are located in the `references/` directory:

1. **common_mistakes.md** - 10 critical rules to avoid common errors
2. **file_structure.md** - Standard AFSIM script file structure and templates
3. **mover_reference.md** - Complete reference for all 22+ mover types
4. **script_api_reference.md** - Full API for WsfPlatform, WsfSensor, WsfWeapon, etc. (158 methods)
5. **commands_reference.md** - Complete command syntax reference
6. **message_types_reference.md** - ⭐ NEW: WsfMessage system and all message types
7. **sensor_types_reference.md** - ⭐ NEW: Radar, ESM, EO/IR sensor parameters
8. **examples.md** - Working examples and common patterns

**Load these files as needed for detailed information.**

---

## 🎯 Best Practices

1. **Always start with file_structure.md** to understand the standard layout
2. **Check common_mistakes.md** before generating any script
3. **Use examples.md** as templates for common scenarios
4. **Verify mover types** in mover_reference.md before defining platforms
5. **Reference script_api_reference.md** when writing processor scripts
6. **Test incrementally** - start simple, add complexity gradually
7. **Use meaningful names** for platforms, sensors, weapons
8. **Add comments** to explain complex logic
9. **Validate coordinates** - use proper lat/lon format
10. **Check units** - every number needs units

---

## 📞 Support

### Configuration
- **Config File**: `config.txt` in skill root directory
- **Default Install**: `D:\Program Files\afsim2.9.0`
- **Update for your system**: Edit `AFSIM_INSTALL_DIR` in config.txt

### AFSIM Resources
- **Installation**: Configured via `config.txt`
- **Documentation**: `{AFSIM_INSTALL_DIR}/documentation/html/docs` (1602 HTML files)
- **Mission.exe**: `{AFSIM_INSTALL_DIR}/bin/mission.exe`
- **Version**: AFSIM 2.9.0

### Documentation Hierarchy
1. **SKILL.md** - Quick reference and navigation (use first)
2. **references/** - Comprehensive skill documentation (use for details)
3. **{AFSIM_INSTALL_DIR}/documentation/** - Ultimate official reference (use for edge cases)

---

## 🔄 Workflow Summary

```
1. Understand Requirements
   ↓
2. Check common_mistakes.md
   ↓
3. Use file_structure.md as template
   ↓
4. Add platform types (mover_reference.md)
   ↓
5. Add sensors/weapons (commands_reference.md)
   ↓
6. Add behaviors (script_api_reference.md)
   ↓
7. Create platform instances
   ↓
8. Save as .txt file
   ↓
9. Execute with run_mission.py
   ↓
10. Validate output and iterate
```

**Remember: File extension MUST be `.txt` and ALL numbers MUST have units!**
