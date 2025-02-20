from model.models import  RestaurantAdmin

def restaurant_admin(name):
    while True:
        command = input("> ").strip()
        command_parts = command.split()

        if len(command_parts) == 3 and command_parts[0] == "charge" and command_parts[1] == "account":
            from decimal import Decimal
            try:
                amount = Decimal(command_parts[2])
                if amount > 0:
                    RestaurantAdmin.add_restaurant_balance(name, amount)
                    print("charge account successful")
                else:
                    print("charge account failed: invalid cost or price")
            except ValueError:
                print("Invalid command")

        elif command.startswith("add food") and len(command_parts) == 5:
            food_name = command_parts[2]
            try:
                food_price = float(command_parts[3])
                food_cost = float(command_parts[4])
                RestaurantAdmin.add_food(food_name, food_price, food_cost, name)
            except ValueError:
                print("Invalid command")

        elif command == "show balance":
            print(RestaurantAdmin.restaurant_balance[name])

        elif command == "show current menu":
            print("restaurant admin menu")

        elif command == "logout":
            print("enter menu successful: You are in the login menu!")
            from controller.login_menu import register
            register()

        elif command == "exit":
            import sys
            sys.exit()

        else:
            print("Invalid command")
