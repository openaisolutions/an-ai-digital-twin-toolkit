class Singleton:
    """
    Singleton class implementing the Singleton design pattern.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


if __name__ == "__main__":
    # Client code
    singleton_1 = Singleton()
    singleton_1.set_value("Hello, Singleton!")

    singleton_2 = Singleton()
    print(singleton_2.get_value())  # Output: "Hello, Singleton!"

    # Check if both instances are the same
    print(singleton_1 is singleton_2)  # Output: True
