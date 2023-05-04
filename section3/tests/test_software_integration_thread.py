# test_software_integration_thread.py

import sys
sys.path.append('../src/software_integration_thread')

from code import CodeManager
from test import TestManager
from simulink import SimulinkIntegration
from jira import JiraIntegration
from teamcenter import TeamcenterIntegration
from c import CIntegration
from python import PythonIntegration
from matlab import MatlabIntegration

def main():
    # Initialize objects for each module
    code_manager = CodeManager()
    test_manager = TestManager()
    simulink_integration = SimulinkIntegration()
    jira_integration = JiraIntegration()
    teamcenter_integration = TeamcenterIntegration()
    c_integration = CIntegration()
    python_integration = PythonIntegration()
    matlab_integration = MatlabIntegration()

    # Step 1: Code Management
    print("Starting code management...")
    code_manager.load_code_data("code_data.csv")
    code_manager.process_code_data()
    code_manager.validate_code_data()
    code_manager.export_code_data("processed_code_data.csv")
    print("Code management completed")

    # Step 2: Test Management
    print("Starting test management...")
    test_manager.load_test_data("test_data.csv")
    test_manager.process_test_data()
    test_manager.validate_test_data()
    test_manager.export_test_data("processed_test_data.csv")
    print("Test management completed")

    # Step 3: Simulink Integration
    print("Starting Simulink integration...")
    simulink_integration.connect_to_simulink("simulink_credentials.json")
    simulink_integration.sync_code_data(code_manager)
    simulink_integration.update_data()
    print("Simulink integration completed")

    # Step 4: Jira Integration
    print("Starting Jira integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.sync_code_and_test_data(code_manager, test_manager)
    jira_integration.update_data()
    print("Jira integration completed")

    # Step 5: Teamcenter Integration
    print("Starting Teamcenter integration...")
    teamcenter_integration.connect_to_teamcenter("teamcenter_credentials.json")
    teamcenter_integration.sync_code_and_test_data(code_manager, test_manager)
    teamcenter_integration.update_data()
    print("Teamcenter integration completed")

    # Step 6: C, Python, and MATLAB Integrations
    print("Starting C, Python, and MATLAB integrations...")
    c_integration.sync_code_data(code_manager)
    python_integration.sync_code_data(code_manager)
    matlab_integration.sync_code_data(code_manager)
    print("C, Python, and MATLAB integrations completed")

if __name__ == "__main__":
    main()
