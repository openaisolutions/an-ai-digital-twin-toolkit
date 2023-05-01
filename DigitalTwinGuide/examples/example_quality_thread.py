# example_test_thread.py

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

    # Step 2: Selenium Integration
    print("Starting Selenium integration...")
    selenium_integration.run_tests(test_manager.get_test_cases())
    selenium_integration.export_test_results("selenium_test_results.csv")
    print("Selenium integration completed")

    # Step 3: Cucumber Integration
    print("Starting Cucumber integration...")
    cucumber_integration.run_tests(test_manager.get_test_cases())
    cucumber_integration.export_test_results("cucumber_test_results.csv")
    print("Cucumber integration completed")

    # Step 4: JIRA Integration
    print("Starting JIRA integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.sync_test_results(test_manager)
    jira_integration.update_issues()
    print("JIRA integration completed")

    # Step 5: Python Test Integration
    print("Starting Python test integration...")
    python_test_integration.run_tests(test_manager.get_test_cases())
    python_test_integration.export_test_results("python_test_results.csv")
    print("Python test integration completed")

    # Step 6: Java Test Integration
    print("Starting Java test integration...")
    java_test_integration.run_tests(test_manager.get_test_cases())
    java_test_integration.export_test_results("java_test_results.csv")
    print("Java test integration completed")

if __name__ == "__main__":
    main()
