# example_logistics_thread.py

import sys
sys.path.append('../src/logistics_thread')

from shipment import ShipmentManagement
from delivery import DeliveryManagement
from jira import JiraIntegration
from teamcenter import TeamcenterIntegration
from sap import SAPIntegration

def main():
    # Initialize objects for each module
    shipment_management = ShipmentManagement()
    delivery_management = DeliveryManagement()
    jira_integration = JiraIntegration()
    teamcenter_integration = TeamcenterIntegration()
    sap_integration = SAPIntegration()

    # Step 1: Shipment Management
    print("Starting shipment management...")
    shipment_management.load_data("input_data.csv")
    shipment_management.schedule_shipment()
    shipment_management.update_shipment_status("In Transit")
    print("Shipment management completed")

    # Step 2: Delivery Management
    print("Starting delivery management...")
    delivery_management.load_data("input_data.csv")
    delivery_management.schedule_delivery()
    delivery_management.update_delivery_status("Delivered")
    print("Delivery management completed")

    # Step 3: Jira Integration
    print("Starting Jira integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.create_issue(shipment_management)
    jira_integration.assign_issue()
    jira_integration.update_issue_status("In Progress")
    print("Jira integration completed")

    # Step 4: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.import_data("input_data.csv")
    teamcenter_integration.sync_shipment_data(shipment_management)
    teamcenter_integration.update_teamcenter()
    print("Teamcenter integration completed")

    # Step 5: SAP Integration
    print("Starting SAP integration...")
    sap_integration.connect_to_sap("sap_credentials.json")
    sap_integration.import_data("input_data.csv")
    sap_integration.sync_delivery_data(delivery_management)
    sap_integration.update_sap()
    print("SAP integration completed")

if __name__ == "__main__":
    main()
