# Windows Python Development Environment Setup Guide

This guide will walk you through the steps to set up a Python development environment on Windows.

## 1. Python Installation

1. **Download Python**: Visit the official Python website [python.org](https://www.python.org/downloads/) and download the latest version of Python.
2. **Run the Installer**: Launch the installer. Make sure to check the box that says **"Add Python to PATH"** before you click **Install Now**.
3. **Verify Installation**: Open Command Prompt and run the following command:
   ```bash
   python --version
   ```  
   This should return the version of Python you just installed.

## 2. Setting up Visual Studio Code (VS Code)

1. **Download VS Code**: Go to [code.visualstudio.com](https://code.visualstudio.com/) and download the installer for Windows.
2. **Install Extensions**: Open VS Code and navigate to the Extensions view (you can press `Ctrl+Shift+X`). Install the following extensions:
   - **Python** (by Microsoft)
   - **Pylance** (for better Python language support).
3. **Configure Python Interpreter**: Open a Python file, and VS Code will prompt you to select the Python interpreter. Choose the version you installed earlier.

## 3. Creating a Virtual Environment

1. **Open Command Prompt**: Navigate to your project directory where you want to create the virtual environment.
   ```bash
   cd path\to\your\project
   ```
2. **Create the Virtual Environment**: Run the following command:
   ```bash
   python -m venv venv
   ```
   Here, `venv` is the name of the virtual environment folder.
3. **Activate the Virtual Environment**: To start using the virtual environment, run:
   ```bash
   venv\Scripts\activate
   ```  
   You should see `(venv)` at the beginning of your command line, indicating that the virtual environment is activated.

## 4. Verification Steps

1. **Check Python Version in Virtual Environment**: Run:
   ```bash
   python --version
   ```
   This will show the Python version within the virtual environment.
2. **Install Packages**: You can now install any necessary packages using pip. For example:
   ```bash
   pip install requests
   ```
3. **Run a Sample Program**: Create a sample Python file (e.g., `main.py`) with the following content:
   ```python
   print("Hello, World!")
   ```
   Run it using:
   ```bash
   python main.py
   ```
   If everything is set up correctly, you should see `Hello, World!` printed in the console.

## Conclusion

You have now successfully set up a Python development environment on Windows using VS Code and a virtual environment. Happy coding!