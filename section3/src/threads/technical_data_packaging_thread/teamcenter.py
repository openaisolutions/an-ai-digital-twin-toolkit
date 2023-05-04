#this should modify teamcenter designs and jira issues based on the data in the csv files
# teamcenter.py

import requests


class TeamcenterManager:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def authenticate(self, username, password):
        """
        Authenticate with the Teamcenter server.

        Args:
            username (str): The username for authentication.
            password (str): The password for authentication.
        """
        url = f"{self.base_url}/authenticate"
        data = {"username": username, "password": password, "api_key": self.api_key}
        response = requests.post(url, json=data)

        if response.status_code == 200:
            self.token = response.json().get("token")
            print("Authenticated successfully with Teamcenter")
        else:
            raise Exception("Failed to authenticate with Teamcenter")

    def upload_technical_data(self, file_path):
        """
        Upload a packaged technical data file to Teamcenter.

        Args:
            file_path (str): The file path of the packaged technical data.
        """
        url = f"{self.base_url}/upload"
        headers = {"Authorization": f"Bearer {self.token}"}

        with open(file_path, "rb") as f:
            files = {"file": (file_path, f)}
            response = requests.post(url, headers=headers, files=files)

        if response.status_code == 200:
            print("Technical data uploaded successfully to Teamcenter")
        else:
            raise Exception("Failed to upload technical data to Teamcenter")
