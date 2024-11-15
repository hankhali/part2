
from inventory import add_item_to_inventory, view_inventory, sell_items

def main():
    """Main program to run the grocery store management system."""
    while True:
        print("\n" + "="*60)
        print("🌟 WELCOME TO THE GROCERY STORE MANAGEMENT SYSTEM 🌟".center(60))
        print("="*60)
        print("""
🔹 [1] 🛠️ Add Item to Inventory
🔹 [2] 📋 View Inventory
🔹 [3] 💰 Sell Items
🔹 [4] ❌ Exit
        """)
        print("="*60)
        choice = input("✨ Enter your choice (1-4): ").strip()

        if choice == '1':
            add_item_to_inventory()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            sell_items()
        elif choice == '4':
            print("\n" + "="*60)
            print("🎉 THANK YOU FOR USING THE SYSTEM! SEE YOU SOON! 🎉".center(60))
            print("="*60)
            break
        else:
            print("\n🚫 Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
