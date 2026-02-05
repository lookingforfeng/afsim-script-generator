# AFSIM 脚本生成器

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![AFSIM Version](https://img.shields.io/badge/AFSIM-2.9.0-green.svg)](https://github.com/lookingforfeng/afsim-script-generator)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-purple.svg)](SKILL.md)

> **这是一个专为 Claude Code 设计的 Skill（技能）**

一个用于生成和执行 AFSIM（Advanced Framework for Simulation, Integration and Modeling）脚本的工具集。本项目提供了完整的 AFSIM 2.9.0 脚本语言支持，包括平台、传感器、武器、行为和任务场景。

## 🤖 关于 Claude Code Skill

本项目是一个 **Claude Code Skill**，专为扩展 Claude Code 的 AI 编程助手能力而设计。当您在 Claude Code 中需要处理 AFSIM 相关任务时，这个 Skill 会自动激活，提供专业的 AFSIM 脚本生成和执行支持。

### Skill 特征

- **智能识别**：自动识别 AFSIM 相关的编程需求
- **专业支持**：提供完整的 AFSIM 2.9.0 脚本语言语法支持
- **上下文感知**：根据您的需求自动生成合适的脚本
- **错误预防**：内置常见错误检测和最佳实践指导
- **无缝集成**：与 Claude Code 的开发流程完美融合

### 适用场景

当您在 Claude Code 中遇到以下需求时，本 Skill 会自动激活：

1. 创建 AFSIM/WSF 场景脚本
2. 生成具有正确语法的仿真脚本
3. 使用 mission.exe 运行 AFSIM 仿真
4. 调试或修复 AFSIM 脚本语法错误
5. 使用 AFSIM 脚本语言工作
6. 执行和验证 AFSIM 仿真输出

### 如何使用

在 Claude Code 中，只需描述您的 AFSIM 仿真需求，例如：

- "帮我创建一个空对空作战的 AFSIM 脚本"
- "生成一个包含雷达和导弹的飞机平台脚本"
- "运行这个 AFSIM 仿真并检查输出"

Claude Code 会自动加载本 Skill，并根据您的需求生成相应的 AFSIM 脚本。

## ✨ 功能特性

- 🎯 **脚本生成**：自动生成语法正确的 AFSIM/WSF 场景脚本
- 🚀 **脚本执行**：通过 mission.exe 运行 AFSIM 仿真
- 🔍 **语法验证**：检测并修复 AFSIM 脚本语法错误
- 📚 **完整文档**：包含语言语法、命令参考和示例
- 🛠️ **Python 工具**：提供便捷的脚本执行包装器

## 🚀 快速开始

### 前置要求

- AFSIM 2.9.0 安装在 `D:\Program Files\afsim2.9.0`
- Python 3.x

### 安装

```bash
git clone https://github.com/lookingforfeng/afsim-script-generator.git
cd afsim-script-generator
```

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

## 📖 使用指南

### 1. 收集需求

在生成脚本前，需要了解以下信息：
- 仿真场景类型（空对空、空对地、ISR 等）
- 涉及的平台（飞机、导弹、地面单位、卫星）
- 需要的传感器和武器
- 任务时间线和事件
- 输出要求

### 2. 生成脚本

使用 AFSIM 脚本语言创建场景。基本结构：

```
// 注释使用 // 或 /* */
PLATFORM my_aircraft
{
    // 平台定义
}

SENSOR my_radar
{
    // 传感器定义
}

// 仿真控制
RUN_SIMULATION
{
    // 运行时命令
}
```

**详细语法参考：**
- `references/common_mistakes.md` - **首先阅读** - 常见错误和最佳实践
- `references/language_grammar.md` - 完整语言语法
- `references/script_types.md` - 数据类型和方法
- `references/commands.md` - 命令参考
- `references/examples.md` - 示例模式

### 3. 执行脚本

使用提供的 Python 包装器：

```bash
python scripts/run_mission.py scenario.txt -es
```

### 4. 验证和迭代

- 检查 mission.exe 输出中的错误
- 验证仿真结果是否符合预期
- 根据需要调整脚本并重新运行

## 📝 常见脚本模式

### 平台定义

```
PLATFORM aircraft_1
{
    TYPE air_vehicle
    POSITION 0.0 0.0 10000.0
    VELOCITY 250.0 0.0 0.0
}
```

### 传感器定义

```
SENSOR radar_1
{
    TYPE radar
    PARENT aircraft_1
    RANGE 100000.0
}
```

### 武器定义

```
WEAPON missile_1
{
    TYPE air_to_air_missile
    PARENT aircraft_1
    QUANTITY 4
}
```

## 📂 项目结构

```
afsim-script-generator/
├── README.md                      # 项目说明文档（中文）
├── SKILL.md                       # 技能描述文件（带导航索引）
├── assets/                        # 资源文件
│   └── template.wsf              # 脚本模板
├── references/                    # 参考文档（完整系统化）
│   ├── common_mistakes.md        # 10条关键规则和常见错误
│   ├── file_structure.md         # 标准AFSIM脚本文件结构
│   ├── mover_reference.md        # 22+种mover类型完整参考
│   ├── script_api_reference.md   # WsfPlatform/Sensor/Weapon完整API
│   ├── commands_reference.md     # 完整命令语法参考
│   ├── examples.md               # 4个完整工作示例+常用模式
│   ├── language_grammar.md       # 语言语法（保留）
│   ├── script_types.md           # 数据类型（保留）
│   └── commands.md               # 命令参考（保留）
└── scripts/                       # 工具脚本
    └── run_mission.py            # mission.exe 执行包装器
```

## 🔧 故障排除

### 语法错误

- 检查 `references/language_grammar.md` 中的语法规则
- 验证 `references/commands.md` 中的命令语法
- 查看 `references/examples.md` 中的示例脚本

### 执行错误

- 确保 mission.exe 路径正确
- 检查文件权限
- 验证所有必需文件都存在

### 输出问题

- 检查仿真日志文件
- 验证输出目录存在
- 查看 mission.exe 控制台输出

## 📚 参考文档

详细文档位于 `references/` 目录（已系统化完善）：

### 核心参考文档（新增/更新）
- **references/common_mistakes.md** - **从这里开始** - 10条关键规则，避免常见错误
- **references/file_structure.md** - **新增** - 标准AFSIM脚本文件结构和模板
- **references/mover_reference.md** - **新增** - 22+种mover类型完整参考（含所有参数）
- **references/script_api_reference.md** - **新增** - WsfPlatform/Sensor/Weapon/Track完整API
- **references/commands_reference.md** - **新增** - 完整命令语法参考（platform/route/sensor/weapon/processor）
- **references/examples.md** - **重写** - 4个完整工作示例+5种常用模式

### 保留的参考文档
- **references/language_grammar.md** - 完整的脚本语言语法和语法规则
- **references/script_types.md** - 所有可用的数据类型、类及其方法
- **references/commands.md** - 按类别组织的综合命令参考

## 💡 注意事项

- **AFSIM 脚本使用 `.txt` 扩展名** - 不是 `.wsf`！
- **所有数值参数都需要单位** - 例如：`100 m/sec`、`30.0 sec`
- 脚本是基于文本的，人类可读
- mission.exe 位于 `D:\Program Files\afsim2.9.0\bin\mission.exe`
- 输出包括事件日志、二进制报告和回放文件

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件

## 🔗 相关链接

- [AFSIM 官方网站](https://github.com/afsim/afsim)
- [项目仓库](https://github.com/lookingforfeng/afsim-script-generator)

---

**注意：** 本项目需要 AFSIM 2.9.0 安装在 `D:\Program Files\afsim2.9.0`。如果您的安装路径不同，请修改 `scripts/run_mission.py` 中的路径配置。