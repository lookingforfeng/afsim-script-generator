# AFSIM Scripting Language Grammar

## Basic Types

```
string, int, double, char, bool
```

## Comments

```
// Single line comment
/* Multi-line comment */
# Shell-style comment
```

## Variable Declaration

```
type identifier;
type identifier = value;
[static|extern|global] type identifier = value;
```

Examples:
```
int count = 0;
double speed = 250.5;
string name = "aircraft_1";
bool active = true;
```

## Control Structures

### If Statement
```
if (condition) {
    // statements
} else {
    // statements
}
```

### For Loop
```
for (int i = 0; i < 10; i++) {
    // statements
}
```

### Foreach Loop
```
foreach (type item in collection) {
    // statements
}
```

### While Loop
```
while (condition) {
    // statements
}
```

### Do-While Loop
```
do {
    // statements
} while (condition);
```

## Operators

### Arithmetic
```
+  -  *  /  (unary +, -)
```

### Comparison
```
==  !=  <  >  <=  >=
```

### Logical
```
&&  ||  !  ^
```

### Assignment
```
=  +=  -=  *=  /=
```

### Member Access
```
.   (dot operator)
->  (arrow operator)
```

## Functions

### Function Definition
```
return_type function_name(type param1, type param2) {
    // statements
    return value;
}
```

### Function Call
```
result = function_name(arg1, arg2);
```

## Arrays and Collections

### Initializer List
```
{value1, value2, value3}
{key1: value1, key2: value2}
```

### Array Access
```
array[index]
array[index] = value
```

## Templates

```
Type<TemplateParam>
Map<string, int>
Array<double>
```

## Keywords

```
if, else, for, foreach, in, while, do
break, continue, return
true, false, null, NULL
static, extern, global
```
