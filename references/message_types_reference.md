# AFSIM 消息类型完整参考

## 概述

AFSIM的消息系统用于平台、传感器、处理器之间的通信。所有消息类型都继承自`WsfMessage`基类。

---

## 消息类型层次结构

```
WsfMessage (基类)
├── WsfTrackMessage - 轨迹消息
├── WsfControlMessage - 控制消息
├── WsfStatusMessage - 状态消息
├── WsfImageMessage - 图像消息
├── WsfAssetMessage - 资产消息
├── WsfTaskAssignMessage - 任务分配消息
├── WsfTrackDropMessage - 轨迹丢弃消息
├── WsfBMTrackMessage - 战场管理轨迹消息
└── 其他消息类型...
```

---

## 1. WsfMessage (基类)

所有消息的基类，提供基本的消息属性和辅助数据功能。

### 构造方法
```javascript
WsfMessage newObj = WsfMessage();
WsfMessage newObj = WsfMessage(other);  // Clone
```

### 核心方法

#### 消息属性
```javascript
string Originator()                      // 返回消息发起平台名称
string Type()                            // 返回消息类型
string SubType()                         // 返回消息子类型
void SetType(string aType)               // 设置消息类型
void SetSubType(string aSubType)         // 设置消息子类型
```

#### 消息大小和优先级
```javascript
int SizeInBits()                         // 返回消息大小（位）
void SetSizeInBits(int aSizeInBits)      // 设置消息大小（位）
int SizeInBytes()                        // 返回消息大小（字节）
void SetSizeInBytes(int aSizeInBytes)    // 设置消息大小（字节）
int Priority()                           // 返回消息优先级（值越高优先级越高）
void SetPriority(int aPriority)          // 设置消息优先级
```

#### 消息标识
```javascript
int SerialNumber()                       // 返回消息序列号
double DataTag()                         // 返回数据标签（唯一标识对象的时间戳）
void CreateDataTag()                     // 创建数据标签
void SetDataTag(double aDataTag)         // 设置数据标签
```

#### 地址信息
```javascript
WsfAddress Destination()                 // 返回消息目的地址
WsfAddress NextHop()                     // 返回消息下一跳地址
```

### 辅助数据方法

辅助数据是可选的用户自定义属性集合，框架维护但不使用这些数据。

#### 读取辅助数据
```javascript
bool AuxDataBool(string aName)           // 获取布尔类型辅助数据
int AuxDataInt(string aName)             // 获取整数类型辅助数据
double AuxDataDouble(string aName)       // 获取双精度类型辅助数据
string AuxDataString(string aName)       // 获取字符串类型辅助数据
Object AuxDataObject(string aName)       // 获取对象类型辅助数据
```

#### 检查辅助数据
```javascript
bool AuxDataExists(string aName)         // 检查辅助数据是否存在
bool CheckAuxData(string aName)          // 检查辅助数据是否存在
bool HasAuxData()                        // 检查对象是否有辅助数据
```

#### 修改辅助数据
```javascript
bool DeleteAuxData(string aName)         // 删除指定辅助数据
void SetAuxData(string aName, bool aValue)      // 设置布尔类型
void SetAuxData(string aName, int aValue)       // 设置整数类型
void SetAuxData(string aName, double aValue)    // 设置双精度类型
void SetAuxData(string aName, string aValue)    // 设置字符串类型
void SetAuxData(string aName, Object aValue)    // 设置对象类型
Map<string, string> GetAllAuxDataTypes() // 返回所有辅助数据的名称和类型
```

---

## 2. WsfTrackMessage (轨迹消息)

用于在系统对象之间传递轨迹信息，通常由传感器和轨迹处理器产生。

### 构造方法
```javascript
WsfTrackMessage newObj = WsfTrackMessage();
WsfTrackMessage newObj = WsfTrackMessage(other);  // Clone
```

### 方法
```javascript
WsfTrack Track()                         // 返回消息中包含的轨迹
void SetTrack(WsfTrack aTrack)           // 设置轨迹
```

### 使用示例
```javascript
on_message
   type WSF_TRACK_MESSAGE
      script
         WsfTrackMessage trackMsg = (WsfTrackMessage)MESSAGE;
         WsfTrack track = trackMsg.Track();
         WsfTrackId trackId = track.TrackId();

         writeln("Received track from ", trackId.OwningPlatform());
         writeln("Track number: ", trackId.TrackNumber());

         if (track.LocationValid())
         {
            writeln("Location: ", track.Latitude(), ", ", track.Longitude());
         }
      end_script
end_on_message
```

---

## 3. WsfControlMessage (控制消息)

用于发送控制命令和请求。

### 构造方法
```javascript
WsfControlMessage newObj = WsfControlMessage();
WsfControlMessage newObj = WsfControlMessage(other);  // Clone
```

### 方法
```javascript
string Function()                        // 返回命令功能
void SetFunction(string aFunction)       // 设置消息功能（等同于设置消息子类型）
WsfTrackId RequestId()                   // 返回当前请求的轨迹ID
void SetRequestId(WsfTrackId aTrackId)   // 设置请求的轨迹ID
string Resource()                        // 返回与命令关联的资源名称
void SetResource(string aResource)       // 设置与消息关联的资源
WsfTrack Track()                         // 返回与命令关联的轨迹
void SetTrack(WsfTrack aTrack)           // 设置与消息关联的轨迹
WsfRoute Route()                         // 返回与命令关联的路由
void SetRoute(WsfRoute aRoute)           // 设置与消息关联的路由
void SetRoute(string aRouteName)         // 通过名称设置路由
```

### 使用示例
```javascript
// 创建控制消息
WsfControlMessage ctrlMsg = WsfControlMessage();

// 设置功能和资源
ctrlMsg.SetFunction("ENGAGE");
ctrlMsg.SetResource("radar-1");

// 设置关联轨迹
WsfTrack targetTrack = GetTargetTrack();
ctrlMsg.SetTrack(targetTrack);

// 设置优先级
ctrlMsg.SetPriority(10);

// 发送消息
SendMessage(ctrlMsg);
```

---

## 4. WsfStatusMessage (状态消息)

用于报告系统或平台的状态。

### 构造方法
```javascript
WsfStatusMessage newObj = WsfStatusMessage();
WsfStatusMessage newObj = WsfStatusMessage(other);  // Clone
```

### 方法
```javascript
string Status()                          // 返回状态
void SetStatus(string aStatus)           // 设置状态
WsfTrackId RequestId()                   // 返回状态适用的轨迹ID
void SetRequestId(WsfTrackId aRequestId) // 设置状态适用的轨迹ID
string SystemName()                      // 返回状态适用的系统名称
void SetSystemName(string aSystemName)   // 设置状态适用的系统名称
WsfPlatform Platform()                   // 返回状态适用的平台
void SetPlatform(WsfPlatform aPlatform)  // 设置状态适用的平台
```

---

## 5. WsfImageMessage (图像消息)

成像传感器的产品，包含图像数据。

### 构造方法
```javascript
WsfImageMessage newObj = WsfImageMessage(other);  // Clone only
```

### 方法
```javascript
WsfImage Image()                         // 返回消息中包含的图像
```

---

## 6. WsfTaskAssignMessage (任务分配消息)

由WsfTaskManager::AssignTask方法发送，用于任务分配。

### 方法
```javascript
WsfPlatform Assigner()                   // 返回分配任务的平台
string AssignerName()                    // 返回分配任务的平台名称
WsfTrack Track()                         // 返回与任务关联的轨迹
string TaskType()                        // 返回任务类型
string ResourceName()                    // 返回任务中指定使用的资源名称
```

---

## 7. WsfTrackDropMessage (轨迹丢弃消息)

传感器在丢弃轨迹时发送给其链接的处理器。

### 构造方法
```javascript
WsfTrackDropMessage newObj = WsfTrackDropMessage();
WsfTrackDropMessage newObj = WsfTrackDropMessage(other);  // Clone
```

### 方法
```javascript
double Time()                            // 返回轨迹被丢弃的仿真时间（秒）
WsfTrackId TrackId()                     // 返回被丢弃轨迹的ID
int TargetIndex()                        // 返回被丢弃轨迹的真实目标索引
```

---

## 8. WsfBMTrackMessage (战场管理轨迹消息)

战场管理器内部轨迹对象的脚本接口，功能最丰富的轨迹消息类型。

### 构造方法
```javascript
WsfBMTrackMessage newObj = WsfBMTrackMessage();
WsfBMTrackMessage newObj = WsfBMTrackMessage(other);  // Clone
```

### 时间和更新方法
```javascript
void SetDataTime(double time)            // 设置消息数据对应的时间
double GetDataTime()                     // 获取消息数据对应的时间
void SetUpdateInterval(double interval)  // 设置轨迹更新间隔（秒）
double GetUpdateInterval()               // 获取轨迹更新间隔
```

### 轨迹标识方法
```javascript
void SetTrackID(int platform_idx, int tan)  // 设置轨迹标识
int GetTrackingSystemID()                // 获取报告平台索引
int GetTrackingSystemTrackID()           // 获取轨迹编号
```

### 位置和速度方法
```javascript
void SetLLA(double lat, double lon, double alt)  // 设置位置（弧度，弧度，米）
double GetLat()                          // 获取纬度（弧度）
double GetLon()                          // 获取经度（弧度）
double GetAlt()                          // 获取高度（米）
void SetECEFVel(double Vx, double Vy, double Vz)  // 设置ECEF速度（米/秒）
double GetVx()                           // 获取ECEF-X速度分量（米/秒）
double GetVy()                           // 获取ECEF-Y速度分量（米/秒）
double GetVz()                           // 获取ECEF-Z速度分量（米/秒）
```

### 协方差和方向方法
```javascript
void SetCovarianceMatrix(WsfCovariance cov)  // 设置协方差矩阵
WsfCovariance GetCovarianceMatrix()      // 获取协方差矩阵
void SetHeadingDegs(double heading)      // 设置航向（相对真北，度）
void SetOrientationDegs(double psi, double theta, double phi)  // 设置欧拉角
double GetOrientationPsiDegs()           // 获取Psi角度
double GetOrientationThetaDegs()         // 获取Theta角度
double GetOrientationPhiDegs()           // 获取Phi角度
```

### 类型和状态方法
```javascript
void SetType(string type, string subtype)  // 设置轨迹类型和子类型
string GetType()                         // 获取类型
string GetSubType()                      // 获取子类型
```

### 跟踪状态方法
```javascript
void SetTrackingStatusNormal()           // 设置跟踪状态为正常
void SetTrackingStatusCoasting()         // 设置跟踪状态为滑行（错过更新）
void SetTrackingStatusTimedOut()         // 设置跟踪状态为超时
void SetTrackingStatusDropping()         // 设置跟踪状态为正在丢弃
void SetTrackingStatusDropped()          // 设置跟踪状态为已丢弃
bool IsTrackingStatusNormal()            // 检查是否为正常状态
bool IsTrackingStatusCoasting()          // 检查是否为滑行状态
bool IsTrackingStatusTimedOut()          // 检查是否为超时状态
bool IsTrackingStatusDropping()          // 检查是否为正在丢弃状态
bool IsTrackingStatusDropped()           // 检查是否为已丢弃状态
```

### IFF（敌我识别）方法
```javascript
void SetIFFUnknown()                     // 设置IFF状态为未知
void SetIFFFriendly()                    // 设置IFF状态为友方
void SetIFFHostile()                     // 设置IFF状态为敌方
void SetIFFNeutral()                     // 设置IFF状态为中立
bool IsIFFUnknown()                      // 检查IFF是否为未知
bool IsIFFFriendly()                     // 检查IFF是否为友方
bool IsIFFHostile()                      // 检查IFF是否为敌方
bool IsIFFNeutral()                      // 检查IFF是否为中立
```

### 其他属性方法
```javascript
void SetManeuveringFlag(bool is_maneuvering)  // 设置机动标志
bool GetManeuveringFlag()                // 获取机动标志
void SetQuantity(int quantity)           // 设置轨迹强度
int GetQuantity()                        // 获取轨迹强度
void SetJamming(bool is_jamming)         // 设置干扰标志
bool GetJamming()                        // 获取干扰标志
void SetJammingPower(double power_dB)    // 设置干扰功率（dB）
double GetJammingPower()                 // 获取干扰功率（dB）
```

### 真实目标信息方法
```javascript
void SetTargetTruthName(string name)     // 设置目标真实名称（用于日志）
string GetTargetTruthName()              // 获取目标真实名称
void SetTargetTruthID(int id)            // 设置目标真实平台索引
int GetTargetTruthID()                   // 获取目标真实平台索引
```

---

## 消息处理模式

### Pattern 1: 基本消息处理
```javascript
processor message-handler WSF_SCRIPT_PROCESSOR
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
            string function = msg.Function();
            // 处理控制消息
         end_script

      type default
         script
            writeln("Unknown message type: ", MESSAGE.Type());
         end_script
   end_on_message
end_processor
```

### Pattern 2: 使用辅助数据
```javascript
// 发送方
WsfTrackMessage msg = WsfTrackMessage();
msg.SetTrack(track);
msg.SetAuxData("mission_id", 12345);
msg.SetAuxData("priority", "HIGH");
msg.SetAuxData("is_critical", true);
SendMessage(msg);

// 接收方
on_message
   type WSF_TRACK_MESSAGE
      script
         WsfTrackMessage msg = (WsfTrackMessage)MESSAGE;

         if (msg.HasAuxData())
         {
            int missionId = msg.AuxDataInt("mission_id");
            string priority = msg.AuxDataString("priority");
            bool critical = msg.AuxDataBool("is_critical");

            writeln("Mission ID: ", missionId);
            writeln("Priority: ", priority);
            writeln("Critical: ", critical);
         }
      end_script
end_on_message
```

### Pattern 3: 消息优先级和大小
```javascript
WsfControlMessage msg = WsfControlMessage();
msg.SetFunction("ENGAGE");
msg.SetPriority(10);              // 高优先级
msg.SetSizeInBytes(1024);         // 设置消息大小
SendMessage(msg);
```

---

## 常用消息类型总结

| 消息类型 | 用途 | 主要方法 |
|---------|------|---------|
| **WsfTrackMessage** | 传递轨迹信息 | Track(), SetTrack() |
| **WsfControlMessage** | 发送控制命令 | SetFunction(), SetResource(), SetTrack() |
| **WsfStatusMessage** | 报告状态 | SetStatus(), SetSystemName() |
| **WsfTaskAssignMessage** | 任务分配 | Assigner(), TaskType(), ResourceName() |
| **WsfTrackDropMessage** | 轨迹丢弃通知 | TrackId(), Time() |
| **WsfBMTrackMessage** | 战场管理轨迹 | SetLLA(), SetIFF(), SetTrackingStatus() |

---

## 最佳实践

1. **消息类型选择**
   - 使用最具体的消息类型（如WsfTrackMessage而不是WsfMessage）
   - 根据用途选择合适的消息类型

2. **辅助数据使用**
   - 用于传递自定义属性
   - 检查HasAuxData()避免访问不存在的数据
   - 使用有意义的键名

3. **消息优先级**
   - 关键消息使用高优先级
   - 默认优先级通常足够

4. **消息大小**
   - 对于通信建模，设置合理的消息大小
   - 影响通信延迟和带宽计算

5. **错误处理**
   - 始终包含default消息类型处理
   - 检查消息内容的有效性

---

## 参考

- 完整API: `script_api_reference.md`
- 使用示例: `examples.md`
- 命令参考: `commands_reference.md`
