class Delivery:
    def __init__(self, delivery_id, date, address, status):
        self.delivery_id = delivery_id
        self.date = date
        self.address = address
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Delivery {self.delivery_id} on {self.date}, {self.address} ({self.status})"
