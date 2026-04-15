---
name: afsim-script-generator
description: "Generate and execute AFSIM (Advanced Framework for Simulation, Integration and Modeling) scripts. Use when the user needs to: (1) Create AFSIM/WSF scenario scripts, (2) Generate simulation scripts with proper syntax, (3) Run AFSIM simulations using mission.exe, (4) Debug or fix AFSIM script syntax errors, (5) Work with AFSIM scripting language, or (6) Execute and validate AFSIM simulation outputs. Supports complete AFSIM 2.9.0 scripting language syntax including platforms, sensors, weapons, behaviors, and mission scenarios."
---

# AFSIM Script Generator

Expert system for generating syntactically correct AFSIM 2.9.0 scripts and executing them using mission.exe.

## Configuration

The skill reads the AFSIM installation directory from `config.txt` in the skill root:

```
AFSIM_INSTALL_DIR=D:\Program Files\afsim2.9.0
```

**Derived paths:**
- **mission.exe**: `{AFSIM_INSTALL_DIR}/bin/mission.exe`
- **Documentation**: `{AFSIM_INSTALL_DIR}/documentation/html/docs` (1602 HTML files — use as ultimate fallback for edge cases)

To use on a different computer, update `AFSIM_INSTALL_DIR` in `config.txt`. All paths derive from it automatically.

## Critical Rules

**Read before generating any script.** Also see `references/script_syntax_critical.md` and `references/common_mistakes.md` for the full error catalogue.

### Rule 1: File Extension — use `.txt`, NOT `.wsf`

```
my_script.txt    # correct
my_script.wsf    # wrong — AFSIM will not load it
```

### Rule 2: Units Required on ALL numeric parameters

```
speed 100 m/sec           # correct
altitude 5000 ft          # correct
update_interval 1.0 sec   # correct
speed 100                 # wrong — missing unit
```

### Rule 3: Every block MUST have its `end_*` tag

```
mover WSF_AIR_MOVER
   maximum_speed 500 m/sec
end_mover
```

### Rule 4: Coordinate format — colon-separated DMS

```
position 38:44:52.3n 90:21:36.4w    # correct
position 38.44.52.3n 90.21.36.4w    # wrong — use colons
```

### Rule 5: Only use documented Script API methods

```
PLATFORM.Name()       # correct
PLATFORM.Latitude()   # correct
TIME_NOW              # correct — global variable for current sim time
Position()            # wrong — does not exist
Time()                # wrong — use TIME_NOW instead
```

### Key syntax pitfalls (脚本语法关键规则)

- Use `print()` for output, not `cout`
- Write code directly in `on_initialize` — do not wrap in `script`
- Antenna patterns require a `constant_pattern` sub-block
- Pulse width uses scientific notation (`1.0e-6 sec`), not `microsec`
- No ternary operators or `fmod` — use `if-else` and time-delta comparisons
- `WSF_AIR_MOVER` does not support `climb_rate` — only use documented parameters

## Minimal Working Example

A complete, runnable script that flies one aircraft along a route:

```
# File: hello_afsim.txt

script_interface
   debug
end_script_interface

event_output
   file output/hello.evt
   enable all
end_event_output

platform_type basic-jet WSF_PLATFORM
   mover WSF_AIR_MOVER
      maximum_speed 300 m/sec
   end_mover

   processor status-printer WSF_SCRIPT_PROCESSOR
      update_interval 5.0 sec
      on_update
         print("Time=", TIME_NOW, " Alt=", PLATFORM.Altitude());
      end_on_update
   end_processor
end_platform_type

platform jet-1 basic-jet
   side blue
   route
      position 38:44:52.3n 90:21:36.4w altitude 10000 ft speed 250 m/sec
      position 38:50:00.0n 90:10:00.0w
   end_route
end_platform

end_time 120 sec
```

Save as `.txt`, then run:

```bash
python scripts/run_mission.py hello_afsim.txt -es -fio
```

**For more examples** (strike missions, naval scenarios, ground patrols): Read `references/examples.md`

## Workflow

### 1. Gather Requirements

Ask the user about scenario type (air-to-air, ISR, naval, etc.), platforms, sensors, weapons, mission timeline, and desired outputs.

### 2. Generate Script

Follow this structure order — see `references/file_structure.md` for the full template:

1. `script_interface` and `event_output` blocks
2. Reusable definitions (antenna patterns, sensors, weapons)
3. `platform_type` blocks with movers, sensors, processors
4. `platform` instances with sides and routes
5. `end_time` to set simulation duration

### 3. Execute

```bash
python scripts/run_mission.py <script_file.txt> [options]
```

| Flag | Mode | Use case |
|------|------|----------|
| `-es` | Event-stepped (default) | Fastest execution |
| `-rt` | Real-time frame-stepped | Watch simulation unfold |
| `-fs` | Non-realtime frame-stepped | Controlled stepping |
| `-fio` | Flush output | See output immediately |
| `-sm` | Suppress messages | Reduce console noise |

### 4. Validate Output

After execution, check for success or failure:

- **Success**: mission.exe prints simulation events and exits cleanly. Output files appear in `output/` (`.evt` event logs, `.rep` replay files).
- **Failure**: Look for `ERROR` or `Parse error` lines in the console output. The error message includes a line number — cross-reference it with the script to find the issue.

**Common validation fixes:**
- `Unexpected token` → missing `end_*` tag or wrong coordinate format. See `references/common_mistakes.md`.
- `Unknown command` → check spelling and context in `references/commands_reference.md`.
- Platform not moving → verify route waypoints have speed with units; check mover params in `references/mover_reference.md`.
- Sensor not detecting → confirm sensor is turned on, target is in range. See `references/sensor_types_reference.md`.

Fix the issue and re-run until output is clean.

## Reference Library

All detailed reference files are in the `references/` directory. Load as needed — keep the main workflow in SKILL.md light.

| File | Contents |
|------|----------|
| `script_syntax_critical.md` | Must-read syntax pitfalls with correct/incorrect examples |
| `common_mistakes.md` | 10 critical rules to avoid common errors |
| `file_structure.md` | Standard AFSIM script structure and block ordering |
| `mover_reference.md` | All 22+ mover types (air, ground, naval, space, special) with parameters |
| `script_api_reference.md` | Full API for WsfPlatform, WsfSensor, WsfWeapon, WsfTrack, collections (158 methods) |
| `commands_reference.md` | Complete syntax for platform, route, sensor, weapon, and processor commands |
| `message_types_reference.md` | WsfMessage system — track, control, status, and BM track messages |
| `sensor_types_reference.md` | WSF_RADAR_SENSOR, WSF_ESM_SENSOR, WSF_EOIR_SENSOR parameters |
| `examples.md` | Working examples — basic air, strike mission, ground patrol, naval platform |

**Global variables** available in all processor scripts: `PLATFORM`, `PROCESSOR`, `SENSOR`, `TRACK`, `MESSAGE`, `TIME_NOW`.

### Documentation Hierarchy

1. **SKILL.md** — rules, workflow, and quick reference (start here)
2. **references/** — comprehensive skill documentation (use for details)
3. **{AFSIM_INSTALL_DIR}/documentation/** — official AFSIM HTML docs (use for edge cases)
