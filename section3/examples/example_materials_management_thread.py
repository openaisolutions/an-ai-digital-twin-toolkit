# example_materials_management_thread.py

import sys
sys.path.append('../src/materials_management_thread')

from bom import BillOfMaterials
from inventory import InventoryManagement
from jira import JiraIntegration
from teamcenter import TeamcenterIntegration
from sap import SAPIntegration

def main():
    # Initialize objects for each module
    bill_of_materials = BillOfMaterials()
    inventory_management = InventoryManagement()
    jira_integration = JiraIntegration()
    teamcenter_integration = TeamcenterIntegration()
    sap_integration = SAPIntegration()

    # Step 1: Bill of Materials
    print("Starting Bill of Materials process...")
    bill_of_materials.load_data("bom_data.csv")
    bill_of_materials.calculate_material_requirements()
    bill_of_materials.update_bom_records()
    print("Bill of Materials process completed")

    # Step 2: Inventory Management
    print("Starting Inventory Management process...")
    inventory_management.load_data("inventory_data.csv")
    inventory_management.update_inventory(bill_of_materials)
    inventory_management.check_availability()
    inventory_management.generate_purchase_orders()
    print("Inventory Management process completed")

    # Step 3: Jira Integration
    print("Starting Jira integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.create_materials_management_tasks()
    jira_integration.sync_tasks_with_inventory(inventory_management)
    print("Jira integration completed")

    # Step 4: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.import_bom_data("bom_data.csv")
    teamcenter_integration.sync_bom_data(bill_of_materials)
    teamcenter_integration.update_teamcenter()
    print("Teamcenter integration completed")

    # Step 5: SAP Integration
    print("Starting SAP integration...")
    sap_integration.connect_to_sap("sap_credentials.json")
    sap_integration.import_purchase_orders(inventory_management.purchase_orders)
    sap_integration.sync_purchase_orders()
    sap_integration.update_sap()
    print("SAP integration completed")

if __name__ == "__main__":
    main()
