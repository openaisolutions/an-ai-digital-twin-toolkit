import pandas as pd

class BOMChatInterface:
    def __init__(self, bom_manager):
        self.bom_manager = bom_manager

    def process_command(self, command):
        # Tokenize the command into words
        words = command.lower().split()

        # Process "add item" command
        if words[0] == "add" and words[1] == "item":
            item_data = {
                'item_id': words[2],
                'quantity': int(words[3]),
                'description': ' '.join(words[4:])
            }
            self.bom_manager.add_item(item_data)
            return f"Item {item_data['item_id']} added to the BOM."

        # Process "update item" command
        elif words[0] == "update" and words[1] == "item":
            item_id = words[2]
            updated_data = {
                'quantity': int(words[3]),
                'description': ' '.join(words[4:])
            }
            self.bom_manager.update_item(item_id, updated_data)
            return f"Item {item_id} updated in the BOM."

        # Process "remove item" command
        elif words[0] == "remove" and words[1] == "item":
            item_id = words[2]
            self.bom_manager.remove_item(item_id)
            return f"Item {item_id} removed from the BOM."

        # Process "get item" command
        elif words[0] == "get" and words[1] == "item":
            item_id = words[2]
            item_data = self.bom_manager.get_item(item_id)
            return f"Item data: {item_data}"

        # Process "get bom data" command
        elif words[0] == "get" and words[1] == "bom" and words[2] == "data":
            bom_data = self.bom_manager.get_bom_data()
            return f"BOM data:\n{bom_data}"

        # Process "validate bom" command
        elif words[0] == "validate" and words[1] == "bom":
            validation_results = self.bom_manager.validate_bom()
            return f"Validation results:\n{validation_results}"

        # Handle unknown command
        else:
            return "Unknown command. Please try again."

# Example usage
bom_data = pd.DataFrame({
    'item_id': ['A1', 'A2'],
    'quantity': [5, 3],
    'description': ['Bolt', 'Nut']
})
bom_manager = BOMManager(bom_data)
bom_chat_interface = BOMChatInterface(bom_manager)

# Simulate user commands
print(bom_chat_interface.process_command("add item A3 10 Screw"))
print(bom_chat_interface.process_command("update item A2 8 Washer"))
print(bom_chat_interface.process_command("get item A1"))
print(bom_chat_interface.process_command("get bom data"))
print(bom_chat_interface.process_command("validate bom"))
