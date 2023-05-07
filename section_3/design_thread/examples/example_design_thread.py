# example_design_thread.py

import sys
sys.path.append('../src/design_thread')

from nx import NetworkDesign
from plm import PLMIntegration
from cam import CAMAutomation

def main():
    # Initialize objects for each module
    network_design = NetworkDesign()
    plm_integration = PLMIntegration()
    cam_automation = CAMAutomation()

    # Step 1: Network design using NetworkX
    print("Starting network design...")
    network_design.load_data("input_data.csv")
    network_design.create_network()
    network_design.calculate_metrics()
    network_design.visualize_network("network_design_output.png")
    print("Network design completed and saved as network_design_output.png")

    # Step 2: Integrate with Product Lifecycle Management (PLM) system
    print("Starting PLM integration...")
    plm_integration.connect_to_plm("plm_credentials.json")
    plm_integration.import_design_data("input_data.csv")
    plm_integration.sync_network_design(network_design)
    plm_integration.update_plm()
    print("PLM integration completed")

    # Step 3: Generate and export CAM data
    print("Starting CAM automation...")
    cam_automation.connect_to_cam("cam_credentials.json")
    cam_automation.import_design_data("input_data.csv")
    cam_automation.generate_toolpaths(network_design)
    cam_automation.export_gcode("gcode_output.nc")
    print("CAM automation completed and G-code saved as gcode_output.nc")

if __name__ == "__main__":
    main()
