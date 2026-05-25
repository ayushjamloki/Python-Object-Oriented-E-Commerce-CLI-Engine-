
# This line looks inside auth.py and brings the UserAuthenticator class here!
from Auth import UserAuthenticator 
from Store import ECommerceStore

def main():
    auth_system = UserAuthenticator()
    
    while True:
        print("\n" + "="*30)
        print("  WELCOME TO THE TERMINAL STORE  ")
        print("="*30)
        print("1. Login")
        print("2. Register New Account")
        print("3. Exit Application")
        
        choice = input("Enter your choice (1-3): ")
        
        current_user = None

        if choice == '1':
            current_user = auth_system.login()
        elif choice == '2':
            current_user = auth_system.register()
        elif choice == '3':
            print("Shutting down the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        if current_user:
            print(f"\n[System] Routing {current_user} to the Store Module...")
            
            # Get the user's role from the auth system
            role = auth_system.users[current_user]["role"]
            
            # Create the store object and pass the user info into it
            store = ECommerceStore(current_user, role)
            
            # Launch the store!
            store.open_store()

if __name__ == "__main__":
    main()