---
name: afsim-script-generator
description: Generate and execute AFSIM (Advanced Framework for Simulation, Integration and Modeling) scripts. Use when the user needs to: (1) Create AFSIM/WSF scenario scripts, (2) Generate simulation scripts with proper syntax, (3) Run AFSIM simulations using mission.exe, (4) Debug or fix AFSIM script syntax errors, (5) Work with AFSIM scripting language, or (6) Execute and validate AFSIM simulation outputs. Supports complete AFSIM 2.9.0 scripting language syntax including platforms, sensors, weapons, behaviors, and mission scenarios.
---

# AFSIM Script Generator

This skill helps generate syntactically correct AFSIM scripts and execute them using mission.exe.

## ⚠️ 关键规则（生成脚本前必读）

**CRITICAL - 必须遵守以下规则，否则脚本会失败：**

1. **文件扩展名必须是 `.txt`** - 不是 `.wsf`！
2. **所有数值参数必须带单位** - 例如：`100 m/sec`、`30.0 sec`、`1000 m`
3. **所有代码块必须有结束标记** - `end_mover`、`end_platform_type`、`end_processor` 等
4. **不要使用不存在的脚本方法** - 避免 `Position()`、`Geodetic()`、`Time()` 等
5. **路由中不要使用 `loop` 命令** - 会导致语法错误

**详细错误说明和最佳实践：** 见 `references/common_mistakes.md`

## Quick Start

1. **Understand the requirement** - Ask clarifying questions about the simulation scenario
2. **Generate the script** - Create WSF script using AFSIM syntax
3. **Execute with mission.exe** - Run using `scripts/run_mission.py`
4. **Validate output** - Check results and iterate if needed

## AFSIM Overview

AFSIM (Advanced Framework for Simulation, Integration and Modeling) is a comprehensive simulation framework for modeling air, space, and ground operations. Scripts are written in a C-like language and saved as `.wsf` files.

**Installation Directory:** `D:\Program Files\afsim2.9.0`

## Script Generation Workflow

### 1. Gather Requirements

Ask the user about:
- Simulation scenario (air-to-air, air-to-ground, ISR, etc.)
- Platforms involved (aircraft, missiles, ground units, satellites)
- Sensors and weapons needed
- Mission timeline and events
- Output requirements

### 2. Generate Script

Use the AFSIM scripting language to create the scenario. Key elements:

**Basic Structure:**
```
// Comments use // or /* */
PLATFORM my_aircraft
{
    // Platform definition
}

SENSOR my_radar
{
    // Sensor definition
}

// Simulation control
RUN_SIMULATION
{
    // Runtime commands
}
```

**For detailed syntax, see:**
- `references/common_mistakes.md` - **READ THIS FIRST** - Common errors and best practices
- `references/language_grammar.md` - Complete language grammar
- `references/script_types.md` - Data types and methods
- `references/commands.md` - Command reference
- `references/examples.md` - Example patterns

### 3. Execute Script

Use the provided Python wrapper:

```bash
python scripts/run_mission.py <script_file.wsf> [options]
```

Options:
- `-es` - Event-stepped (default)
- `-rt` - Real-time frame-stepped
- `-fs` - Non-realtime frame-stepped
- `-fio` - Flush output
- `-sm` - Suppress messages

### 4. Validate and Iterate

- Check mission.exe output for errors
- Verify simulation results match expectations
- Adjust script and re-run as needed

## Common Script Patterns

### Platform Definition
```
PLATFORM aircraft_1
{
    TYPE air_vehicle
    POSITION 0.0 0.0 10000.0
    VELOCITY 250.0 0.0 0.0
}
```

### Sensor Definition
```
SENSOR radar_1
{
    TYPE radar
    PARENT aircraft_1
    RANGE 100000.0
}
```

### Weapon Definition
```
WEAPON missile_1
{
    TYPE air_to_air_missile
    PARENT aircraft_1
    QUANTITY 4
}
```

## Troubleshooting

**Syntax Errors:**
- Check grammar in `references/language_grammar.md`
- Verify command syntax in `references/commands.md`
- Review example scripts in `references/examples.md`

**Execution Errors:**
- Ensure mission.exe path is correct
- Check file permissions
- Verify all required files are present

**Output Issues:**
- Check simulation log files
- Verify output directory exists
- Review mission.exe console output

## Reference Files

Load these as needed for detailed information:

- **references/common_mistakes.md** - **START HERE** - Common errors and how to avoid them
- **references/language_grammar.md** - Complete scripting language grammar and syntax rules
- **references/script_types.md** - All available data types, classes, and their methods
- **references/commands.md** - Comprehensive command reference organized by category
- **references/examples.md** - Example scripts demonstrating common patterns

## Notes

- **AFSIM scripts use `.txt` extension** - NOT `.wsf`!
- **All numeric parameters require units** - e.g., `100 m/sec`, `30.0 sec`
- Scripts are text-based and human-readable
- mission.exe is located at `D:\Program Files\afsim2.9.0\bin\mission.exe`
- Output includes event logs, binary reports, and replay files
