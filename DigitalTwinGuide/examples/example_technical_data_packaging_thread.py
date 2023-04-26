# example_technical_data_packaging_thread.py

import sys
sys.path.append('../src/technical_data_packaging_thread')

from technical_data import TechnicalDataManager
from packaging import PackageManager
from jira import JiraIntegration
from teamcenter import TeamcenterIntegration

def main():
    # Initialize objects for each module
    technical_data_manager = TechnicalDataManager()
    package_manager = PackageManager()
    jira_integration = JiraIntegration()
    teamcenter_integration = TeamcenterIntegration()

    # Step 1: Technical Data Management
    print("Starting technical data management...")
    technical_data_manager.load_data("technical_data.csv")
    technical_data_manager.process_data()
    technical_data_manager.validate_data()
    technical_data_manager.export_data("processed_data.csv")
    print("Technical data management completed")

    # Step 2: Packaging
    print("Starting packaging...")
    package_manager.load_packaging_data("packaging_data.csv")
    package_manager.process_packaging_data()
    package_manager.export_packaging_data("processed_packaging_data.csv")
    print("Packaging completed")

    # Step 3: JIRA Integration
    print("Starting JIRA integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.sync_issues()
    jira_integration.update_issues()
    print("JIRA integration completed")

    # Step 4: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.sync_technical_data(technical_data_manager, package_manager)
    teamcenter_integration.update_teamcenter()
    print("Teamcenter integration completed")

if __name__ == "__main__":
    main()
