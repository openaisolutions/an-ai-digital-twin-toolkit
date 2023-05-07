#thread factory class for digitial twin guide book framework

class ThreadFactory:
    def __init__(self):
        self.thread_map = {
            "training": TrainingThread,
            "field_maintenance_support": FieldMaintenanceSupportThread,
            "manufacturing": ManufacturingThread,
            "quality": QualityThread
        }

    def create_thread(self, thread_name):
        if thread_name in self.thread_map:
            return self.thread_map[thread_name]()
        else:
            return None

#framework controller class for digitial twin guide book framework

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
    
#framework facade class for digitial twin guide book framework

class FrameworkFacade:
    def __init__(self):
        self.thread_factory = ThreadFactory()
        self.framework_controller = FrameworkController()

    def execute_thread(self, thread_name, *args, **kwargs):
        # Create the thread object using the ThreadFactory
        thread = self.thread_factory.create_thread(thread_name)

        if thread:
            # Execute the thread using the FrameworkController
            result = self.framework_controller.execute_thread(thread, *args, **kwargs)
            return result
        else:
            raise ValueError(f"Invalid thread name: {thread_name}")

    def get_thread_status(self, thread_name):
        return self.framework_controller.get_thread_status(thread_name)

    def stop_thread(self, thread_name):
        self.framework_controller.stop_thread(thread_name)

#main for digitial twin guide book framework
