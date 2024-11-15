# main.py

# Import functions from inventory.py
from inventory import add_item_to_inventory, view_inventory, sell_items

def main():
    """Main program to run the grocery store management system."""
    while True:
        print("\nMenu:")
        print("1. Add Item to Inventory")
        print("2. View Inventory")
        print("3. Sell Items")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item_to_inventory()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            sell_items()
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the program
if __name__ == "__main__":
    main()
