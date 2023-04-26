import pandas as pd

class BOMManager:
    """
    BOMManager class for handling Bill of Materials management.

    This class provides methods to manage and process Bill of Materials (BOM) data,
    including adding, updating, and removing items in the BOM.

    Attributes:
        bom_data (pd.DataFrame): The BOM data as a pandas DataFrame.
    """

    def __init__(self, bom_data):
        """
        Initialize BOMManager with a given BOM data.

        Args:
            bom_data (pd.DataFrame): The BOM data as a pandas DataFrame.
        """
        self.bom_data = bom_data

    def add_item(self, item_data):
        """
        Add an item to the BOM.

        Args:
            item_data (dict): A dictionary containing item data.
        """
        self.bom_data = self.bom_data.append(item_data, ignore_index=True)

    def update_item(self, item_id, updated_data):
        """
        Update an item in the BOM.

        Args:
            item_id (int): The ID of the item to be updated.
            updated_data (dict): A dictionary containing updated item data.
        """
        self.bom_data.loc[self.bom_data['item_id'] == item_id, updated_data.keys()] = updated_data.values()

    def remove_item(self, item_id):
        """
        Remove an item from the BOM.

        Args:
            item_id (int): The ID of the item to be removed.
        """
        self.bom_data = self.bom_data[self.bom_data['item_id'] != item_id]

    def get_item(self, item_id):
        """
        Get an item from the BOM.

        Args:
            item_id (int): The ID of the item to be fetched.

        Returns:
            dict: A dictionary containing item data.
        """
        item_data = self.bom_data.loc[self.bom_data['item_id'] == item_id].to_dict(orient='records')[0]
        return item_data

    def get_bom_data(self):
        """
        Get the entire BOM data.

        Returns:
            pd.DataFrame: The BOM data as a pandas DataFrame.
        """
        return self.bom_data
