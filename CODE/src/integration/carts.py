# cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        self.items[item_name] = self.items.get(item_name, 0) + quantity
        return f"{item_name} added"

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            return f"{item_name} removed"
        return "Item not found"
