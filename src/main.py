
from product import Product
from inventory import Inventory
from order import Order
from user import User
from utils import validate_input

def main():
    # Initialize inventory
    inventory = Inventory()
    inventory.add_product(Product(1, "Laptop", 1200, "High-performance laptop"), 5)
    inventory.add_product(Product(2, "Mouse", 25, "Wireless mouse"), 50)
    inventory.add_product(Product(3, "Keyboard", 75, "Mechanical keyboard"), 30)

    # Initialize user
    user = User("john_doe", "password123")

    # Main loop
    while True:
        print("\nOnline Store System")
        print("1. View Products")
        print("2. View Inventory")
        print("3. Create Order")
        print("4. Exit")

        choice = validate_input("Enter your choice: ", int)

        if choice == 1:
            print("\nAvailable Products:")
            for product_id in inventory.inventory:
                product = next(p for p_id, p in inventory.inventory.items() if p_id == product_id)
                product.display_info()
        elif choice == 2:
            inventory.display_inventory()
        elif choice == 3:
            order = Order(user)
            while True:
                inventory.display_inventory()
                product_id = validate_input("Enter product ID to add to order (or 0 to finish): ", int)
                if product_id == 0:
                    break

                try:
                    product = next(p for p_id, p in inventory.inventory.items() if p_id == product_id)
                    quantity = validate_input("Enter quantity: ", int)
                    if quantity > inventory.get_quantity(product_id):
                        print("Not enough stock.")
                        continue

                    order.add_item(product, quantity)
                    inventory.remove_product(product_id, quantity)
                    print("Product added to order.")
                except (ValueError, StopIteration) as e:
                    print(f"Error: {e}")

            order.display_order()
            print(f"Total cost: ${order.calculate_total():.2f}")
        elif choice == 4:
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()