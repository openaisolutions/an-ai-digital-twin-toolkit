from configuration import Configuration
from framework_facade import FrameworkFacade

class FrameworkController:
    def __init__(self, config_file="config.json"):
        self.config = Configuration(config_file)
        self.facade = FrameworkFacade(self.config)

    def execute_threads(self, thread_ids):
        for thread_id in thread_ids:
            self.facade.execute_thread(thread_id)

    def update_configuration(self, key, value):
        self.config.set_value(key, value)
        self.config.save_config()

    def get_configuration_value(self, key, default=None):
        return self.config.get_value(key, default)

if __name__ == "__main__":
    controller = FrameworkController()

    # Example: Execute threads with IDs 1 and 2
    thread_ids = [1, 2]
    controller.execute_threads(thread_ids)

    # Example: Update configuration value
    controller.update_configuration("new_key", "new_value")

    # Example: Get configuration value
    print(controller.get_configuration_value("new_key"))
