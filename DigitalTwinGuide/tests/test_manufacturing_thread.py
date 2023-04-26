# test_manufacturing_thread.py

import sys
sys.path.append('../src/manufacturing_thread')

from manufacturing import ManufacturingManager
from teamcenter import TeamcenterIntegration
from cam import CAMIntegration
from gcode import GCodeGenerator

def main():
    # Initialize objects for each module
    manufacturing_manager = ManufacturingManager()
    teamcenter_integration = TeamcenterIntegration()
    cam_integration = CAMIntegration()
    gcode_generator = GCodeGenerator()

    # Step 1: Manufacturing Management
    print("Starting manufacturing management...")
    manufacturing_manager.load_manufacturing_data("manufacturing_data.csv")
    manufacturing_manager.process_manufacturing_data()
    manufacturing_manager.validate_manufacturing_data()
    manufacturing_manager.export_manufacturing_data("processed_manufacturing_data.csv")
    print("Manufacturing management completed")

    # Step 2: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.sync_manufacturing_data(manufacturing_manager)
    teamcenter_integration.update_data()
    print("Teamcenter integration completed")

    # Step 3: CAM Integration
    print("Starting CAM integration...")
    cam_integration.connect_to_cam("cam_credentials.json")
    cam_integration.import_manufacturing_data(manufacturing_manager)
    cam_integration.generate_toolpaths()
    cam_integration.export_toolpaths("toolpaths_data.csv")
    print("CAM integration completed")

    # Step 4: G-Code Generation
    print("Starting G-Code generation...")
    gcode_generator.import_toolpaths("toolpaths_data.csv")
    gcode_generator.generate_gcode()
    gcode_generator.export_gcode("manufacturing_gcode.txt")
    print("G-Code generation completed")

if __name__ == "__main__":
    main()
