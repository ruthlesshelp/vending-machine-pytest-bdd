# Using a Python virtual environment

You will want to use the *venv* module to create a “virtual environment”, with an independent set of Python packages installed in the project directory.
https://docs.python.org/3/library/venv.html

Confirm the Python version with `python --version`
```zsh
Python 3.11.7
```

**NOTE:** On a lot of Linux distributions and on macOS, `python` is Python 2. `python3` is Python 3. In other installations, `python` is a command alias for `python3`. We’ll always be using `python3`, but will shorten it to `python`. If you couldn't confirm the Python version, try with `python3 --version`.

## 1. Clone this repo

[Clone this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to create a local copy on your computer.

## 2. Create and activate the virtual environment

Create the virtual environment with `python -m venv .venv`

### Activate on macOS and Linux

Activate the virtual environment with `source .venv/bin/activate`

### Activate on Windows

Activate on Windows with `.venv\Scripts\activate.bat`

**NOTE:** To activate on Windows with PowerShell use `.venv\Scripts\Activate.ps1`

## 3. Use pip to install pytest

Confirm pip version by running `pip --version`
```zsh
pip 24.0 from /Users/ ... /tdd-exercises-python/.venv/lib/python3.11/site-packages/pip (python 3.11)
```

Install pytest by running `pip install pytest`

Confirm the pytest version by running `pytest --version`
```zsh
pytest 8.1.1
```

## 4. Run the testing framework

Run pytest with the following command:
```zsh
$ pytest
```

You should get 1 failing test with the message: "You are all set!"

The output looks like this:
```zsh
rootdir: /Users/ ... /tdd-exercises-python
collected 1 item / 4 skipped                                                                     

getting_started/test_getting_started.py F                                                  [100%]

============================================ FAILURES ============================================
___________________________________________ test_start ___________________________________________

    def test_start():
>       assert True == False, "You are all set!"
E       AssertionError: You are all set!
E       assert True == False

getting_started/test_getting_started.py:4: AssertionError
==================================== short test summary info =====================================
FAILED getting_started/test_getting_started.py::test_start - AssertionError: You are all set!
================================== 1 failed, 4 skipped in 0.01s ==================================
```

## You're All Set

That's it. Return to the [Read Me](./README.md) file to configure your IDE.
