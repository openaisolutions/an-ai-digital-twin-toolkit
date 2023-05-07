"""
production.py: Production data processing module.
"""

import os

from .teamcenter import TeamcenterClient
from .cam import CamClient


class ProductionDataProcessor:
    """
    Class for processing production data.
    """

    def __init__(self, teamcenter_config_file_path, cam_config_file_path):
        """
        Constructor for ProductionDataProcessor.

        :param teamcenter_config_file_path: The file path for the Teamcenter configuration file.
        :type teamcenter_config_file_path: str
        :param cam_config_file_path: The file path for the CAM configuration file.
        :type cam_config_file_path: str
        """
        self.teamcenter_client = TeamcenterClient(teamcenter_config_file_path)
        self.cam_client = CamClient(cam_config_file_path)

    def get_production_data(self, product_id):
        """
        Get the production data for a product.

        :param product_id: The ID of the product to get the production data for.
        :type product_id: str
        :return: The production data for the product.
        :rtype: dict
        """
        # Get the product information from Teamcenter
        product_info = self.teamcenter_client.get_product_info(product_id)

        # Get the manufacturing information from CAM
        manufacturing_info = self.cam_client.get_manufacturing_info(product_info["part_number"])

        # Process the production data
        production_data = {
            "product_id": product_id,
            "part_number": product_info["part_number"],
            "manufacturing_info": manufacturing_info,
            # Add more production data as needed
        }

        return production_data


if __name__ == "__main__":
    # Example usage
    teamcenter_config_file_path = os.path.join(os.path.dirname(__file__), "teamcenter_config.json")
    cam_config_file_path = os.path.join(os.path.dirname(__file__), "cam_config.json")
    processor = ProductionDataProcessor(teamcenter_config_file_path, cam_config_file_path)
    production_data = processor.get_production_data("PRODUCT123")
    print(production_data)
