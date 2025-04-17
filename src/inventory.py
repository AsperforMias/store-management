
from product import Product

class Inventory:
    def __init__(self):
        self.inventory = {}  # {product_id: quantity}

    def add_product(self, product, quantity):
        if not isinstance(product, Product):
            raise ValueError("Invalid product type.")
        if product.product_id in self.inventory:
            self.inventory[product.product_id] += quantity
        else:
            self.inventory[product.product_id] = quantity

    def remove_product(self, product_id, quantity):
        if product_id not in self.inventory:
            raise ValueError("Product not found in inventory.")
        if quantity > self.inventory[product_id]:
            raise ValueError("Not enough stock.")
        self.inventory[product_id] -= quantity
        if self.inventory[product_id] == 0:
            del self.inventory[product_id]

    def get_quantity(self, product_id):
        return self.inventory.get(product_id, 0)

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")

        else:
            print("Current Inventory:")
            for product_id, quantity in self.inventory.items():
                print(f"Product ID: {product_id}, Quantity: {quantity}")