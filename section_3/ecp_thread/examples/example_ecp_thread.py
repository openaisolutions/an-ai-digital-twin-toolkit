# examples_ecp_thread.py

import sys
sys.path.append('../src/ecp_thread')

from ecp import ECPManagement
from bom import BOMManagement
from jira import JiraIntegration
from teamcenter import TeamcenterIntegration
from sap import SAPIntegration

def main():
    # Initialize objects for each module
    ecp_management = ECPManagement()
    bom_management = BOMManagement()
    jira_integration = JiraIntegration()
    teamcenter_integration = TeamcenterIntegration()
    sap_integration = SAPIntegration()

    # Step 1: ECP Management
    print("Starting ECP management...")
    ecp_management.load_data("input_data.csv")
    ecp_management.create_ecp()
    ecp_management.review_ecp()
    ecp_management.approve_ecp()
    print("ECP management completed")

    # Step 2: BOM Management
    print("Starting BOM management...")
    bom_management.load_data("input_data.csv")
    bom_management.create_bom()
    bom_management.update_bom(ecp_management)
    bom_management.export_bom("bom_output.csv")
    print("BOM management completed and BOM saved as bom_output.csv")

    # Step 3: Jira Integration
    print("Starting Jira integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.create_issue(ecp_management)
    jira_integration.assign_issue()
    jira_integration.update_issue_status("In Progress")
    print("Jira integration completed")

    # Step 4: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.import_data("input_data.csv")
    teamcenter_integration.sync_ecp_data(ecp_management)
    teamcenter_integration.update_teamcenter()
    print("Teamcenter integration completed")

    # Step 5: SAP Integration
    print("Starting SAP integration...")
    sap_integration.connect_to_sap("sap_credentials.json")
    sap_integration.import_data("input_data.csv")
    sap_integration.sync_bom_data(bom_management)
    sap_integration.update_sap()
    print("SAP integration completed")

if __name__ == "__main__":
    main()
