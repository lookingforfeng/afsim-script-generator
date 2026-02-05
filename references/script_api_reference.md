# AFSIM 脚本 API 完整参考

本文档包含 AFSIM 2.9.0 所有可用脚本类的完整 API 参考。

## 目录

1. [核心平台类](#核心平台类)
2. [传感器和武器类](#传感器和武器类)
3. [容器类](#容器类)
4. [几何和数学类](#几何和数学类)
5. [通信和跟踪类](#通信和跟踪类)

---

## 核心平台类

### WsfPlatform

**继承**: WsfObject

**用途**: 代表仿真中的平台对象（飞机、导弹、舰船等）

#### 基本信息方法

```javascript
int Index()                              // 返回平台唯一索引
string Name()                            // 返回平台名称
double CreationTime()                    // 返回创建时的仿真时间（秒）
double TimeSinceCreation()               // 返回自创建以来的时间（秒）
void SetCreationTime(double aTime)       // 设置创建时间
```

#### 阵营和标识

```javascript
void SetSide(string aSide)               // 设置所属方
string Side()                            // 返回所属方
void SetIcon(string aIcon)               // 设置图标
string Icon()                            // 返回图标
```

#### 指挥链方法

```javascript
WsfPlatform Commander()                  // 返回指挥官
void SetCommander(WsfPlatform aPlatform) // 设置指挥官
string CommanderName()                   // 返回指挥官名称
WsfPlatformList Peers()                  // 返回同级平台列表
WsfPlatformList Subordinates()           // 返回下属平台列表
```

#### 子系统访问

```javascript
WsfMover Mover()                         // 返回移动器对象
WsfFuel Fuel()                           // 返回燃料对象

// 通信设备
WsfComm Comm(string aName)               // 返回指定通信设备
int CommCount()                          // 返回通信设备数量
WsfComm CommEntry(int aIndex)            // 返回指定索引的通信设备

// 传感器
WsfSensor Sensor(string aName)           // 返回指定传感器
int SensorCount()                        // 返回传感器数量
WsfSensor SensorEntry(int aIndex)        // 返回指定索引的传感器

// 武器
WsfWeapon Weapon(string aName)           // 返回指定武器
int WeaponCount()                        // 返回武器数量
WsfWeapon WeaponEntry(int aIndex)        // 返回指定索引的武器

// 处理器
WsfProcessor Processor(string aName)     // 返回指定处理器
int ProcessorCount()                     // 返回处理器数量
WsfProcessor ProcessorEntry(int aIndex)  // 返回指定索引的处理器
```

#### 设备控制

```javascript
bool TurnCommOn(string aName)            // 打开通信设备
bool TurnCommOff(string aName)           // 关闭通信设备
bool TurnSensorOn(string aName)          // 打开传感器
bool TurnSensorOff(string aName)         // 关闭传感器
bool TurnProcessorOn(string aName)       // 打开处理器
bool TurnProcessorOff(string aName)      // 关闭处理器
```

#### 物理属性

```javascript
double Length()                          // 返回长度（米）
double Width()                           // 返回宽度（米）
double Height()                          // 返回高度（米）
double TotalMass()                       // 返回总质量
double EmptyMass()                       // 返回空载质量
double FuelMass()                        // 返回燃料质量
double PayloadMass()                     // 返回载荷质量
```

#### 平台控制

```javascript
void Detonate(string aResult)            // 引爆平台
void DeletePlatform()                    // 从仿真中删除平台
bool IsExternallyControlled()            // 返回是否被外部控制
```

#### 静态方法

```javascript
static bool IsA_TypeOf(string aDerivedType, string aBaseType)
// 检查平台类型继承关系

static WsfRoute CreateRoute(string aRouteName)
// 返回指定名称路由的克隆

static bool ExecuteGlobalScript(string aScript)
// 在全局上下文中执行脚本
```

---

### WsfMover

**继承**: WsfPlatformPart

**用途**: 控制平台的运动

#### 基本方法

```javascript
double UpdateInterval()                  // 返回更新间隔
WsfRoute Route()                         // 返回移动器路由的副本
WsfRoute DefaultRoute()                  // 返回默认路由的副本
void SetMode(string aModeString)         // 设置移动器模式
bool SetTSPI_FileName(string aFileName)  // 设置TSPI文件名
bool IsExtrapolating()                   // 返回是否正在外推
void BurnedOut(double aBurnoutTime)      // 触发移动器外推
bool TurnOff()                           // 关闭移动器
bool TurnOn()                            // 打开移动器
```

#### 数据访问

```javascript
Array<int> PropertyInt(string aPropertyName)
// 返回整数属性值

Array<double> PropertyDouble(string aPropertyName)
// 返回双精度属性值

Array<string> PropertyString(string aPropertyName)
// 返回字符串属性值
```

#### 静态方法

```javascript
static WsfMover Create(string aMoverType)
// 创建指定类型的移动器

static bool IsA_TypeOf(string aDerivedType, string aBaseType)
// 检查移动器类型继承关系
```

---

## 传感器和武器类

### WsfSensor

**继承**: WsfArticulatedPart

**用途**: 代表平台上的传感器设备

#### 基本控制

```javascript
bool TurnOff()                           // 关闭传感器
bool TurnOn()                            // 打开传感器
```

#### 模式控制

```javascript
int ModeCount()                          // 返回模式数量
string ModeName(int aModeIndex)          // 返回模式名称
string CurrentMode()                     // 返回当前模式名称
void SelectMode(string aMode)            // 选择模式
void DeselectMode(string aMode)          // 取消选择模式
```

#### 视场 (FOV) 方法

```javascript
WsfFieldOfView FOV()                     // 返回视场对象
double FOV_MinimumAzimuth()              // 返回最小方位角
double FOV_MaximumAzimuth()              // 返回最大方位角
double FOV_MinimumElevation()            // 返回最小仰角
double FOV_MaximumElevation()            // 返回最大仰角
double FOV_MinimumRange()                // 返回最小距离
double FOV_MaximumRange()                // 返回最大距离

void SetFOV(WsfFieldOfView aFOV)         // 设置视场
void SetFOV_Azimuth(double aMin, double aMax)
// 设置方位角视场

void SetFOV_Elevation(double aMin, double aMax)
// 设置仰角视场

void SetFOV_Range(double aMin, double aMax)
// 设置距离限制

bool WithinFieldOfView(WsfGeoPoint aPoint)
// 检查点是否在视场内
```

#### 扫描方法

```javascript
bool CanScanInAzimuth()                  // 返回是否可以在方位角扫描
bool CanScanInElevation()                // 返回是否可以在仰角扫描
double ScanMinimumAzimuth()              // 返回扫描最小方位角
double ScanMaximumAzimuth()              // 返回扫描最大方位角
double ScanMinimumElevation()            // 返回扫描最小仰角
double ScanMaximumElevation()            // 返回扫描最大仰角
```

#### 跟踪方法

```javascript
int ActiveTrackCount()                   // 返回当前跟踪目标数量
int MaximumTrackCount()                  // 返回最大跟踪目标数量
double TrackQuality()                    // 返回跟踪质量
int MaximumRequestCount()                // 返回最大跟踪请求数
int ActiveRequestCount()                 // 返回当前活动跟踪请求数

bool HaveRequestFor(WsfTrackId aTrackId)
// 检查是否有针对指定航迹的跟踪请求

bool StartTracking(WsfTrack aTrack, string aMode)
// 开始跟踪指定航迹

bool StopTracking(WsfTrackId aTrackId)
// 停止跟踪指定航迹
```

#### 波束控制

```javascript
int BeamCount()                          // 返回波束数量
double FrameTime()                       // 返回当前模式的帧时间
```

#### 发射器/接收器

```javascript
WsfEM_Xmtr Xmtr(int aIndex)              // 返回发射器对象
int XmtrCount()                          // 返回发射器数量
WsfEM_Rcvr Rcvr(int aIndex)              // 返回接收器对象
int RcvrCount()                          // 返回接收器数量
```

#### 电子战方法

```javascript
bool JammingPerceived()                  // 返回是否感知到干扰
bool ContinuousJammingPerceived()        // 返回是否感知到连续干扰
bool PulseJammingPerceived()             // 返回是否感知到脉冲干扰

bool IsEP_TechniqueActive(string aTechniqueName)
// 检查EP技术是否激活

bool SelectEP_Technique(string aTechniqueName)
// 选择EP技术

bool DeselectEP_Technique(string aTechniqueName)
// 取消选择EP技术
```

#### 激光代码

```javascript
int LaserCode()                          // 返回激光代码值
void SetLaserCode(int aValue)            // 设置激光代码值
```

---

### WsfWeapon

**继承**: WsfArticulatedPart

**用途**: 代表平台上的武器系统

#### 基本控制

```javascript
bool TurnOff()                           // 关闭武器
bool TurnOn()                            // 打开武器
void CueToTarget(WsfTrack aTrack)        // 将武器指向航迹
```

#### 发射方法

```javascript
bool Fire()                              // 发射武器
bool Fire(WsfTrack aTrack)               // 向指定航迹发射
bool FireAtLocation(WsfGeoPoint aLocation)
// 向指定位置发射

bool FireSalvo(WsfTrack aTrack, int aNumRounds)
// 发射齐射

void AbortSalvo(WsfTrackId aTrackId)     // 中止齐射
void CeaseFire()                         // 停止所有发射请求
```

#### 状态查询

```javascript
int ActiveRequestCount()                 // 返回当前活动的发射请求数
int MaximumRequestCount()                // 返回最大同时发射请求数
double QuantityRemaining()               // 返回剩余武器数量
void SetQuantityRemaining(double aQuantity)
// 设置剩余武器数量

double TotalQuantityUsed()               // 返回已使用的武器总量
double ReloadInventory()                 // 返回重装弹药库存
double TimeLastFired()                   // 返回上次发射的仿真时间
double TimeSinceLastFired()              // 返回自上次发射以来的时间
double FiringInterval()                  // 返回发射间隔时间
bool IsReloading()                       // 返回是否正在重装
```

#### 针对特定目标的状态

```javascript
double TimeSinceWeaponLastFiredFor(WsfTrackId aTrackId)
// 返回针对指定航迹上次发射以来的时间

int WeaponsPendingFor(WsfTrackId aTrackId)
// 返回针对指定航迹待发射的武器数

int WeaponsActiveFor(WsfTrackId aTrackId)
// 返回针对指定航迹当前活动的武器数

int RoundsCompleteFor(WsfTrackId aTrackId)
// 返回针对指定航迹已终止的武器数

int RoundsFiredAt(WsfTrackId aTrackId)
// 返回针对指定航迹已发射的武器数

WsfPlatformList ActiveWeaponPlatformsFor(WsfTrackId aTrackId)
// 返回针对指定航迹当前活动的武器平台列表
```

#### 发射计算机

```javascript
WsfLaunchComputer LaunchComputer()       // 返回发射计算机对象

bool CanIntercept(WsfTrack aTrack)
// 检查是否能拦截目标

double TimeToIntercept(WsfTrack aTrack)
// 返回拦截时间
```

#### 模式控制

```javascript
int ModeCount()                          // 返回模式数量
string ModeName(int aModeIndex)          // 返回模式名称
string CurrentMode()                     // 返回当前模式
void SelectMode(string aModeName)        // 选择模式
```

#### 干扰方法

```javascript
bool CanJam(double aFrequency)           // 检查是否能干扰指定频率
int ActiveBeams()                        // 返回活动波束数
int MaximumBeams()                       // 返回最大波束数
double MinimumFrequency()                // 返回最小频率
double MaximumFrequency()                // 返回最大频率
bool WithinFrequencyBand(double aFrequency)
// 检查频率是否在频带内

bool StartJamming(double aFrequency, double aBandwidth)
// 开始干扰

bool StopJamming(double aFrequency, double aBandwidth)
// 停止干扰
```

---

## 容器类

### Array<T>

**用途**: 动态数组容器，类似 C++ STL vector

**构造**: `Array<T> newObj = Array<T>();`

#### 基本方法

```javascript
int Size()                               // 返回元素数量
bool Empty()                             // 返回是否为空
void Clear()                             // 清空数组
```

#### 元素访问

```javascript
T Get(int aIndex)                        // 返回指定索引的元素（可用 [] 操作符）
void Set(int aIndex, T aData)            // 设置指定索引的元素（可用 [] 操作符）
T Front()                                // 返回第一个元素
T Back()                                 // 返回最后一个元素
```

#### 修改操作

```javascript
void PushBack(T aData)                   // 在末尾添加元素
void PopBack()                           // 删除最后一个元素
void Insert(int aIndex, T aVal)          // 在指定位置插入元素
bool Erase(T aData)                      // 删除指定元素（第一个匹配）
bool EraseAt(int aIndex)                 // 删除指定索引的元素
```

#### 算法操作

```javascript
void Reverse()                           // 反转数组元素
void Sort(bool aAscending)               // 排序数组（升序或降序）
```

#### 迭代器

```javascript
ArrayIterator GetIterator()              // 返回迭代器
```

**使用示例**:
```javascript
Array<int> numbers = Array<int>();
numbers.PushBack(10);
numbers.PushBack(20);
numbers.PushBack(30);
writeln("Size: ", numbers.Size());       // 输出: Size: 3
writeln("First: ", numbers[0]);          // 输出: First: 10
numbers.Sort(true);                      // 升序排序
```

---

### Map<K,V>

**用途**: 键值对容器，类似 C++ STL map

**构造**: `Map<K,V> newObj = Map<K,V>();`

#### 基本方法

```javascript
int Size()                               // 返回元素数量
bool Empty()                             // 返回是否为空
void Clear()                             // 清空映射
```

#### 元素访问和修改

```javascript
V Get(K aKey)                            // 返回指定键的值（可用 [] 操作符）
void Set(K aKey, V aValue)               // 设置指定键的值（可用 [] 操作符）
bool HasKey(K aKey)                      // 检查键是否存在
bool Erase(K aKey)                       // 删除指定键
```

#### 迭代器

```javascript
MapIterator GetIterator()                // 返回迭代器
```

**使用示例**:
```javascript
Map<string, int> scores = Map<string, int>();
scores["Alice"] = 95;
scores["Bob"] = 87;
scores["Charlie"] = 92;

if (scores.HasKey("Alice")) {
    writeln("Alice's score: ", scores["Alice"]);
}
```

---

## 几何和数学类

### WsfGeoPoint

**用途**: 表示地理位置点

#### 方法

```javascript
double Latitude()                        // 返回纬度（弧度）
double Longitude()                       // 返回经度（弧度）
double Altitude()                        // 返回高度（米）
```

---

### Math

**用途**: 数学函数库

#### 常用函数

```javascript
static double Abs(double x)              // 绝对值
static double Sqrt(double x)             // 平方根
static double Sin(double x)              // 正弦（弧度）
static double Cos(double x)              // 余弦（弧度）
static double Tan(double x)              // 正切（弧度）
static double Asin(double x)             // 反正弦
static double Acos(double x)             // 反余弦
static double Atan(double x)             // 反正切
static double Atan2(double y, double x)  // 两参数反正切
static double Pow(double x, double y)    // 幂运算
static double Exp(double x)              // 指数函数
static double Log(double x)              // 自然对数
static double Log10(double x)            // 常用对数
static double Floor(double x)            // 向下取整
static double Ceil(double x)             // 向上取整
static double Round(double x)            // 四舍五入
static double Min(double a, double b)    // 最小值
static double Max(double a, double b)    // 最大值
```

#### 常数

```javascript
static double PI()                       // 圆周率 π
static double E()                        // 自然常数 e
```

---

## 通信和跟踪类

### WsfTrack

**用途**: 表示跟踪目标

#### 方法

```javascript
WsfTrackId Id()                          // 返回航迹ID
string Name()                            // 返回航迹名称
WsfPlatform Platform()                   // 返回关联的平台对象
```

---

### WsfTrackId

**用途**: 航迹唯一标识符

---

## 重要提示

### ⚠️ 不存在的方法（避免使用）

以下方法在之前的错误中被使用，但**实际不存在**：

```javascript
// ❌ 错误 - 这些方法不存在
WsfGeoPoint pos = myUAV.Position();      // Position() 不存在
WsfGeodetic geo = pos.Geodetic();        // Geodetic() 不存在
Time()                                   // Time() 不存在
```

### ✅ 正确的替代方法

```javascript
// ✅ 正确 - 使用简单的 print 语句
on_update
    print("UAV status update");
    print("Current time: ", SIMTIME);    // 使用 SIMTIME 获取当前时间
end_on_update
```

---

## 全局变量和常量

```javascript
PLATFORM                                 // 当前平台对象
PROCESSOR                                // 当前处理器对象
SENSOR                                   // 当前传感器对象
WEAPON                                   // 当前武器对象
SIMTIME                                  // 当前仿真时间（秒）
```

---

## 内置函数

```javascript
print(...)                               // 打印到控制台
writeln(...)                             // 打印并换行
```