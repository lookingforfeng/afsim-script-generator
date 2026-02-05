# AFSIM Script Types and Classes

## Basic Types

- `int` - 32-bit integer
- `double` - Double precision floating point
- `string` - String type
- `char` - Character type
- `bool` - Boolean (true/false)

## Collection Types

### Array<T>
Generic array container.

```
Array<double> myArray = Array<double>();
myArray.PushBack(1.5);
myArray.PushBack(2.5);
double val = myArray[0];
int size = myArray.Size();
```

### Map<K,V>
Generic map/dictionary container.

```
Map<string, int> myMap = Map<string, int>();
myMap["key1"] = 100;
myMap["key2"] = 200;
int val = myMap["key1"];
```

## Core WSF Classes

### WsfPlatform
Represents a simulation platform (aircraft, missile, ground unit, etc.).

Common methods:
- `Name()` - Get platform name
- `Position()` - Get position
- `Velocity()` - Get velocity
- `Heading()` - Get heading

### WsfSensor
Represents a sensor on a platform.

### WsfWeapon
Represents a weapon on a platform.

### WsfMover
Controls platform movement.

## Utility Classes

### Math
Mathematical functions and constants.

### FileIO
File input/output operations.

### Time
Time-related functions.
