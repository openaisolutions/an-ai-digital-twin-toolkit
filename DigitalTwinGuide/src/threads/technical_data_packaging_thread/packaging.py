#draft a py script for technical data paackaging thread
# packaging.py

import os
import zipfile


class PackagingManager:
    def __init__(self):
        self.packaged_data = []

    def load_technical_data(self, data_files):
        """
        Load the technical data files to be packaged.

        Args:
            data_files (list): A list of file paths to technical data files.
        """
        self.packaged_data = data_files

    def validate_technical_data(self):
        """
        Validate the technical data files. This method can be customized to
        implement specific validation rules based on the project requirements.
        """
        for data_file in self.packaged_data:
            if not os.path.isfile(data_file):
                raise FileNotFoundError(f"File not found: {data_file}")

    def package_technical_data(self, output_path):
        """
        Package the technical data files into a zip archive.

        Args:
            output_path (str): The file path to save the zip archive.
        """
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for data_file in self.packaged_data:
                zf.write(data_file, os.path.basename(data_file))

        print(f"Packaged technical data saved to {output_path}")
