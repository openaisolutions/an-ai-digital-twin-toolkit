import requests


class TeamcenterIntegration:
    """
    TeamcenterIntegration class for handling Teamcenter integration.

    This class provides methods for interacting with Teamcenter, including sending and
    receiving data related to Engineering Change Proposals (ECPs) and Bill of Materials (BOM).

    Attributes:
        base_url (str): The base URL for the Teamcenter server.
        headers (dict): The headers for the HTTP requests.
    """

    def __init__(self, base_url, api_key):
        """
        Initialize TeamcenterIntegration with Teamcenter server base URL and API key.

        Args:
            base_url (str): The base URL for the Teamcenter server.
            api_key (str): The API key for the Teamcenter server.
        """
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "APIKey": api_key,
        }

    def send_ecp_data(self, ecp_data):
        """
        Send ECP data to the Teamcenter server.

        Args:
            ecp_data (dict): A dictionary containing ECP data.
        """
        url = f"{self.base_url}/ecp"
        response = requests.post(url, json=ecp_data, headers=self.headers)
        response.raise_for_status()

    def get_bom_data(self, bom_id):
        """
        Get BOM data from the Teamcenter server.

        Args:
            bom_id (int): The ID of the BOM to be fetched.

        Returns:
            dict: A dictionary containing BOM data.
        """
        url = f"{self.base_url}/bom/{bom_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_bom_data(self, bom_id, updated_data):
        """
        Update BOM data in the Teamcenter server.

        Args:
            bom_id (int): The ID of the BOM to be updated.
            updated_data (dict): A dictionary containing updated BOM data.
        """
        url = f"{self.base_url}/bom/{bom_id}"
        response = requests.put(url, json=updated_data, headers=self.headers)
        response.raise_for_status()
