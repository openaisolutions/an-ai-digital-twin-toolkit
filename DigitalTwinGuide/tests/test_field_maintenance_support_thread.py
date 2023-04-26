# test_field_maintenance_support_thread.py

import sys
sys.path.append('../src/field_maintenance_support_thread')

from maintenance import MaintenanceManager
from support import SupportManager
from jira import JiraIntegration
from teamcenter import TeamcenterIntegration

def main():
    # Initialize objects for each module
    maintenance_manager = MaintenanceManager()
    support_manager = SupportManager()
    jira_integration = JiraIntegration()
    teamcenter_integration = TeamcenterIntegration()

    # Step 1: Maintenance Management
    print("Starting maintenance management...")
    maintenance_manager.load_maintenance_data("maintenance_data.csv")
    maintenance_manager.process_maintenance_data()
    maintenance_manager.validate_maintenance_data()
    maintenance_manager.export_maintenance_data("processed_maintenance_data.csv")
    print("Maintenance management completed")

    # Step 2: Support Management
    print("Starting support management...")
    support_manager.load_support_data("support_data.csv")
    support_manager.process_support_data()
    support_manager.validate_support_data()
    support_manager.export_support_data("processed_support_data.csv")
    print("Support management completed")

    # Step 3: JIRA Integration
    print("Starting JIRA integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.sync_maintenance_support_tasks(maintenance_manager, support_manager)
    jira_integration.update_issues()
    print("JIRA integration completed")

    # Step 4: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.sync_maintenance_support_data(maintenance_manager, support_manager)
    teamcenter_integration.update_data()
    print("Teamcenter integration completed")

if __name__ == "__main__":
    main()
