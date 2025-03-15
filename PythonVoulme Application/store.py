import json
import os

class OnlineStore:
    def __init__(self, data_directory):
        self.products = {
            '1': {'name': 'Laptop', 'price': 1000},
            '2': {'name': 'Phone', 'price': 500},
            '3': {'name': 'Headphones', 'price': 100}
        }
        self.cart = []
        self.data_directory = data_directory
        self.cart_file = os.path.join(self.data_directory, 'cart_data.json')
        self.load_cart_data()

    def load_cart_data(self):
        """Load cart data from the volume file if it exists."""
        if os.path.exists(self.cart_file):
            with open(self.cart_file, 'r') as f:
                self.cart = json.load(f)

    def save_cart_data(self):
        """Save cart data to the volume file."""
        with open(self.cart_file, 'w') as f:
            json.dump(self.cart, f)

    def display_products(self):
        print("\nAvailable Products:")
        for key, product in self.products.items():
            print(f"{key}: {product['name']} - ${product['price']}")

    def add_to_cart(self, product_id):
        if product_id in self.products:
            self.cart.append(self.products[product_id])
            print(f"{self.products[product_id]['name']} added to cart.")
            self.save_cart_data()  # Save cart after adding item
        else:
            print("Invalid product ID.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("\nYour Cart:")
            total = 0
            for item in self.cart:
                print(f"{item['name']} - ${item['price']}")
                total += item['price']
            print(f"Total: ${total}")

    def checkout(self):
        if not self.cart:
            print("Your cart is empty. Add items before checkout.")
        else:
            self.view_cart()
            print("Checkout complete. Thank you for shopping!")
            self.cart = []  # Clear cart after checkout
            self.save_cart_data()  # Save empty cart data after checkout

# Assume the volume directory is mounted at /app/data
data_directory = '/app/data'
store = OnlineStore(data_directory)

while True:
    print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Checkout\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        store.display_products()
    elif choice == '2':
        product_id = input("Enter product ID to add to cart: ")
        store.add_to_cart(product_id)
    elif choice == '3':
        store.view_cart()
    elif choice == '4':
        store.checkout()
    elif choice == '5':
        print("Thankyou uuuuu.")
        break
    else:
        print("Invalid choice. Please try again.")
