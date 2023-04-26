# example_requirements_thread.py

import sys
sys.path.append('../src/requirements_thread')

from doors import DoorsIntegration
from cameo import CameoIntegration
from sysml import SysMLModel

def main():
    # Initialize objects for each module
    doors_integration = DoorsIntegration()
    cameo_integration = CameoIntegration()
    sysml_model = SysMLModel()

    # Step 1: DOORS Integration
    print("Starting DOORS integration...")
    doors_integration.connect_to_doors("doors_credentials.json")
    doors_integration.load_requirements("requirements_data.csv")
    doors_integration.sync_requirements()
    print("DOORS integration completed")

    # Step 2: Cameo Integration
    print("Starting Cameo integration...")
    cameo_integration.connect_to_cameo("cameo_credentials.json")
    cameo_integration.load_model("sysml_model.mdzip")
    cameo_integration.sync_requirements(doors_integration)
    cameo_integration.update_cameo_model()
    print("Cameo integration completed")

    # Step 3: SysML Model
    print("Starting SysML model processing...")
    sysml_model.load_model("sysml_model.mdzip")
    sysml_model.process_model()
    sysml_model.export_diagrams("diagram_folder")
    sysml_model.validate_model()
    print("SysML model processing completed")

if __name__ == "__main__":
    main()
