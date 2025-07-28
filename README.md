# Customs Declaration Plugin for Dify

一个用于处理物流报关文件的Dify插件，可自动处理装箱单、发票和随附文件，并生成标准化的报关Excel文件。

## 功能特性

- 自动处理多种报关相关Excel文件
- 生成标准化的报关文件
- 支持模板定制
- 易于集成到Dify工作流中

## 安装

1. 在Dify平台上创建新的插件
2. 将此仓库作为插件代码源导入
3. 配置必要的环境变量和文件路径

## 使用方法

在Dify工作流中添加此插件的代码节点，并传入包含待处理Excel文件的文件夹路径。

## 文件结构

```
customs-declaration-plugin/
├── plugin_config.yml       # 插件配置文件
├── dify_integration.py     # 核心功能实现
├── dify_config.py          # Dify环境配置
├── requirements.txt        # 依赖包列表
└── templates/
    └── 001.xlsx            # Excel模板文件
```

## 许可证

MIT
