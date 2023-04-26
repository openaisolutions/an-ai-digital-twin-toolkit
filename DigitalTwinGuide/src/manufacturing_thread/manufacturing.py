import os
from typing import List

def create_gcode_file(cam_file: str, output_dir: str) -> str:
"""
Creates a G-code file from the given CAM file.