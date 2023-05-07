# test_requirements_thread.py

import sys
sys.path.append('../src/requirements_thread')

from doors import DoorsIntegration
from cameo import CameoIntegration
from sysml import SysMLValidator

def main():
    # Initialize objects for each module
    doors_integration = DoorsIntegration()
    cameo_integration = CameoIntegration()
    sysml_validator = SysMLValidator()

    # Step 1: Doors Integration
    print("Starting Doors integration...")
    doors_integration.connect_to_doors("doors_credentials.json")
    doors_integration.load_requirements_data("doors_requirements.csv")
    doors_integration.sync_requirements_data()
    doors_integration.export_requirements_data("updated_doors_requirements.csv")
    print("Doors integration completed")

    # Step 2: Cameo Integration
    print("Starting Cameo integration...")
    cameo_integration.connect_to_cameo("cameo_credentials.json")
    cameo_integration.load_requirements_data("updated_doors_requirements.csv")
    cameo_integration.sync_requirements_data()
    cameo_integration.export_requirements_data("cameo_requirements.csv")
    print("Cameo integration completed")

    # Step 3: SysML Validation
    print("Starting SysML validation...")
    sysml_validator.load_requirements_data("cameo_requirements.csv")
    sysml_validator.validate_requirements_data()
    sysml_validator.generate_validation_report("sysml_validation_report.txt")
    print("SysML validation completed")

if __name__ == "__main__":
    main()
