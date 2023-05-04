"""
This module provides functions to work with MATLAB in the software integration thread of the digital twin.

It requires the MATLAB engine API to be installed on the system.
"""

import matlab.engine

class MatlabEngine:
    """
    Class to interface with the MATLAB engine API.
    """
    def __init__(self):
        """
        Initializes the MATLAB engine.
        """
        self.eng = matlab.engine.start_matlab()

    def eval(self, command: str):
        """
        Evaluates the given command in MATLAB.

        Args:
        - command: The command to evaluate.

        Returns:
        - The result of the evaluation.
        """
        return self.eng.eval(command)

    def close(self):
        """
        Closes the MATLAB engine.
        """
        self.eng.quit()
