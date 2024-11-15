item_names = []
item_prices = []
item_stocks = []


def add_item_to_inventory():
    """Adds an item to the inventory."""
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    stock = int(input("Enter item stock: "))
    item_names.append(name)
    item_prices.append(price)
    item_stocks.append(stock)
    print(f"{name} added to inventory.")
def view_inventory():
    """Displays the current inventory."""
    if not item_names:
        print("Inventory is empty.")
    else:
        print("\nInventory:")
        for i in range(len(item_names)):
            print(f"{item_names[i]} - Price: ${item_prices[i]:.2f}, Stock: {item_stocks[i]}")

def sell_items():
    """Sells items to the customer and updates the inventory."""
    name = input("Enter item name to sell: ")
    if name in item_names:
        index = item_names.index(name)
        quantity = int(input("Enter quantity to sell: "))
        if quantity <= item_stocks[index]:
            total_price = quantity * item_prices[index]
            item_stocks[index] -= quantity
            print(f"Sold {quantity} {name}(s) for ${total_price:.2f}.")
        else:
            print(f"Not enough stock. Only {item_stocks[index]} available.")
    else:
        print("Item not found in inventory.")
