"""
Module for interfacing with SAP in the Materials Management thread.
"""

import sap
from .bom import BillOfMaterials
from .inventory import Inventory


class SAPMaterials:
    def __init__(self, username, password):
        self.connection = sap.connect(username, password)

    def get_bom(self, part_number):
        # code to retrieve bill of materials from SAP
        return BillOfMaterials()

    def update_bom(self, part_number, bom):
        # code to update bill of materials in SAP
        pass

    def get_inventory(self, part_number):
        # code to retrieve inventory data from SAP
        return Inventory()

    def update_inventory(self, part_number, inventory):
        # code to update inventory data in SAP
        pass
