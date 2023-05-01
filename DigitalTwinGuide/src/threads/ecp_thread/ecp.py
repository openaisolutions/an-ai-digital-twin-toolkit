class ECPProcessor:
    """
    ECPProcessor class for handling Engineering Change Proposal processing and management.

    This class provides methods to manage and process Engineering Change Proposals (ECPs),
    including creating, approving, and implementing ECPs.

    Attributes:
        ecp_list (list): A list of ECP dictionaries.
    """

    def __init__(self):
        """
        Initialize ECPProcessor with an empty list of ECPs.
        """
        self.ecp_list = []

    def create_ecp(self, ecp_data):
        """
        Create a new ECP.

        Args:
            ecp_data (dict): A dictionary containing ECP data.
        """
        self.ecp_list.append(ecp_data)

    def approve_ecp(self, ecp_id):
        """
        Approve an ECP.

        Args:
            ecp_id (int): The ID of the ECP to be approved.
        """
        for ecp in self.ecp_list:
            if ecp['ecp_id'] == ecp_id:
                ecp['status'] = 'approved'
                break

    def implement_ecp(self, ecp_id, bom_manager):
        """
        Implement an approved ECP.

        Args:
            ecp_id (int): The ID of the ECP to be implemented.
            bom_manager (BOMManager): The BOMManager instance used to modify the BOM.
        """
        for ecp in self.ecp_list:
            if ecp['ecp_id'] == ecp_id and ecp['status'] == 'approved':
                for change in ecp['changes']:
                    if change['action'] == 'add':
                        bom_manager.add_item(change['item_data'])
                    elif change['action'] == 'update':
                        bom_manager.update_item(change['item_id'], change['updated_data'])
                    elif change['action'] == 'remove':
                        bom_manager.remove_item(change['item_id'])
                ecp['status'] = 'implemented'
                break

    def get_ecp(self, ecp_id):
        """
        Get an ECP by its ID.

        Args:
            ecp_id (int): The ID of the ECP to be fetched.

        Returns:
            dict: A dictionary containing ECP data, or None if not found.
        """
        for ecp in self.ecp_list:
            if ecp['ecp_id'] == ecp_id:
                return ecp
        return None

    def get_all_ecps(self):
        """
        Get all ECPs.

        Returns:
            list: A list of ECP dictionaries.
        """
        return self.ecp_list
