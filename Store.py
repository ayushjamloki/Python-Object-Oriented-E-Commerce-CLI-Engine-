import datetime
from Chatbot import SupportBot
from models import ElectronicItem, AccessoryItem

def admin_only(func):
    def wrapper(self, *args, **kwargs):
        if self.role != 'admin':
            print("\n⛔ ACCESS DENIED: Only Admins can perform this action!")
            return  
        
        return func(self, *args, **kwargs)
    return wrapper

class ECommerceStore:

    def __init__(self,username, role):
      self.username = username
      self.role = role
      

      self.products = {
            # Accessories 
            "P01": AccessoryItem("P01", "Wireless Mouse", 500, 20, "Matte Plastic"),
            "P03": AccessoryItem("P03", "Laptop Stand", 800, 25, "Aluminium"),
            "P08": AccessoryItem("P08", "Gaming Mouse Pad", 400, 40, "Rubber & Cloth"),
            
            # Electronics 
            "P02": ElectronicItem("P02", "Mechanical Keyboard", 1500, 15, 12), # 12 Months Warranty
            "P04": ElectronicItem("P04", "HD Webcam", 2500, 10, 6),
            "P07": ElectronicItem("P07", "27-inch 4K Monitor", 15000, 5, 36)
        }
  # Smart Recommendation Logic (Mapping ID to IDs)
      self.recommendations = {
            "P07": ["P02", "P08"], # 4K Monitor -> Suggests: Keyboard, Mouse Pad
            "P03": ["P01", "P02"], # Laptop Stand -> Suggests: Mouse, Keyboard
            "P01": ["P08"],        # Mouse -> Suggests: Mouse Pad
            "P02": ["P08", "P01"], # Keyboard -> Suggests: Mouse Pad, Mouse
            "P04": ["P07"],        # Webcam -> Suggests: Monitor
            "P08": ["P01", "P02"]  # Mouse Pad -> Suggests: Mouse, Keyboard
        }
      self.cart = {}




    def open_store(self):
        if self.role == "admin":
            self.admin_menu()
        else:
            self.customer_menu()
    
    @admin_only
    def admin_menu(self):
        
        while True:
            print("\n--- ADMIN PANEL ---")
            print("1. View Full Inventory")
            print("2. Add New Product to Store")
            print("3. Logout")
            
            choice = input("Enter choice (1-3): ")
            
            if choice == '1':
                self.display_products()
            elif choice == '2':
                p_id = input("Enter the ID (e.g., P04): ")
                name = input("Enter the Name: ")
                price = int(input("Enter the Price: "))
                stock = int(input("Enter the Stock: "))
                self.products[p_id] = {"name": name, "price": price, "stock": stock}
                print(f"\nSuccess! {name} has been added.")
            elif choice == '3':
                print("Logging out of Admin Panel...")
                break
            else:
                print("Invalid choice.")

    def customer_menu(self):
        while True:
            print(f"\n=== E-Commerce Terminal (User: {self.username}) ===")
            print("1. View Products")
            print("2. Searh products filter")
            print("3. Add to Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Ask help ")
            print("7. Logout")
            
            try:
               choice = int(input("Enter your choice (1-5): "))
            except ValueError:
                print("INvalid Input! please type a number")
                continue
            
            if choice == 1:
                self.display_products()
            elif choice == 2:
                self.search_and_sort_menu()
            elif choice == 3:
                self.add_to_cart()
            elif choice == 4:
                self.view_cart()
            elif choice == 5:
                self.checkout()
            elif choice == 6:
                bot = SupportBot(self.products)
                bot.start_chat()
            elif choice == 7:
                print(f"Logging out {self.username}...")
                break
            else:
                print("Enter a valid choice")

    
    def display_products(self):
        print("\n--- Available Products ---")
        for p_id, details in self.products.items():
            print(details.get_details())

    def add_to_cart(self):
        print("\n--- Add to Cart ---")
        p_id = input("Enter the product ID you want to add to cart: ")
        
        if p_id in self.products:
            try:
               quantity = int(input("Enter the quantity you want (e.g. 1, 2, 3): "))
            except ValueError:
                print("INvalid Quantity ! Please input the valid Quantity")
                return
            
            if self.products[p_id].stock >= quantity:
                self.cart[p_id] = quantity
                self.products[p_id].stock -= quantity
                print(f"\n✅ Success! {quantity} item(s) added to your cart.")
                
             
                self.suggest_products(p_id)    
            else:
                print(f"Sorry, we only have {self.products[p_id].stock} left in stock.") 
        else:
            print("Error: Invalid Product ID. Please check the menu.")

    def view_cart(self):
        print("\n--- Your Cart ---")
        if not self.cart:
            print("Your Cart is Empty. Please add products to cart.")
        else:
            for p_id, quantity in self.cart.items():
                print(f"ID: {p_id} | Quantity: {quantity}")
 
    def checkout(self):
        print("\n--- Checkout & Bill ---")
        if not self.cart:
            print("Your cart is empty! Please add some items first.")
            return
        
        total_amount = 0

        with open("bill_receipt.txt","a") as file:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            file.write(f"\n===================================\n")
            file.write(f"         E-COMMERCE RECEIPT          \n")
            file.write(f"Date: {current_time}\n")
            file.write(f"---------------------------------------\n")
            print("Item Details:")
        
            for p_id, quantity in self.cart.items():
               price = self.products[p_id].price
               name = self.products[p_id].name
 
               item_total = price * quantity
               total_amount += item_total

               print(f"- {name} x {quantity} = ₹{item_total}")
               file.write(f"{name} x {quantity} = Rs.{item_total}\n")

            
            print("-" * 25)
            print(f"Total Amount to Pay: ₹{total_amount}")
            print("-" * 25)
            print("Thank you for shopping with us!\n")

            file.write(f"---------------------------------\n")
            file.write(f"TOTAL AMOUNT: Rs.{total_amount}\n")
            file.write(f"=================================\n")

        
        print("--> Success! Your official bill has been saved as 'bill_receipt.txt'.")
        self.cart.clear()

    def suggest_products(self, purchased_p_id):
        if purchased_p_id in self.recommendations:
            print("\n💡 [Smart Suggestion] Customers who bought this also liked:")
            for rec_id in self.recommendations[purchased_p_id]:
                if rec_id in self.products:
                    item_obj = self.products[rec_id]
                    print(f"   -> {item_obj.name} (₹{item_obj.price}) | Use ID: {rec_id} to add!")
            print("-" * 50)

    def search_and_sort_menu(self):
        while True:
            print("\n--- Search & Sort Menu ---")
            print("1. Search Products by Keyword")
            print("2. Sort by Price (Low to High)")
            print("3. Sort by Price (High to Low)")
            print("4. Show Only In-Stock Items")
            print("5. Go Back")
            
            choice = input("Enter choice (1-5): ")
            
            if choice == '1':
                # Searching: Iterating and matching substrings
                keyword = input("Enter product name or keyword: ").lower()
                print(f"\n--- Search Results for '{keyword}' ---")
                found = False
                for p_id, item_obj in self.products.items():
                    if keyword in item_obj.name.lower():
                       print(f"[{p_id}] {item_obj.name} | Price: ₹{item_obj.price} | Stock: {item_obj.stock}")
                       found = True
                if not found:
                    print("No items found matching your search.")
                    
            elif choice == '2':
                # Sorting: Using Python's sorted() with a lambda function
                print("\n--- Products (Price: Low to High) ---")
                # lambda x: x[1]['price'] tells Python to sort based on the 'price' value inside the dictionary
                sorted_items = sorted(self.product77s.items(), key=lambda item: item[1].price)
                for p_id, item_obj in sorted_items:
                    print(f"[{p_id}] {item_obj.name} | Price: ₹{item_obj.price} | Stock: {item_obj.stock}")
                    
            elif choice == '3':
                # Sorting: High to Low uses 'reverse=True'
                print("\n--- Products (Price: High to Low) ---")
                sorted_items = sorted(self.products.items(), key=lambda item: item[1].price, reverse=True)
                for p_id, item_obj in sorted_items:
                    print(f"[{p_id}] {item_obj.name} | Price: ₹{item_obj.price} | Stock: {item_obj.stock}")
                    
            elif choice == '4':
                # Filtering: Only printing items where stock > 0
                print("\n--- In-Stock Products ---")
                for p_id, item_obj in self.products.items():
                    if item_obj.stock > 0:
                        print(f"[{p_id}] {item_obj.name} | Price: ₹{item_obj.price} | Stock: {item_obj.stock}")
                        
            elif choice == '5':
                break
            else:
                print("Invalid choice.")

