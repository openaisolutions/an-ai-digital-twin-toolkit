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
