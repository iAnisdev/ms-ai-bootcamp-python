# Python Project

## Description

This project [briefly describe your Python project, its purpose, and what it does]. The main objectives of the project are [list objectives and key features of your project].

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Setting Up Jupyter in VSCode](#setting-up-jupyter-in-vscode)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/iAnisdev/ms-ai-bootcamp-python
    cd your-repo
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Python scripts directly:

    ```bash
    python script_name.py
    ```

2. Alternatively, you can run the notebooks by setting up Jupyter as described below.

## Setting Up Jupyter in VSCode

Follow the steps below to set up Jupyter notebooks in Visual Studio Code:

### Prerequisites

- Install [Python](https://www.python.org/downloads/) (v3.6 or higher).
- Install [VSCode](https://code.visualstudio.com/Download).

### Steps

1. **Install the Python Extension in VSCode**:
    - Open VSCode and go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or press `Ctrl+Shift+X`.
    - Search for "Python" and install the official extension by Microsoft.

2. **Install Jupyter Extension**:
    - In the same Extensions view, search for "Jupyter" and install the Jupyter extension.

4. **Open or Create a Jupyter Notebook**:
    - To create a new notebook, open VSCode, go to the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac), and type `Jupyter: Create New Blank Notebook`.
    - To open an existing notebook, simply navigate to the `.ipynb` file, and VSCode will automatically open it with the Jupyter interface.

5. **Select Python Kernel**:
    - Once the notebook is opened, VSCode will prompt you to select a Python kernel. Choose the interpreter you wish to use (e.g., your virtual environment's Python).

6. **Run Cells**:
    - You can now run each cell in your Jupyter notebook by clicking the "Run" button next to the cell or using the shortcut `Shift+Enter`.

