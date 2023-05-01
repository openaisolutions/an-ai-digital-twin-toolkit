import os
import json


class Configuration:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as file:
                config_data = json.load(file)
            return config_data
        else:
            raise FileNotFoundError(f"Configuration file '{self.config_file}' not found.")

    def get_value(self, key, default=None):
        return self.config_data.get(key, default)

    def set_value(self, key, value):
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, "w") as file:
            json.dump(self.config_data, file, indent=4, sort_keys=True)
