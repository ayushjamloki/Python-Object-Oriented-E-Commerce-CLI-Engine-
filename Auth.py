# auth.py
import json
import os

class UserAuthenticator:
    def __init__(self):
        self.filename = "users.json"
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {} 

    def save_users(self):
        with open(self.filename, "w") as file:
            json.dump(self.users, file, indent=4)

    def register(self):
        print("\n--- Create New Account ---")
        username = input("Enter a new username: ")
        
        if username in self.users:
            print("Error: Username already exists! Try logging in.")
            return None
        
        password = input("Enter a password: ")
        phone = input("Enter your phone number: ")
        address = input("Enter your shipping address: ")
        
        self.users[username] = {
            "password": password,
            "role": "customer", 
            "profile": {
                "phone": phone,
                "address": address,
                "order_history": [] 
            }
        }
        
        self.save_users()
        print(f"\n--> Registration successful! Welcome to the store, {username}.")
        return username

    def login(self):
        print("\n--- Secure Login ---")
        username = input("Username: ")
        password = input("Password: ")
        
        if username in self.users and self.users[username]["password"] == password:
            print(f"\n--> Login successful! Welcome back, {username}.")
            return username
        else:
            print("Error: Invalid username or password.")
            return None