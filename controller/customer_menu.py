from model.models import SnappFood, RestaurantAdmin
import sys

def customer_command(username):
    while True:
        command = input("> ")
        command = command.lower().strip()
        command_parts = command.split()

        if len(command_parts) == 3 and command_parts[0] == "charge" and command_parts[1] == "account":
            from decimal import Decimal
            try:
                amount = Decimal(command_parts[2])
                if amount > 0:
                    SnappFood.add_balance(username, amount)
                    print("charge account successful")
                else:
                    print("charge account failed: invalid cost or price")
            except ValueError:
                print("Invalid command")

        elif command == "show balance":
            print(SnappFood.balance[username])

        elif command == "show restaurant":
            from model.models import SnappFoodAdmin
            count = 1
            for restaurant in SnappFoodAdmin.get_restaurant():
                print(f"{count}) {restaurant}")
                count += 1

        elif command.startswith("show menu") and len(command_parts) == 3:
            from model.models import SnappFoodAdmin
            restaurant_name = command_parts[2]
            if restaurant_name in SnappFoodAdmin.get_restaurant():
                foods = RestaurantAdmin.menu.get(restaurant_name, {})
                if not foods:
                    print("Menu is empty!")
                else:
                    for food, price in foods.items():
                        print(f"{food} | price = {price}")

            else:
                print("show menu failed: restaurant not found")

        elif command.startswith("add to cart") and len(command_parts) == 6:
            restaurant_name = command_parts[3]
            food_name = command_parts[4]
            try:
                number = int(command_parts[5])
                SnappFood.add_to_cart(username, food_name, restaurant_name, number)
            except ValueError:
                print("invalid command!")

        elif command == "show cart":
            total = 0
            count = 1
            for restaurant, foods in SnappFood.cart.get(username, {}).items():
                for food, price in foods.items():
                    print(f"{count}) {food} | restaurant = {restaurant} | price = {price}")
                    count += 1
                    total += price
            print(f"Total: {total}")

        elif command.startswith("remove from cart") and len(command_parts) == 6:
            restaurant_name = command_parts[3]
            food_name = command_parts[4]
            try:
                number = int(command_parts[5])
                SnappFood.remove_from_cart(username, food_name, restaurant_name, number)
            except ValueError:
                print("invalid command!")

        elif command == "purchase cart":
            total = 0
            for restaurant, foods in SnappFood.cart.get(username, {}).items():
                for food, price in foods.items():
                    total += price
            # cart = SnappFood.cart.get(username, {})
            if total == 0:
                print("Your cart is empty!")
            else:
                SnappFood.purchase(username, total)

        elif command == "logout":
            from controller.login_menu import register
            print("enter menu successful: You are in the login menu!")
            register()

        elif command == "show current menu":
            print("customer menu")

        elif command == "exit":
            sys.exit()

        else:
            print("Invalid command")
