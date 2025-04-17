
from product import Product

class Order:
    def __init__(self, user):
        self.user = user
        self.items = []  # List of Product objects

    def add_item(self, product, quantity):
        if not isinstance(product, Product):
            raise ValueError("Invalid product type.")
        self.items.extend([product] * quantity)

    def remove_item(self, product, quantity):
        count = self.items.count(product)
        if count < quantity:
            raise ValueError("Not enough items in order.")
        for _ in range(quantity):
            self.items.remove(product)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

    def display_order(self):
        if not self.items:
            print("Order is empty.")
        else:
            print("Order Details:")
            for item in self.items:
                item.display_info()
            print(f"Total: ${self.calculate_total():.2f}")