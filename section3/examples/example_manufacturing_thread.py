# example_manufacturing_thread.py

import sys
sys.path.append('../src/manufacturing_thread')

from manufacturing import ManufacturingProcess
from teamcenter import TeamcenterIntegration
from cam import CAMIntegration
from gcode import GCodeGenerator

def main():
    # Initialize objects for each module
    manufacturing_process = ManufacturingProcess()
    teamcenter_integration = TeamcenterIntegration()
    cam_integration = CAMIntegration()
    gcode_generator = GCodeGenerator()

    # Step 1: Manufacturing Process
    print("Starting manufacturing process...")
    manufacturing_process.load_data("input_data.csv")
    manufacturing_process.prepare_manufacturing_plan()
    manufacturing_process.execute_manufacturing()
    manufacturing_process.update_manufacturing_records()
    print("Manufacturing process completed")

    # Step 2: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.import_data("input_data.csv")
    teamcenter_integration.sync_manufacturing_data(manufacturing_process)
    teamcenter_integration.update_teamcenter()
    print("Teamcenter integration completed")

    # Step 3: CAM Integration
    print("Starting CAM integration...")
    cam_integration.load_model("3d_model.stl")
    cam_integration.perform_toolpath_generation()
    cam_integration.export_toolpath("toolpath_data.txt")
    print("CAM integration completed")

    # Step 4: G-Code Generation
    print("Starting G-Code generation...")
    gcode_generator.import_toolpath("toolpath_data.txt")
    gcode_generator.generate_gcode()
    gcode_generator.export_gcode("output.gcode")
    print("G-Code generation completed")

if __name__ == "__main__":
    main()
