from design_thread import plm

# Define the item properties
item_type = "Part"
item_name = "Widget"
item_properties = {
    "Material": "Steel",
    "Dimensions": {
        "Width": 10,
        "Length": 20,
        "Height": 30
    }
}

# Create the item
item_id = plm.create_item(item_type, item_name, item_properties)

# Get the item
item = plm.get_item(item_id)

# Update the item properties
item_properties["Material"] = "Aluminum"
plm.update_item(item_id, item_properties)

# Delete the item
plm.delete_item(item_id)
