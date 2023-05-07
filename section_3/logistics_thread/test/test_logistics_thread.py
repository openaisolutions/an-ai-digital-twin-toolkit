# test_logistics_thread.py

import sys
sys.path.append('../src/logistics_thread')

from shipment import ShipmentManager
from delivery import DeliveryManager
from jira import JiraIntegration
from teamcenter import TeamcenterIntegration
from sap import SAPIntegration

def main():
    # Initialize objects for each module
    shipment_manager = ShipmentManager()
    delivery_manager = DeliveryManager()
    jira_integration = JiraIntegration()
    teamcenter_integration = TeamcenterIntegration()
    sap_integration = SAPIntegration()

    # Step 1: Shipment Management
    print("Starting shipment management...")
    shipment_manager.load_shipment_data("shipment_data.csv")
    shipment_manager.process_shipment_data()
    shipment_manager.validate_shipment_data()
    shipment_manager.export_shipment_data("processed_shipment_data.csv")
    print("Shipment management completed")

    # Step 2: Delivery Management
    print("Starting delivery management...")
    delivery_manager.load_delivery_data("delivery_data.csv")
    delivery_manager.process_delivery_data()
    delivery_manager.validate_delivery_data()
    delivery_manager.export_delivery_data("processed_delivery_data.csv")
    print("Delivery management completed")

    # Step 3: JIRA Integration
    print("Starting JIRA integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.sync_logistics_tasks(shipment_manager, delivery_manager)
    jira_integration.update_issues()
    print("JIRA integration completed")

    # Step 4: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.sync_logistics_data(shipment_manager, delivery_manager)
    teamcenter_integration.update_data()
    print("Teamcenter integration completed")

    # Step 5: SAP Integration
    print("Starting SAP integration...")
    sap_integration.connect_to_sap("sap_credentials.json")
    sap_integration.sync_logistics_data(shipment_manager, delivery_manager)
    sap_integration.update_data()
    print("SAP integration completed")

if __name__ == "__main__":
    main()
