# technical_data.py

import os
import zipfile


class TechnicalDataManager:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def package_technical_data(self, file_names, package_name):
        """
        Package the given list of technical data files into a single zip file.

        Args:
            file_names (list): List of technical data file names.
            package_name (str): The name of the output zip package.
        """
        package_path = os.path.join(self.output_folder, package_name)

        with zipfile.ZipFile(package_path, 'w', zipfile.ZIP_DEFLATED) as package:
            for file_name in file_names:
                file_path = os.path.join(self.input_folder, file_name)
                if os.path.isfile(file_path):
                    package.write(file_path, os.path.basename(file_path))
                else:
                    print(f"File not found: {file_path}")

        print(f"Packaged technical data successfully: {package_path}")

