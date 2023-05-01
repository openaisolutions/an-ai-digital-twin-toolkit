class Inventory:
def init(self, item_id, item_name, item_count):
self.item_id = item_id
self.item_name = item_name
self.item_count = item_count
def update_inventory(self, delta):
    self.item_count += delta

def __str__(self):
    return f"{self.item_name}: {self.item_count}"
