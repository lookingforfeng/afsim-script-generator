# AFSIM Script File Structure

## File Extension
**CRITICAL**: AFSIM script files MUST use `.txt` extension, NOT `.wsf`

## Basic File Structure

```
# Header comments (optional but recommended)
################################################################################
# Script Description
# Purpose: [What this script does]
# Author: [Optional]
# Date: [Optional]
################################################################################

# Configuration sections
script_interface
   [options]
end_script_interface

event_output
   file output/[filename].evt
   enable all
end_event_output

dis_interface
   record output/[filename].rep
   [other options]
end_dis_interface

# Define reusable components
antenna_pattern [name] [...]
sensor [name] [type] [...]
weapon [name] [type] [...]
weapon_effects [name] [type] [...]
aero [name] [type] [...]
processor [name] [type] [...]

# Define platform types
platform_type [name] [model]
   mover [type]
      [mover parameters]
   end_mover

   sensor [name] [type]
      [sensor parameters]
   end_sensor

   weapon [name] [type]
      [weapon parameters]
   end_weapon

   processor [name] [type]
      [processor parameters]
   end_processor
end_platform_type

# Create platform instances
platform [instance-name] [platform-type]
   side [blue|red|white|...]

   route
      position [lat] [lon] altitude [alt] speed [speed]
      position [lat] [lon] altitude [alt] speed [speed]
   end_route

   sensor [sensor-name]
      [overrides]
   end_sensor

   weapon [weapon-name]
      [overrides]
   end_weapon
end_platform

# Simulation control
end_time [duration] sec
```

## Section Order (Recommended)

1. **Header Comments** - Description and metadata
2. **Script Interface** - Debug and configuration options
3. **Output Configuration** - Event and DIS output files
4. **Reusable Definitions** - Antenna patterns, sensors, weapons, etc.
5. **Platform Types** - Template definitions
6. **Platform Instances** - Actual scenario objects
7. **Simulation Control** - End time and other controls

## Common Sections

### Script Interface
```
script_interface
   debug              # Enable debug output
end_script_interface
```

### Event Output
```
event_output
   file output/simulation.evt
   enable all
end_event_output
```

### DIS Interface
```
dis_interface
   record output/simulation.rep
   mover_update_timer 5.0 seconds
   entity_position_threshold 10 m
   heartbeat_timer 5.0 seconds
end_dis_interface
```

### Platform Type Structure
```
platform_type [NAME] WSF_PLATFORM
   # Optional: icon, category
   icon [icon-name]
   category [category-name]

   # Required: mover
   mover [MOVER_TYPE]
      # Mover-specific parameters
   end_mover

   # Optional: sensors
   sensor [name] [TYPE]
      # Sensor parameters
      processor [processor-name]  # Optional
   end_sensor

   # Optional: weapons
   weapon [name] [TYPE]
      # Weapon parameters
   end_weapon

   # Optional: comm systems
   comm [name] [TYPE]
      # Comm parameters
   end_comm

   # Optional: processors
   processor [name] [TYPE]
      # Processor parameters

      # Script variables (optional)
      script_variables
         [type] [name] = [value];
      end_script_variables

      # Custom scripts (optional)
      script [return-type] [name]([parameters])
         # Script code
      end_script

      # Event handlers (optional)
      on_initialize
         # Initialization code
      end_on_initialize

      on_update
         # Update code
      end_on_update

      on_message
         type [MESSAGE_TYPE]
            script
               # Message handling code
            end_script
      end_on_message
   end_processor
end_platform_type
```

### Platform Instance Structure
```
platform [instance-name] [platform-type]
   side [blue|red|white|...]

   # Optional: command chain
   command_chain [chain-name] [commander|SELF]

   # Optional: position (static platform)
   position [lat] [lon] altitude [alt]

   # Optional: route (moving platform)
   route
      position [lat] [lon] altitude [alt] speed [speed]
      position [lat] [lon] altitude [alt] speed [speed]
      # ... more waypoints
   end_route

   # Optional: sensor overrides
   sensor [sensor-name]
      on  # or off
      # Other overrides
   end_sensor

   # Optional: weapon overrides
   weapon [weapon-name]
      quantity [number]
      firing_interval [time] sec
   end_weapon

   # Optional: processor overrides
   processor [processor-name]
      on  # or off
      update_interval [time] sec
   end_processor
end_platform
```

## Units Requirements

**CRITICAL**: All numeric parameters MUST include units. Common units:

### Distance
- `m` (meters)
- `ft` (feet)
- `nm` (nautical miles)
- `km` (kilometers)

### Speed
- `m/sec` or `m/s`
- `kts` (knots)
- `mph` (miles per hour)

### Time
- `sec` or `s` (seconds)
- `min` (minutes)
- `hr` (hours)

### Angle
- `deg` (degrees)
- `rad` (radians)

### Altitude Modifiers
- `agl` (above ground level)
- `msl` (mean sea level)

### Frequency
- `hz` (hertz)
- `mhz` (megahertz)
- `ghz` (gigahertz)

### Power
- `w` (watts)
- `kw` (kilowatts)

### Mass
- `kg` (kilograms)
- `lbm` (pounds mass)

### Acceleration
- `g` (gravitational acceleration)

## Coordinate Formats

### Latitude/Longitude
```
# Decimal degrees
38.5 deg
-90.25 deg

# Degrees:Minutes:Seconds with direction
38:44:52.3n
90:21:36.4w
39:31:42.42n
91:38:35.111w
```

### Position Command
```
position [lat] [lon] altitude [alt] speed [speed]
position [lat] [lon] altitude [alt] agl speed [speed]
position [lat] [lon]  # Uses previous altitude/speed
```

## Comments

```
# Single line comment

// Alternative single line comment

/* Multi-line comment
   can span multiple lines */
```

## Common Mistakes to Avoid

1. **Wrong file extension** - Use `.txt` not `.wsf`
2. **Missing units** - Every number needs units: `100 m/sec` not `100`
3. **Missing end tags** - Every block needs its `end_*` tag
4. **Incorrect coordinate format** - Use `38:44:52.3n` not `38.44.52.3n`
5. **Case sensitivity** - Command names are case-sensitive
6. **Missing semicolons in scripts** - Script statements need `;`
7. **Undeclared variables** - Use `script_variables` section
8. **Wrong script syntax** - Use `on_update` not `on_update()`
