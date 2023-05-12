# 🎮 Wordle

This repository contains the code that imitates the popular game Wordle.

## 🚀 Workflow

Follow these steps to clone the repository, set up a virtual environment, install the required dependencies, and run the game:

1. Clone the repository:

    ```
    git clone https://github.com/ethanmaxey/Wordle.git
    ```
   
2. Set up a virtual environment. If you don't want to use a virtual environment, skip to step 5, in step 5, it should auto install the dependencies:

    ```
    cd Wordle
    python3.9 -m venv venv
    ```

    This will create a virtual environment named `venv`.

3. Activate the virtual environment:

    ```
    source venv/bin/activate
    ```

4. Install the dependencies listed in `requirements.txt`:

    ```
    pip install -r requirements.txt
    ```

5. Run the game:

    ```
    paver ui
    ```

    This will start the game and allow you to play.

6. Run tests:

    ```
    paver
    ```

    This will run all the tests in the repository.

7. Clean up junk files:

    ```
    paver clean
    ```

    This will remove any `.pyc` files and `__pycache__` directories.

    ```
    paver cleanup
    ```

    This will remove any other files that are not required to run the game.

## 📦 Packages

Here are brief descriptions of the Python packages used in this project:

- **Paver**: Paver is a Python-based build and deployment tool that aims to simplify the process of managing software projects. It provides a simple and flexible way to define tasks and dependencies, and automates common tasks such as running tests, building documentation, and deploying software.

- **Radon**: Radon is a Python package that provides a set of tools for performing static code analysis of Python code. It can be used to measure code complexity, maintainability, and other metrics, and provides several different analysis methods, including Cyclomatic Complexity and Halstead metrics.

- **Coverage**: Coverage is a Python package that provides code coverage analysis for Python code. It can be used to measure how much of a codebase is covered by tests, and to identify areas of code that need additional testing. It works by running tests with a code coverage tool enabled, and then generating reports that show which lines of code were executed during the test run.

📝 **Note:** This project requires Python 3.9.13. Please ensure you have Python 3.9.13 installed before proceeding.
