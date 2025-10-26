<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**INTRODUCTION**
---
This project focuses on sentiment analysis of movie reviews using the **IMDB dataset**, combining **PyTorch**, *
*TensorFlow**, and **PySide6** to build a complete **deep learning** workflow with a visualization interface. The main
goal is to help learners understand text processing, model training & evaluation, and GUI presentation.

**FEATURES**
---

- **Data Processing**: Utilize the IMDB dataset for text preprocessing, including tokenization, vectorization, and
  padding.
- **Model Training**: Implement RNN, LSTM, or Transformer models with PyTorch and TensorFlow for sentiment
  classification.
- **Real-time Visualization**: Build a simple desktop application with PySide6 to display training progress and
  prediction results.
- **Multi-framework Learning**: Experience both PyTorch and TensorFlow and understand their differences in text
  classification tasks.
- **Highly Extensible**: Easily swap models, optimizers, or preprocessing methods for experimental comparisons.

**NLP MODELS USAGE**
---
To use the models provided in this project, follow these general steps:

1. Download the NLP models while using the SpaCy package by running the following command in your terminal:
    ```bash
    python -m spacy download en_core_web_sm
    # or using uv
    uv pip download https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.8.0/en_core_web_md-3.8.0.tar.gz
    uv pip download https://github.com/explosion/spacy-models/releases/download/zh_core_web_md-3.8.0/zh_core_web_md-3.8.0.tar.gz
    ```
   This command downloads the **md** English model for SpaCy, which is suitable for various NLP tasks. If you plan to
   update the model, you can find the latest versions on
   the [SpaCy Models page](https://github.com/explosion/spacy-models/releases).
2. Download the NLP models while using the Stanza package by running the following code in your IDE:
    ```python
    import stanza
    stanza.download('en')
    stanza.download('zh')
    ```
   This command downloads the English and Chinese models for Stanza, which are essential for various NLP tasks.
3. If you plan to use the models on the server side, ensure that the models are correctly loaded in your server
   environment if capable. Otherwise, you must put the models in your root directory.

**PRIVACY NOTICE**
---

This application is designed to process the data you provide to generate customized suggestions and results. Your
privacy is paramount.

**We do not collect, store, or transmit your personal information or data.** All processing occurs locally on your
device (in your browser or runtime environment), and **no data is ever sent to an external server or third party.**

- **Local Processing:** Your data never leaves your device. The entire analysis and generation process happens locally.
- **No Data Retention:** Since no data is transmitted, none is stored on any server. Closing the application typically
  clears any temporary local data.
- **Transparency:** The entire codebase is open source. You are encouraged to review the [code](./) to verify how your
  data is handled.

In summary, you maintain full control and ownership of your data at all times.

**LICENCE**
---
This project is open source and available under the **[BSD-3-Clause Licence](LICENCE)**.

In simple terms, this is a very permissive licence that allows you to freely use this code for almost any purpose,
including in proprietary projects, as long as you include the original copyright and licence notice.

Feel free to fork, modify, and build upon this work! We simply ask that you give credit where credit is due.

**ENVIRONMENT SETUP**
---
This project uses **Python 3.12** and [uv](https://docs.astral.sh/uv/) for fast dependency management and virtual
environment handling. The required Python version is automatically detected from the [.python-version](.python-version)
file.

1. **Installing uv**:  
   If you don't have `uv` installed, you can install it using the following command:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # This installation method works on macOS and Linux.
    ```
   Alternatively, you can install it by running the following PowerShell command:
    ```bash
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    # This installation method works on Windows.
    ```

   **💡 Recommended**: For the best experience, install `uv` as a standalone tool. Avoid installing it within `pip` or
   `conda` environments to prevent potential dependency conflicts.

2. **Adding Dependencies**:

- To add a main (production) dependency:
    ```bash
    uv add <package_name>
    # This automatically updates pyproject.toml and installs the package
    ```
- To add a development dependency:
    ```bash
    uv add <package_name> --group dev
    # Example: uv add ruff --group dev
    # This adds the package to the [project.optional-dependencies.dev] section automatically
    ```
- To add other types of optional dependencies (e.g., test, docs):
    ```bash
    uv add <package_name> --group test
    uv add <package_name> --group docs
    ```
- To import dependencies from a `requirements.txt` file:
    ```bash
    uv add -r requirements.txt
    # This reads packages from requirements.txt and adds them to pyproject.toml
    ```

3. Removing Dependencies

- To remove a main (production) dependency:
    ```bash
    uv remove <package_name>
    # This automatically updates pyproject.toml and removes the package
    ```
- To remove a development dependency:
    ```bash
    uv remove <package_name> --group dev
    # Example: uv remove ruff --group dev
    # This removes the package from the [project.optional-dependencies.dev] section
    ```
- To remove other types of optional dependencies:
    ```bash
    uv remove <package_name> --group test
    uv remove <package_name> --group docs
    ```

4. **Managing the Environment**

- After using add/remove commands, sync the environment:
    ```bash
    uv sync
    ```

**CHANGELOG**
---
This project uses [git-changelog](https://github.com/pawamoy/git-changelog) to automatically generate and maintain a
changelog based on [Conventional Commits](https://www.conventionalcommits.org/).

1. **Installation**
   ```bash
   pip install git-changelog
   # or use uv to add it as a development dependency
   uv add git-changelog --group dev
   ```
2. **Verify Installation**
   ```bash
   pip show git-changelog
   # or check the version specifically
   pip show git-changelog | grep Version
   ```
3. **Configuration**
   Ensure you have a properly configured `pyproject.toml` file at the project root. The configuration should specify
   Conventional Commits as the changelog style. Here is an example configuration:
   ```toml
   [tool.git-changelog]
   version = "0.1.0"
   style = "conventional-commits"
   output = "CHANGELOG.md"
   ```
4. **Generate Changelog**
   ```bash
   git-changelog --output CHANGELOG.md
   # Or use uv to run it if installed as a dev dependency
   uv run git-changelog --output CHANGELOG.md
   ```
   This command creates or updates the `CHANGELOG.md` file with all changes based on your git history.
5. **Push Changes**
   ```bash
   git push origin main
   ```
   Alternatively, use your IDE's Git interface (e.g., `Git → Push` in many editors).
6. **Note**:

- The changelog is automatically generated from your commit messages following the Conventional Commits specification.
- Run the generation command whenever you want to update the changelog, typically before a release or after significant
  changes.
