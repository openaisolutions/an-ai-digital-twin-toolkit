# test_training_thread.py

import sys
sys.path.append('../src/training_thread')

from training import TrainingManager
from powerpoint import PowerPointManager
from jira import JiraIntegration

def main():
    # Initialize objects for each module
    training_manager = TrainingManager()
    powerpoint_manager = PowerPointManager()
    jira_integration = JiraIntegration()

    # Step 1: Training Management
    print("Starting training management...")
    training_manager.load_training_data("training_data.csv")
    training_manager.process_training_data()
    training_manager.validate_training_data()
    training_manager.export_training_data("processed_training_data.csv")
    print("Training management completed")

    # Step 2: PowerPoint Management
    print("Starting PowerPoint management...")
    powerpoint_manager.create_powerpoint_presentation("Training Presentation.pptx")
    powerpoint_manager.add_slides_from_training_data(training_manager)
    powerpoint_manager.save_presentation()
    print("PowerPoint management completed")

    # Step 3: Jira Integration
    print("Starting Jira integration...")
    jira_integration.connect_to_jira("jira_credentials.json")
    jira_integration.sync_training_data(training_manager)
    jira_integration.update_data()
    print("Jira integration completed")

if __name__ == "__main__":
    main()
