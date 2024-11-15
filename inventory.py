item_names = []
item_prices = []
item_stocks = []

def add_item_to_inventory():
    """Adds an item to the inventory."""
    print("\n" + "="*50)
    print("🛠️ ADD NEW ITEM TO INVENTORY".center(50))
    print("="*50)
    name = input("Enter item name: ").strip().capitalize()
    price = float(input("Enter item price: $"))
    stock = int(input("Enter item stock quantity: "))
    item_names.append(name)
    item_prices.append(price)
    item_stocks.append(stock)
    print(f"\n✅ {name} has been successfully added to the inventory!")

def view_inventory():
    """Displays the current inventory."""
    print("\n" + "="*50)
    print("📋 CURRENT INVENTORY".center(50))
    print("="*50)
    if not item_names:
        print("🚫 The inventory is currently empty. Please add items.")
    else:
        print(f"{'Item':<20}{'Price ($)':<15}{'Stock':<10}")
        print("-"*50)
        for i in range(len(item_names)):
            print(f"{item_names[i]:<20}${item_prices[i]:<15.2f}{item_stocks[i]:<10}")
    print("="*50)

def sell_items():
    """Sells items to the customer and updates the inventory."""
    print("\n" + "="*50)
    print("💰 SELL ITEMS".center(50))
    print("="*50)
    name = input("Enter item name to sell: ").strip().capitalize()
    if name in item_names:
        index = item_names.index(name)
        quantity = int(input("Enter quantity to sell: "))
        if quantity <= item_stocks[index]:
            total_price = quantity * item_prices[index]
            item_stocks[index] -= quantity
            print(f"\n✅ Sold {quantity} {name}(s) for ${total_price:.2f}.")
            print(f"Remaining stock: {item_stocks[index]} {name}(s).")
        else:
            print(f"\n🚫 Not enough stock! Only {item_stocks[index]} {name}(s) available.")
    else:
        print("\n🚫 Item not found in inventory. Please check the name.")
