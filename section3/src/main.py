from framework_facade import FrameworkFacade
from configuration import Configuration
from framework_controller import FrameworkController
from logger import Logger
from command import Invoker, ConcreteCommandA, ConcreteCommandB
from singleton import SingletonMeta


class Main(metaclass=SingletonMeta):
    def __init__(self):
        self._config = Configuration.load_configuration("config.json")
        self._logger = Logger(self._config.logging_level)
        self._framework_controller = FrameworkController(self._config)
        self._facade = FrameworkFacade(self._framework_controller, self._logger)

        self._invoker = Invoker()
        self._register_commands()

    def _register_commands(self):
        command_a = ConcreteCommandA()
        command_b = ConcreteCommandB()

        self._invoker.register_command("A", command_a)
        self._invoker.register_command("B", command_b)

    def run(self):
        self._facade.initialize_framework()

        print(self._invoker.execute_command("A"))
        print(self._invoker.execute_command("B"))

        self._facade.terminate_framework()


if __name__ == "__main__":
    main = Main()
    main.run()
