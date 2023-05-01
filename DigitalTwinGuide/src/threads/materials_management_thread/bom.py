def update_inventory(self, delta):
    self.item_count += delta

def __str__(self):
    return f"{self.item_name}: {self.item_count}"