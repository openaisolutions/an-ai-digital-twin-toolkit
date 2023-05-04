# quality_thread/python.py

import unittest

class PythonTest:
    def __init__(self):
        self.test_suite = unittest.TestSuite()

    def add_test_case(self, test_case):
        """
        Add a Python test case.

        Args:
            test_case (str): The name of the Python test case (e.g. 'my_module.MyTestCase').
        """
        self.test_suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test_case))

    def run_tests(self):
        """
        Execute the Python tests.

        Returns:
            dict: A dictionary with the status and message of the test execution.
        """
        result = unittest.TextTestRunner().run(self.test_suite)

        if result.wasSuccessful():
            return {
                "status": "success",
                "message": f"All Python tests executed successfully."
            }
        else:
            return {
                "
