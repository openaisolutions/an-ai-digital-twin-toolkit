# test_production_thread.py

import sys
sys.path.append('../src/production_thread')

from production import ProductionManager
from teamcenter import TeamcenterIntegration
from cam import CAMIntegration
from gcode import GcodeGenerator

def main():
    # Initialize objects for each module
    production_manager = ProductionManager()
    teamcenter_integration = TeamcenterIntegration()
    cam_integration = CAMIntegration()
    gcode_generator = GcodeGenerator()

    # Step 1: Production Management
    print("Starting production management...")
    production_manager.load_production_data("production_data.csv")
    production_manager.process_production_data()
    production_manager.validate_production_data()
    production_manager.export_production_data("processed_production_data.csv")
    print("Production management completed")

    # Step 2: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.sync_production_data(production_manager)
    teamcenter_integration.update_data()
    print("Teamcenter integration completed")

    # Step 3: CAM Integration
    print("Starting CAM integration...")
    cam_integration.connect_to_cam("cam_credentials.json")
    cam_integration.sync_production_data(production_manager)
    cam_integration.update_data()
    print("CAM integration completed")

    # Step 4: Gcode Generation
    print("Starting Gcode generation...")
    gcode_generator.load_cam_data(cam_integration)
    gcode_generator.generate_gcode()
    gcode_generator.export_gcode("generated_gcode.gcode")
    print("Gcode generation completed")

if __name__ == "__main__":
    main()
