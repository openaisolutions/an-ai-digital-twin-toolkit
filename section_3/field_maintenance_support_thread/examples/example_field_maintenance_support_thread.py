# example_field_maintenance_support_thread.py

import sys
sys.path.append('../src/field_maintenance_support_thread')

from maintenance import MaintenanceManagement
from support import SupportTicketManagement
from jira import JiraIntegration
from teamcenter import TeamcenterIntegration

def main():
    # Initialize objects for each module
    maintenance_management = MaintenanceManagement()
    support_ticket_management = SupportTicketManagement()
    jira_integration = JiraIntegration()
    teamcenter_integration = TeamcenterIntegration()

    # Step 1: Maintenance Management
    print("Starting maintenance management...")
    maintenance_management.load_data("input_data.csv")
    maintenance_management.schedule_maintenance()
    maintenance_management.perform_maintenance()
    maintenance_management.update_maintenance_records()
    print("Maintenance management completed")

    # Step 2: Support Ticket Management
    print("Starting support ticket management...")
    support_ticket_management.load_data("input_data.csv")
    support_ticket_management.create_support_ticket()
    support_ticket_management.assign_ticket()
    support_ticket_management.resolve_ticket()
    print("Support ticket management completed")

    # Step 3: Jira Integration
    print("Starting Jira integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.create_issue(support_ticket_management)
    jira_integration.assign_issue()
    jira_integration.update_issue_status("In Progress")
    print("Jira integration completed")

    # Step 4: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.import_data("input_data.csv")
    teamcenter_integration.sync_maintenance_data(maintenance_management)
    teamcenter_integration.update_teamcenter()
    print("Teamcenter integration completed")

if __name__ == "__main__":
    main()
