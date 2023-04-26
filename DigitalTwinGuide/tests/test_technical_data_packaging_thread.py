# test_technical_data_packaging_thread.py

import sys
sys.path.append('../src/technical_data_packaging_thread')

from technical_data import TechnicalDataManager
from packaging import PackagingManager
from jira import JiraIntegration
from teamcenter import TeamcenterIntegration

def main():
    # Initialize objects for each module
    technical_data_manager = TechnicalDataManager()
    packaging_manager = PackagingManager()
    jira_integration = JiraIntegration()
    teamcenter_integration = TeamcenterIntegration()

    # Step 1: Technical Data Management
    print("Starting technical data management...")
    technical_data_manager.load_technical_data("technical_data.csv")
    technical_data_manager.process_technical_data()
    technical_data_manager.validate_technical_data()
    technical_data_manager.export_technical_data("processed_technical_data.csv")
    print("Technical data management completed")

    # Step 2: Packaging Management
    print("Starting packaging management...")
    packaging_manager.load_packaging_data("packaging_data.csv")
    packaging_manager.process_packaging_data()
    packaging_manager.validate_packaging_data()
    packaging_manager.export_packaging_data("processed_packaging_data.csv")
    print("Packaging management completed")

    # Step 3: Jira Integration
    print("Starting Jira integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.sync_technical_data(technical_data_manager)
    jira_integration.sync_packaging_data(packaging_manager)
    jira_integration.update_data()
    print("Jira integration completed")

    # Step 4: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.sync_technical_data(technical_data_manager)
    teamcenter_integration.sync_packaging_data(packaging_manager)
    teamcenter_integration.update_data()
    print("Teamcenter integration completed")

if __name__ == "__main__":
    main()
