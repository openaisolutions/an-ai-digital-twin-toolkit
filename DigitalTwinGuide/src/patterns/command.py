from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class ConcreteCommandA(Command):
    """
    Concrete Commands implement various kinds of requests.
    """

    def execute(self) -> None:
        print("ConcreteCommandA: Handling request")


class ConcreteCommandB(Command):
    """
    Concrete Commands implement various kinds of requests.
    """

    def execute(self) -> None:
        print("ConcreteCommandB: Handling request")


class Invoker:
    """
    The Invoker is responsible for initializing and executing commands.
    """

    def __init__(self) -> None:
        self._commands = []

    def add_command(self, command: Command) -> None:
        self._commands.append(command)

    def execute_commands(self) -> None:
        for command in self._commands:
            command.execute()


if __name__ == "__main__":
    # Client code
    invoker = Invoker()
    command_a = ConcreteCommandA()
    command_b = ConcreteCommandB()

    invoker.add_command(command_a)
    invoker.add_command(command_b)

    invoker.execute
