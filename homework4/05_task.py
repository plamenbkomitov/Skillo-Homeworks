shop = {
    "bottled water": 0.60,
    "beer": 1.50,
    "sandwich": 1.90,
    "snickers": 0.90
}
shopping_cart = {}


def add_item():
    print("This is what we have available:")
    print(shop)
    add_command = str(input("Enter what you want to add: "))
    if shop.get(add_command) is None:
        print("This item is not available in our shop.")
        return

    if shopping_cart.get(add_command) is None:
        shopping_cart[add_command] = 1
    else:
        shopping_cart[add_command] = shopping_cart.get(add_command) + 1


def remove_item():
    remove_command = str(input("What do you want to remove? "))
    removed_item = shopping_cart.pop(remove_command, None)
    if removed_item is None:
        print("This item is not in your cart.")


def cart_price():
    price = 0.0
    for item, item_amount in shopping_cart.items():
        price += shop.get(item) * item_amount
    return price


def cart():
    print(shopping_cart)


def commands():
    print("1) To add an item to your cart enter \"add\".")
    print("2) To remove an item from your cart enter \"remove\".")
    print("3) To calculate the total price of your cart enter \"price\".")
    print("4) To display the contents of your cart enter \"cart\".")
    print("5} To complete purchase enter \"buy\".")
    print("6) To view available commands enter \"commands\".")


print("Welcome to our shop!")
commands()

while True:
    command = str(input("What do you want to do? "))

    if command == "add":
        add_item()
    if command == "remove":
        remove_item()
    if command == "price":
        print(cart_price())
    if command == "cart":
        cart()
    if command == "buy":
        amount = float(cart_price())
        shopping_cart.clear()
        print(f"Your purchase is completed. You've payed {amount}$. Thank you for shopping!")
        break
    if command == "commands":
        commands()
