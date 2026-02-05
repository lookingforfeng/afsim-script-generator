# AFSIM Commands Reference

## Platform Commands

### PLATFORM
Defines a platform instance.

```
PLATFORM my_aircraft
{
    platform_type 737
    initial_position 0.0 0.0 10000.0
    initial_velocity 250.0 0.0 0.0
}
```

### PLATFORM_TYPE
Defines a reusable platform type.

```
platform_type 737 WSF_PLATFORM
{
    mover WSF_AIR_MOVER
    end_mover
}
```

## Sensor Commands

### SENSOR
Defines a sensor on a platform.

```
sensor my_radar WSF_RADAR_SENSOR
{
    parent my_aircraft
    range 100000.0
}
```

## Weapon Commands

### WEAPON
Defines a weapon on a platform.

```
weapon my_missile WSF_AIR_TO_AIR_MISSILE
{
    parent my_aircraft
    quantity 4
}
```

## Script Commands

### SCRIPT
Defines a script function.

```
script void MyFunction(int param)
{
    print("Value: ", param);
}
end_script
```

### SCRIPT_INTERFACE
Configures script debugging.

```
script_interface
    debug
end_script_interface
```

### SCRIPT_VARIABLES
Declares instance variables.

```
script_variables
    int myVar = 0;
    double speed = 250.0;
end_script_variables
```

### Common Script Hooks

#### on_initialize
Runs once when component initializes.

```
on_initialize
    print("Initializing...");
end_on_initialize
```

#### on_update
Runs periodically based on update_interval.

```
on_update
    print("Updating...");
end_on_update
```

## Processor Commands

### PROCESSOR
Defines a script processor.

```
processor my_proc WSF_SCRIPT_PROCESSOR
{
    update_interval 1.0 sec

    script_variables
        int counter = 0;
    end_script_variables

    on_update
        counter = counter + 1;
    end_on_update
}
```

## Simulation Control

### RUN_SIMULATION
Controls simulation execution.

```
RUN_SIMULATION
{
    start_time 0.0
    end_time 3600.0
}
```

## Built-in Functions

- `print(...)` - Print to console
- `Time()` - Get current simulation time
- `extern` - Declare external function
