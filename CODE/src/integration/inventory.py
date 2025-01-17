# inventory.py
class InventorySystem:
    def __init__(self):
        self.stock = {}

    def add_stock(self, product_name, quantity):
        self.stock[product_name] = self.stock.get(product_name, 0) + quantity
        return f"{quantity} units of {product_name} added to inventory"

    def reduce_stock(self, product_name, quantity):
        if self.stock.get(product_name, 0) >= quantity:
            self.stock[product_name] -= quantity
            return f"{quantity} units of {product_name} removed from inventory"
        return "Insufficient stock"
