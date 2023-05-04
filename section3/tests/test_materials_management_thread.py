# test_materials_management_thread.py

import sys
sys.path.append('../src/materials_management_thread')

from bom import BOMManager
from inventory import InventoryManager
from jira import JiraIntegration
from teamcenter import TeamcenterIntegration
from sap import SAPIntegration

def main():
    # Initialize objects for each module
    bom_manager = BOMManager()
    inventory_manager = InventoryManager()
    jira_integration = JiraIntegration()
    teamcenter_integration = TeamcenterIntegration()
    sap_integration = SAPIntegration()

    # Step 1: BOM Management
    print("Starting BOM management...")
    bom_manager.load_bom_data("bom_data.csv")
    bom_manager.process_bom_data()
    bom_manager.validate_bom_data()
    bom_manager.export_bom_data("processed_bom_data.csv")
    print("BOM management completed")

    # Step 2: Inventory Management
    print("Starting inventory management...")
    inventory_manager.load_inventory_data("inventory_data.csv")
    inventory_manager.process_inventory_data()
    inventory_manager.validate_inventory_data()
    inventory_manager.export_inventory_data("processed_inventory_data.csv")
    print("Inventory management completed")

    # Step 3: Jira Integration
    print("Starting Jira integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.sync_bom_data(bom_manager)
    jira_integration.sync_inventory_data(inventory_manager)
    jira_integration.update_data()
    print("Jira integration completed")

    # Step 4: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.sync_bom_data(bom_manager)
    teamcenter_integration.sync_inventory_data(inventory_manager)
    teamcenter_integration.update_data()
    print("Teamcenter integration completed")

    # Step 5: SAP Integration
    print("Starting SAP integration...")
    sap_integration.connect_to_sap("sap_credentials.json")
    sap_integration.sync_bom_data(bom_manager)
    sap_integration.sync_inventory_data(inventory_manager)
    sap_integration.update_data()
    print("SAP integration completed")

if __name__ == "__main__":
    main()
