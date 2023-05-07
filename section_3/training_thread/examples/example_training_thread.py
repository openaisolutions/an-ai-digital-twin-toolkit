# example_training_thread.py

import sys
sys.path.append('../src/training_thread')

from training import TrainingManager
from powerpoint import PowerPointIntegration
from jira import JiraIntegration

def main():
    # Initialize objects for each module
    training_manager = TrainingManager()
    powerpoint_integration = PowerPointIntegration()
    jira_integration = JiraIntegration()

    # Step 1: Training Management
    print("Starting training management...")
    training_manager.load_training_data("training_data.csv")
    training_manager.process_training_data()
    training_manager.validate_training_data()
    training_manager.export_training_data("processed_training_data.csv")
    print("Training management completed")

    # Step 2: PowerPoint Integration
    print("Starting PowerPoint integration...")
    powerpoint_integration.create_presentation(training_manager.get_training_modules())
    powerpoint_integration.save_presentation("training_presentation.pptx")
    print("PowerPoint integration completed")

    # Step 3: JIRA Integration
    print("Starting JIRA integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.sync_training_tasks(training_manager)
    jira_integration.update_issues()
    print("JIRA integration completed")

if __name__ == "__main__":
    main()
