# AFSIM Script Generator - Claude Code Skill

# AFSIM 脚本生成器 - Claude Code 技能

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![AFSIM Version](https://img.shields.io/badge/AFSIM-2.9.0-green.svg)](https://github.com/lookingforfeng/afsim-script-generator)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-purple.svg)](SKILL.md)

> **Claude Code Skill for AFSIM | 专为 Claude Code 设计的 AFSIM 仿真技能**

**AFSIM Script Generator** 是一个专业的 **Claude Code Skill**，用于生成和执行 **AFSIM**（Advanced Framework for Simulation, Integration and Modeling）**仿真脚本**。本项目提供完整的 **AFSIM 2.9.0** 脚本语言支持，涵盖**无人机仿真**、**平台建模**、**传感器配置**、**武器系统**、**协同作战**等场景。

---

## 📋 项目简介 | Project Overview

**AFSIM** 是美国空军研究实验室开发的**高级仿真框架**，广泛应用于军事仿真、无人机集群、传感器建模、武器系统和任务规划。本 Skill 为 Claude Code 提供：

- ✅ **AFSIM 2.9.0** 完整脚本语言支持
- ✅ **WSF (World Simulation Framework)** 语法和 API
- ✅ **158个 API 方法**的完整文档
- ✅ **22+种平台类型** (mover types) 参考
- ✅ **智能脚本生成**和**语法验证**
- ✅ **一键仿真执行**和**结果分析**

## ✨ 功能特性 | Features

### 核心能力

- 🎯 **智能脚本生成**：基于 Claude AI 自动生成语法正确的 AFSIM/WSF 场景脚本，支持空对空、空对地、ISR等多种仿真场景
- 🚀 **一键脚本执行**：通过 mission.exe 直接运行 AFSIM 仿真，支持事件步进、实时帧步进等多种执行模式
- 🔍 **智能语法验证**：自动检测并修复 AFSIM 脚本语法错误，避免常见的单位缺失、代码块未闭合等问题
- 📚 **完整文档库**：包含 AFSIM 2.9.0 完整语言语法、158个API方法、22+种mover类型、命令参考和工作示例
- 🛠️ **Python 工具集**：提供便捷的脚本执行包装器，支持配置管理和路径自动推导

### 仿真场景支持

- ✈️ **空战仿真**：空对空作战、BVR交战、近距格斗
- 🎯 **对地打击**：空对地攻击、精确制导、目标打击
- 🛰️ **ISR任务**：情报监视侦察、目标搜索、态势感知
- 🚁 **无人机集群**：UAV编队协同、分布式任务规划、集群智能
- 🎮 **多域作战**：空天地海多域协同、联合作战仿真

### 技术特性

- 🔧 **WSF脚本语言**：完整支持 World Simulation Framework 脚本语法
- 📡 **传感器建模**：雷达、ESM、EOIR等多种传感器类型
- 💣 **武器系统**：空空导弹、空地导弹、炸弹、火炮等武器建模
- 🤖 **行为树**：支持复杂的AI决策和任务规划
- 📊 **数据输出**：事件日志、二进制报告、回放文件生成

## 🚀 快速开始 | Quick Start

### 前置要求 | Prerequisites

- **AFSIM 2.9.0** - Advanced Framework for Simulation, Integration and Modeling
  - 可安装在任意位置（通过配置文件指定）
  - 需要有效的 AFSIM 许可证
- **Python 3.x** - 用于运行脚本执行包装器
- **Claude Code** - Anthropic 的 AI 编程助手（可选，用于智能脚本生成）

### 安装和配置 | Installation & Configuration

#### 步骤 1：获取 Skill

**方式 1：从 GitHub 克隆**

```bash
git clone https://github.com/lookingforfeng/afsim-script-generator.git
cd afsim-script-generator
```

**方式 2：直接下载**

- 下载 ZIP 文件并解压到本地目录
- 或复制整个 skill 目录到 `~/.claude/skills/` 目录

#### 步骤 2：配置 AFSIM 安装路径

编辑 `config.txt` 文件，设置你的 **AFSIM 安装目录**：

```ini
# AFSIM 安装目录配置
# 修改下面的路径为你的 AFSIM 2.9.0 安装位置
AFSIM_INSTALL_DIR=D:\Program Files\afsim2.9.0
```

**配置说明：**

- ✅ 只需修改 `AFSIM_INSTALL_DIR` 这一行
- ✅ `mission.exe` 路径会自动推导为：`{AFSIM_INSTALL_DIR}/bin/mission.exe`
- ✅ 文档路径会自动推导为：`{AFSIM_INSTALL_DIR}/documentation/html/docs`
- ✅ 在不同电脑上使用时，只需更新这个配置即可
- ✅ 支持 Windows、Linux、macOS 路径格式

#### 步骤 3：验证配置

运行以下命令验证配置是否正确：

```bash
python scripts/run_mission.py --help
```

如果配置正确，会显示：

- ✅ 帮助信息
- ✅ 当前 AFSIM 安装目录
- ✅ mission.exe 路径
- ✅ 文档目录路径

#### 步骤 4：在 Claude Code 中使用

在 **Claude Code** 中，直接描述您的 AFSIM 仿真需求，例如：

```
"帮我创建一个空对空作战的 AFSIM 脚本"
```

Claude Code 会自动加载本 Skill 并生成相应的脚本。

### 基本使用

1. **生成脚本**：使用 AFSIM 脚本语言创建场景脚本
2. **执行脚本**：使用提供的 Python 包装器运行

```bash
python scripts/run_mission.py <脚本文件.txt> [选项]
```

**可用选项：**

- `-es` - 事件步进模式（默认）
- `-rt` - 实时帧步进模式
- `-fs` - 非实时帧步进模式
- `-fio` - 刷新输出
- `-sm` - 抑制消息

## ⚠️ 关键规则（生成脚本前必读）

**必须遵守以下规则，否则脚本会失败：**

1. **文件扩展名必须是 `.txt`** - 不是 `.wsf`！
2. **所有数值参数必须带单位** - 例如：`100 m/sec`、`30.0 sec`、`1000 m`
3. **所有代码块必须有结束标记** - `end_mover`、`end_platform_type`、`end_processor` 等
4. **不要使用不存在的脚本方法** - 避免 `Position()`、`Geodetic()`、`Time()` 等
5. **路由中不要使用 `loop` 命令** - 会导致语法错误

**详细错误说明和最佳实践：** 见 `references/common_mistakes.md`

## 📖 使用指南 | Usage Guide

### 1. 收集仿真需求

在生成 **AFSIM 脚本**前，需要明确以下仿真要素：

#### 场景类型

- **空对空作战** (Air-to-Air Combat)：BVR交战、近距格斗、多机协同
- **空对地打击** (Air-to-Ground Strike)：精确打击、区域轰炸、SEAD任务
- **ISR任务** (Intelligence, Surveillance, Reconnaissance)：侦察、监视、目标搜索
- **无人机集群** (UAV Swarm)：编队飞行、协同作战、分布式任务
- **多域作战** (Multi-Domain Operations)：空天地海联合仿真

#### 平台配置

- **有人机平台**：战斗机、轰炸机、运输机、预警机
- **无人机平台**：侦察无人机、攻击无人机、蜂群无人机
- **导弹平台**：空空导弹、空地导弹、巡航导弹
- **地面单位**：SAM系统、雷达站、指挥中心
- **卫星平台**：通信卫星、侦察卫星

#### 传感器和武器

- **传感器类型**：雷达 (Radar)、ESM、EOIR、声纳
- **武器系统**：导弹、炸弹、火炮、电子战设备

#### 任务时间线

- 仿真开始时间和持续时间
- 关键事件触发条件
- 平台航路和机动

#### 输出要求

- 事件日志 (Event Log)
- 轨迹数据 (Track Data)
- 传感器探测记录
- 武器交战结果

### 2. 生成 AFSIM 脚本

使用 **AFSIM 脚本语言** (WSF Scripting Language) 创建仿真场景。本 **Skill** 提供完整的语法支持和 API 参考。

#### 基本脚本结构

```
// AFSIM/WSF 脚本使用 // 或 /* */ 注释
// 文件扩展名必须是 .txt

// 1. 平台定义 (Platform Definition)
PLATFORM my_aircraft
{
    TYPE air_vehicle           // 平台类型
    POSITION 0.0 0.0 10000.0  // 初始位置 (m)
    VELOCITY 250.0 0.0 0.0    // 初始速度 (m/s)
}

// 2. 传感器定义 (Sensor Definition)
SENSOR my_radar
{
    TYPE radar                 // 传感器类型
    PARENT my_aircraft        // 父平台
    RANGE 100000.0            // 探测距离 (m)
}

// 3. 武器定义 (Weapon Definition)
WEAPON my_missile
{
    TYPE air_to_air_missile   // 武器类型
    PARENT my_aircraft        // 父平台
    QUANTITY 4                // 数量
}

// 4. 仿真控制 (Simulation Control)
RUN_SIMULATION
{
    DURATION 300.0 sec        // 仿真时长
    // 运行时命令和事件
}
```

#### 关键语法规则

1. **文件扩展名**：必须使用 `.txt`，不是 `.wsf`
2. **单位要求**：所有数值必须带单位 (如 `100 m/sec`, `30.0 sec`, `1000 m`)
3. **代码块闭合**：所有代码块必须有结束标记 (`end_mover`, `end_platform_type` 等)
4. **脚本方法**：避免使用不存在的方法 (如 `Position()`, `Geodetic()`, `Time()`)
5. **路由命令**：不要在路由中使用 `loop` 命令

#### 完整语法参考

- **references/common_mistakes.md** - **首先阅读** - 10条关键规则和常见错误
- **references/file_structure.md** - 标准 AFSIM 脚本文件结构和模板
- **references/mover_reference.md** - 22+种 mover 类型完整参考（含所有参数）
- **references/script_api_reference.md** - WsfPlatform/Sensor/Weapon/Track 完整 API（158个方法）
- **references/commands_reference.md** - 完整命令语法参考
- **references/message_types_reference.md** - WsfMessage 消息系统（8种核心消息类型）
- **references/sensor_types_reference.md** - 特殊传感器类型（Radar/ESM/EOIR）
- **references/examples.md** - 4个完整工作示例 + 5种常用模式

### 3. 执行 AFSIM 仿真

使用提供的 Python 包装器通过 **mission.exe** 运行仿真：

```bash
python scripts/run_mission.py scenario.txt -es
```

#### 执行模式选项

- **`-es`** - 事件步进模式 (Event Stepping) - **推荐用于调试**
  
  - 按事件驱动仿真
  - 适合分析事件序列

- **`-rt`** - 实时帧步进模式 (Real-Time Frame Stepping)
  
  - 实时速率执行
  - 适合可视化和演示

- **`-fs`** - 非实时帧步进模式 (Fast Frame Stepping)
  
  - 最快速度执行
  - 适合批量仿真

- **`-fio`** - 刷新输出 (Flush I/O)
  
  - 立即输出日志
  - 适合实时监控

- **`-sm`** - 抑制消息 (Suppress Messages)
  
  - 减少控制台输出
  - 适合批处理

#### 仿真输出

AFSIM 仿真会生成以下输出文件：

- **事件日志** (.log) - 仿真事件序列
- **二进制报告** (.bin) - 详细仿真数据
- **回放文件** (.replay) - 可视化回放数据
- **轨迹数据** - 平台运动轨迹
- **传感器记录** - 探测和跟踪数据
- **武器交战记录** - 发射和命中数据

### 4. 验证和迭代仿真结果

#### 检查仿真执行

- 查看 **mission.exe** 控制台输出，检查语法错误和警告
- 验证仿真是否按预期完成
- 检查事件日志中的关键事件

#### 分析仿真结果

- **轨迹分析**：验证平台运动是否符合预期
- **传感器性能**：检查探测距离、跟踪精度
- **武器效能**：分析命中率、杀伤效果
- **任务完成度**：评估任务目标达成情况

#### 脚本优化

根据仿真结果调整脚本参数：

- 调整平台性能参数（速度、机动性）
- 优化传感器配置（探测距离、视场角）
- 修改武器参数（射程、命中率）
- 改进任务规划（航路、时序）

#### 常见问题排查

- **语法错误**：参考 `references/common_mistakes.md`
- **执行错误**：检查 mission.exe 路径和配置
- **性能问题**：优化仿真步长和输出频率
- **结果异常**：验证物理模型和参数设置

## 📝 常见脚本模式 | Common Script Patterns

### 平台定义 (Platform Definition)

创建一个基本的**空中平台** (Air Vehicle)，用于**战斗机仿真**或**无人机仿真**：

```
PLATFORM aircraft_1
{
    TYPE air_vehicle              // 平台类型：空中载具
    POSITION 0.0 0.0 10000.0     // 初始位置 (x, y, z) 单位：米
    VELOCITY 250.0 0.0 0.0       // 初始速度 (vx, vy, vz) 单位：m/s
    // 适用于：战斗机、轰炸机、无人机等空中平台
}
```

### 传感器定义 (Sensor Definition)

为平台添加**雷达传感器** (Radar Sensor)，用于**目标探测**和**态势感知**：

```
SENSOR radar_1
{
    TYPE radar                    // 传感器类型：雷达
    PARENT aircraft_1            // 父平台：挂载在 aircraft_1 上
    RANGE 100000.0               // 探测距离：100km
    // 适用于：空对空雷达、地面搜索雷达、火控雷达
}
```

### 武器定义 (Weapon Definition)

为平台配置**空空导弹** (Air-to-Air Missile)，用于**空战仿真**：

```
WEAPON missile_1
{
    TYPE air_to_air_missile      // 武器类型：空空导弹
    PARENT aircraft_1            // 父平台：挂载在 aircraft_1 上
    QUANTITY 4                   // 携带数量：4枚
    // 适用于：AIM-120、AIM-9、霹雳系列等空空导弹
}
```

### 无人机集群 (UAV Swarm)

创建**无人机编队**，用于**集群协同仿真**：

```
// 创建多个无人机平台
PLATFORM uav_1
{
    TYPE air_vehicle
    POSITION 0.0 0.0 5000.0
    VELOCITY 50.0 0.0 0.0        // 无人机巡航速度
}

PLATFORM uav_2
{
    TYPE air_vehicle
    POSITION 100.0 0.0 5000.0    // 编队间距
    VELOCITY 50.0 0.0 0.0
}

// 为每个无人机配置传感器
SENSOR uav_sensor_1
{
    TYPE eoir                     // 光电传感器
    PARENT uav_1
}
```

### 任务规划 (Mission Planning)

定义**ISR任务**的仿真控制流程：

```
RUN_SIMULATION
{
    DURATION 3600.0 sec          // 仿真时长：1小时

    // 任务阶段1：起飞和爬升
    AT_TIME 0.0 sec
    {
        // 初始化命令
    }

    // 任务阶段2：巡航和搜索
    AT_TIME 300.0 sec
    {
        // 搜索区域命令
    }

    // 任务阶段3：返航
    AT_TIME 3000.0 sec
    {
        // 返航命令
    }
}
```

### 更多示例

完整的工作示例和高级模式，请参考：

- **references/examples.md** - 4个完整 AFSIM 脚本示例
- **references/mover_reference.md** - 22+种平台类型参考
- **references/commands_reference.md** - 完整命令语法

## 📂 项目结构 | Project Structure

```
afsim-script-generator/                    # AFSIM 脚本生成器 Claude Code Skill
├── README.md                              # 项目说明文档（中英文）
├── SKILL.md                               # Claude Code Skill 描述文件（带导航索引）
├── CONFIG_README.md                       # 配置文件详细说明
├── config.txt                             # AFSIM 安装目录配置文件
├── LICENSE                                # MIT 开源许可证
│
├── assets/                                # 资源文件目录
│   ├── template.wsf                       # AFSIM 脚本模板
│   ├── wechat_contact.jpg                 # 微信联系方式二维码
│   └── wechat_reward.jpg                  # 微信赞赏码
│
├── references/                            # 参考文档目录（完整系统化）
│   ├── common_mistakes.md                 # ⭐ 10条关键规则和常见错误（必读）
│   ├── file_structure.md                  # 标准 AFSIM 脚本文件结构
│   ├── mover_reference.md                 # 22+种 mover 类型完整参考
│   ├── script_api_reference.md            # WsfPlatform/Sensor/Weapon 完整 API（158个方法）
│   ├── commands_reference.md              # 完整命令语法参考
│   ├── message_types_reference.md         # WsfMessage 消息系统（8种核心消息类型）
│   ├── sensor_types_reference.md          # 特殊传感器类型（Radar/ESM/EOIR）
│   ├── examples.md                        # 4个完整工作示例 + 5种常用模式
│   ├── language_grammar.md                # 完整脚本语言语法
│   ├── script_types.md                    # 数据类型和类方法
│   └── commands.md                        # 命令参考（按类别组织）
│
└── scripts/                               # 工具脚本目录
    └── run_mission.py                     # mission.exe 执行包装器（支持配置管理）
```

### 文档说明

#### 核心文档

- **README.md** - 项目主文档，包含安装、配置、使用指南
- **SKILL.md** - Claude Code Skill 定义，包含快速参考和导航索引
- **CONFIG_README.md** - 配置系统详细说明

#### 参考文档（references/）

- **11个系统化参考文档**，涵盖 AFSIM 脚本语言的所有方面
- 从基础语法到高级 API，从常见错误到完整示例
- 支持快速查找和深度学习

#### 工具脚本（scripts/）

- **run_mission.py** - Python 包装器，简化 mission.exe 调用
- 支持配置文件管理、路径自动推导、多种执行模式

## 🔧 故障排除 | Troubleshooting

### AFSIM 脚本语法错误

**常见问题：**

- ❌ 文件扩展名错误（使用了 `.wsf` 而不是 `.txt`）
- ❌ 数值缺少单位（如 `100` 而不是 `100 m/sec`）
- ❌ 代码块未闭合（缺少 `end_mover`、`end_platform_type` 等）
- ❌ 使用了不存在的脚本方法（如 `Position()`、`Geodetic()`）
- ❌ 路由中使用了 `loop` 命令

**解决方案：**

- 📖 查看 `references/common_mistakes.md` - 10条关键规则
- 📖 参考 `references/language_grammar.md` - 完整语法规则
- 📖 检查 `references/commands_reference.md` - 命令语法
- 📖 查看 `references/examples.md` - 工作示例

### mission.exe 执行错误

**常见问题：**

- ❌ mission.exe 路径不正确
- ❌ AFSIM 安装目录配置错误
- ❌ 文件权限不足
- ❌ 缺少必需的 AFSIM 组件

**解决方案：**

- ✅ 检查 `config.txt` 中的 `AFSIM_INSTALL_DIR` 配置
- ✅ 验证 mission.exe 是否存在：`{AFSIM_INSTALL_DIR}/bin/mission.exe`
- ✅ 确保有执行权限（Windows: 右键→属性→安全）
- ✅ 运行 `python scripts/run_mission.py --help` 验证配置

### 仿真输出问题

**常见问题：**

- ❌ 没有生成输出文件
- ❌ 输出目录不存在
- ❌ 日志文件为空
- ❌ 仿真结果异常

**解决方案：**

- ✅ 检查仿真日志文件（.log）
- ✅ 验证输出目录存在且有写权限
- ✅ 查看 mission.exe 控制台输出
- ✅ 使用 `-fio` 选项刷新输出
- ✅ 检查仿真时长和事件设置

### Claude Code Skill 未激活

**常见问题：**

- ❌ Skill 未正确安装
- ❌ SKILL.md 文件缺失或损坏
- ❌ Claude Code 未识别 AFSIM 关键词

**解决方案：**

- ✅ 确保 skill 目录在 `~/.claude/skills/` 下
- ✅ 验证 SKILL.md 文件存在且完整
- ✅ 在提示词中明确提到 "AFSIM"、"WSF"、"仿真脚本" 等关键词
- ✅ 重启 Claude Code

### 性能和优化问题

**常见问题：**

- ❌ 仿真运行缓慢
- ❌ 内存占用过高
- ❌ 输出文件过大

**解决方案：**

- ✅ 使用 `-fs` 模式（非实时帧步进）加快仿真
- ✅ 减少输出频率和详细程度
- ✅ 优化仿真步长设置
- ✅ 使用 `-sm` 选项抑制不必要的消息

## 📚 参考文档

详细文档位于 `references/` 目录（已系统化完善）：

### 核心参考文档（新增/更新）

- **references/common_mistakes.md** - **从这里开始** - 10条关键规则，避免常见错误
- **references/file_structure.md** - **新增** - 标准AFSIM脚本文件结构和模板
- **references/mover_reference.md** - **新增** - 22+种mover类型完整参考（含所有参数）
- **references/script_api_reference.md** - **新增** - WsfPlatform/Sensor/Weapon/Track完整API（158个方法）
- **references/commands_reference.md** - **新增** - 完整命令语法参考（platform/route/sensor/weapon/processor）
- **references/message_types_reference.md** - **新增** - WsfMessage消息系统完整参考（8种核心消息类型）
- **references/sensor_types_reference.md** - **新增** - 特殊传感器类型参数（Radar/ESM/EOIR）
- **references/examples.md** - **重写** - 4个完整工作示例+5种常用模式

### 保留的参考文档

- **references/language_grammar.md** - 完整的脚本语言语法和语法规则
- **references/script_types.md** - 所有可用的数据类型、类及其方法
- **references/commands.md** - 按类别组织的综合命令参考

## 💡 注意事项

- **AFSIM 脚本使用 `.txt` 扩展名** - 不是 `.wsf`！
- **所有数值参数都需要单位** - 例如：`100 m/sec`、`30.0 sec`
- 脚本是基于文本的，人类可读
- **配置文件** - `config.txt` 中设置AFSIM安装目录
- **mission.exe 位置** - 从配置文件自动推导：`{AFSIM_INSTALL_DIR}/bin/mission.exe`
- **文档目录** - 从配置文件自动推导：`{AFSIM_INSTALL_DIR}/documentation/html/docs`
- 输出包括事件日志、二进制报告和回放文件

## 📂 文档层次结构

本skill提供三层文档支持：

### 1. SKILL.md - 快速参考（首选）

- 快速导航索引
- 关键规则和最佳实践
- 各参考文档的摘要
- **使用场景**：日常脚本编写，快速查找

### 2. references/ - 详细参考（常用）

- 11个系统化参考文档
- 完整的API、命令、示例
- **使用场景**：需要详细信息时

### 3. {AFSIM_INSTALL_DIR}/documentation/ - 终极参考（备用）

- 1602个官方HTML文档
- 最权威、最详细的信息
- **使用场景**：
  - 需要确认非常具体的细节
  - 查找罕见参数或选项
  - 验证边缘情况
  - skill文档未覆盖的内容

**建议使用顺序**：SKILL.md → references/ → documentation/

---

**注意：** 本项目需要AFSIM 2.9.0。如果您的安装路径不同，请修改 `config.txt` 中的 `AFSIM_INSTALL_DIR` 配置。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件

## 🔗 相关链接

- [AFSIM 官方网站](https://github.com/afsim/afsim)
- [项目仓库](https://github.com/lookingforfeng/afsim-script-generator)

---

## 👨‍💻 关于作者

我是**冯zhangwei**，来自四川成都，致力于研究**无人机大规模异构协同智能化及仿真相关技术**。

### 研究方向

- 🚁 无人机集群协同
- 🤖 异构系统智能化
- 🎮 仿真技术与建模
- 📊 AFSIM仿真应用

### 联系方式

欢迎交流讨论！可以通过以下方式联系我：

<div align="center">

#### 添加微信好友

<img src="assets/wechat_contact.jpg" width="300" alt="微信联系方式">

*扫码添加微信，一起交流无人机仿真技术*

---

#### 支持我的工作

如果这个项目对你有帮助，欢迎请我喝杯咖啡！☕

<img src="assets/wechat_reward.jpg" width="300" alt="微信赞赏码">

*感谢你的支持！*

</div>

---

<div align="center">

**⭐ 如果觉得这个项目有用，请给个Star支持一下！⭐**

Made with ❤️ by 冯zhangwei

</div>