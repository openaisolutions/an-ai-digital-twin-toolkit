"""
Python module for Python-specific software integration functions.
"""
import os


def run_python_script(script_path):
    """
    Runs a Python script located at the given path.

    Args:
        script_path (str): The path to the Python script to be run.
    """
    if os.path.exists(script_path):
        os.system(f"python {script_path}")
    else:
        raise FileNotFoundError(f"No file found at path {script_path}")


def run_python_tests(test_path):
    """
    Runs Python tests located at the given path.

    Args:
        test_path (str): The path to the Python test file to be run.
    """
    if os.path.exists(test_path):
        os.system(f"python -m unittest {test_path}")
    else:
        raise FileNotFoundError(f"No file found at path {test_path}")
