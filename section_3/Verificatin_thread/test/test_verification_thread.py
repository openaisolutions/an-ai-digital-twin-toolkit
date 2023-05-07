# test_test_thread.py

import sys
sys.path.append('../src/test_thread')

from test import TestManager
from selenium import SeleniumIntegration
from cucumber import CucumberIntegration
from jira import JiraIntegration
from python import PythonTestIntegration
from java import JavaTestIntegration

def main():
    # Initialize objects for each module
    test_manager = TestManager()
    selenium_integration = SeleniumIntegration()
    cucumber_integration = CucumberIntegration()
    jira_integration = JiraIntegration()
    python_test_integration = PythonTestIntegration()
    java_test_integration = JavaTestIntegration()

    # Step 1: Test Management
    print("Starting test management...")
    test_manager.load_test_data("test_data.csv")
    test_manager.process_test_data()
    test_manager.validate_test_data()
    test_manager.export_test_data("processed_test_data.csv")
    print("Test management completed")

    # Step 2: Selenium and Cucumber Integrations
    print("Starting Selenium and Cucumber integrations...")
    selenium_integration.sync_test_data(test_manager)
    cucumber_integration.sync_test_data(test_manager)
    print("Selenium and Cucumber integrations completed")

    # Step 3: Jira Integration
    print("Starting Jira integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.sync_test_data(test_manager)
    jira_integration.update_data()
    print("Jira integration completed")

    # Step 4: Python and Java Test Integrations
    print("Starting Python and Java test integrations...")
    python_test_integration.sync_test_data(test_manager)
    java_test_integration.sync_test_data(test_manager)
    print("Python and Java test integrations completed")

if __name__ == "__main__":
    main()
