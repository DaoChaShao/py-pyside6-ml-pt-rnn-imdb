<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**项目简介**
---
本项目旨在使用 **IMDB** 数据集进行电影评论的情感分析（文本分类），通过 **PyTorch**、**TensorFlow** 以及 **PySide6**
构建完整的深度学习流程和可视化界面。

项目的主要目标是帮助学习者掌握文本处理、模型训练与评估，以及 GUI 展示的基本技能。

**功能特色**
---

- **数据处理**：使用 IMDB 数据集，进行文本预处理，包括分词、向量化、填充等操作。
- **模型训练**：基于 PyTorch 和 TensorFlow 实现 RNN、LSTM 或 Transformer 模型，用于情感分类。
- **实时可视化**：利用 PySide6 构建简单的桌面应用，可实时显示训练过程和预测结果。
- **多框架学习**：同时接触 PyTorch 和 TensorFlow，理解它们在文本分类任务中的应用差异。
- **扩展性强**：可轻松替换模型、优化器或数据预处理方法，进行实验对比。

**NLP 模型使用说明**
---
要使用本项目中提供的模型，请按照以下步骤进行：

1. 使用 **SpaCy** 包下载 NLP 模型，在终端中运行以下命令：
    ```bash
    python -m spacy download en_core_web_sm
    # 或使用 uv
    uv pip download https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.8.0/en_core_web_md-3.8.0.tar.gz
    uv pip download https://github.com/explosion/spacy-models/releases/download/zh_core_web_md-3.8.0/zh_core_web_md-3.8.0.tar.gz
    ```
   该命令会下载 **md** 版本的英文 SpaCy 模型，适用于多种自然语言处理（NLP）任务。  
   如果你计划更新模型，可以在 [SpaCy 模型页面](https://github.com/explosion/spacy-models/releases) 找到最新版本。

2. 使用 **Stanza** 包下载 NLP 模型，在 IDE 中运行以下代码：
    ```python
    import stanza
    stanza.download('en')
    stanza.download('zh')
    ```
   该命令会下载 **英文** 和 **中文** 的 Stanza 模型，它们是执行多种 NLP 任务所必需的。

3. 如果你打算在 **服务器端** 使用这些模型，请确保模型在服务器环境中被正确加载。  
   如果无法自动加载，则必须将模型放置在项目的根目录中。

**隐私声明**
---
本应用程序旨在处理您提供的数据以生成定制化的建议和结果。您的隐私至关重要。

**我们不会收集、存储或传输您的个人信息或数据。** 所有处理都在您的设备本地进行（在浏览器或运行时环境中），*
*数据永远不会发送到任何外部服务器或第三方。**

- **本地处理：** 您的数据永远不会离开您的设备。整个分析和生成过程都在本地进行。
- **无数据保留：** 由于没有数据传输，因此不会在任何服务器上存储数据。关闭应用程序通常会清除任何临时本地数据。
- **透明度：** 整个代码库都是开源的。我们鼓励您随时审查[代码](./)以验证您的数据处理方式。

总之，您始终完全控制和拥有自己的数据。

**许可声明**
---
本项目是开源的，可在 [BSD-3-Clause 许可证](LICENCE) 下使用。

简单来说，这是一个非常宽松的许可证，允许您几乎出于任何目的自由使用此代码，包括在专有项目中，只要您包含原始的版权和许可证声明。

欢迎随意分叉、修改并在此作品基础上进行构建！我们只要求您在适当的地方给予认可。

**环境设置**
---
本项目使用 **Python 3.12** 和 [uv](https://docs.astral.sh/uv/) 进行快速的依赖管理和虚拟环境处理。所需的 Python
版本会自动从 [.python-version](.python-version) 文件中检测到。

1. **安装 uv**：  
   如果您还没有安装 `uv`，可以使用以下命令安装：
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # 此安装方法适用于 macOS 和 Linux。
    ```
   或者，您可以运行以下 PowerShell 命令来安装：
    ```bash
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    # 此安装方法适用于 Windows。
    ```

   **💡 推荐**：为了获得最佳体验，请将 `uv` 作为独立工具安装。避免在 `pip` 或 `conda` 环境中安装，以防止潜在的依赖冲突。

2. **添加依赖**：

- 添加主要（生产）依赖：
    ```bash
    uv add <package_name>
    # 这会自动更新 pyproject.toml 并安装包
    ```
- 添加开发依赖：
    ```bash
    uv add <package_name> --group dev
    # 示例：uv add ruff --group dev
    # 这会自动将包添加到 [project.optional-dependencies.dev] 部分
    ```
- 添加其他类型的可选依赖（例如测试、文档）：
    ```bash
    uv add <package_name> --group test
    uv add <package_name> --group docs
    ```
- 从 `requirements.txt` 文件导入依赖：
    ```bash
    uv add -r requirements.txt
    # 这会从 requirements.txt 读取包并将其添加到 pyproject.toml
    ```

3. **移除依赖**

- 移除主要（生产）依赖：
    ```bash
    uv remove <package_name>
    # 这会自动更新 pyproject.toml 并移除包
    ```
- 移除开发依赖：
    ```bash
    uv remove <package_name> --group dev
    # 示例：uv remove ruff --group dev
    # 这会从 [project.optional-dependencies.dev] 部分移除包
    ```
- 移除其他类型的可选依赖：
    ```bash
    uv remove <package_name> --group test
    uv remove <package_name> --group docs
    ```

4. **管理环境**

- 使用添加/移除命令后，同步环境：
    ```bash
    uv sync
    ```

**更新日志**
---
本项目使用 [git-changelog](https://github.com/pawamoy/git-changelog)
基于 [Conventional Commits](https://www.conventionalcommits.org/) 自动生成和维护更新日志。

1. **安装**
   ```bash
   pip install git-changelog
   # 或使用 uv 将其添加为开发依赖
   uv add git-changelog --group dev
   ```
2. **验证安装**
   ```bash
   pip show git-changelog
   # 或专门检查版本
   pip show git-changelog | grep Version
   ```
3. **配置**
   确保您在项目根目录有一个正确配置的 `pyproject.toml` 文件。配置应将 Conventional Commits 指定为更新日志样式。以下是示例配置：
   ```toml
   [tool.git-changelog]
   version = "0.1.0"
   style = "conventional-commits"
   output = "CHANGELOG.md"
   ```
4. **生成更新日志**
   ```bash
   git-changelog --output CHANGELOG.md
   # 或者使用 uv 运行
   uv run git-changelog --output CHANGELOG.md
   ```
   此命令会根据您的 git 历史记录创建或更新 `CHANGELOG.md` 文件。
5. **推送更改**
   ```bash
   git push origin main
   ```
   或者，使用您 IDE 的 Git 界面（例如，在许多编辑器中的 `Git → Push`）。
6. **注意**：

- 更新日志是根据您的提交消息遵循 Conventional Commits 规范自动生成的。
- 每当您想要更新更新日志时（通常在发布之前或进行重大更改之后），运行生成命令。
