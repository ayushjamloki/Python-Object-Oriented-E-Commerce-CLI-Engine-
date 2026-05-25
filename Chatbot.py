class SupportBot:
    def __init__(self, store_inventory):
        # We pass the store's products to the bot so it knows what we sell!
        self.inventory = store_inventory

    def get_response(self, user_query):
        query = user_query.lower()
        
        # Keyword matching logic (Basic NLP intent detection)
        if "hello" in query or "hi" in query:
            return "Hello! I am your virtual store assistant. How can I help you today?"
        
        elif "shipping" in query or "delivery" in query:
            return "We offer standard delivery within 3-5 business days across India."
        
        elif "refund" in query or "return" in query:
            return "You can return products within 7 days of delivery. Please keep the original packaging."
        
        elif "gaming" in query:
            # Dynamically scans the inventory for gaming gear
            gaming_items = [item['name'] for item in self.inventory.values() 
                            if "gaming" in item['name'].lower() or "mechanical" in item['name'].lower()]
            if gaming_items:
                return f"For gaming, I highly recommend checking out: {', '.join(gaming_items)}."
            return "We have some great accessories. Check our main product list!"
            
        elif "cheap" in query or "discount" in query or "budget" in query:
            # Dynamically scans for items under ₹1000
            cheap_items = [item['name'] for item in self.inventory.values() if item['price'] < 1000]
            if cheap_items:
                return f"If you are on a budget, we have these items under ₹1000: {', '.join(cheap_items)}."
            return "All our items are reasonably priced! Check the main menu."
            
        elif "bye" in query or "exit" in query:
            return "Goodbye! Have a great time shopping."
            
        else:
            return "I am still learning! For specific product details, please check the 'View Products' menu."

    def start_chat(self):
        print("\n" + "*"*45)
        print("    E-COMMERCE SUPPORT BOT ONLINE   ")
        print("*"*45)
        print("Ask me about shipping, refunds, or product suggestions!")
        print("Type 'exit' to return to the store.")
        
        while True:
            user_input = input("\nYou: ")
            if "exit" in user_input.lower() or "bye" in user_input.lower():
                print("Bot: " + self.get_response(user_input))
                break
            
            response = self.get_response(user_input)
            print(f"Bot: {response}")