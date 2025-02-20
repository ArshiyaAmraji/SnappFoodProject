import re, sys
from model.models import SnappFoodAdmin, SnappFood, RestaurantAdmin
from controller.login_menu import register

valid_pattern = re.compile(r"^\w+$")
def snappfood_admin():
    while True:
        command = input("> ")
        command = command.lower().strip()
        command_parts = command.split()

        if len(command_parts) == 4 and command_parts[0] == "add" and command_parts[1] == "restaurant":
            restaurant_name = command_parts[2]
            restaurant_password = command_parts[3]
            if valid_pattern.match(restaurant_name):
                if valid_pattern.match(restaurant_password):
                    SnappFoodAdmin.add_restaurant(restaurant_name, restaurant_password)
                    SnappFood.add_restaurant_admin(restaurant_name, restaurant_password)
                else:
                    print("add restaurant failed: invalid password format")
            else:
                print("add restaurant failed: invalid username format")

        elif command == "show restaurant":
            count = 1
            for restaurant in SnappFoodAdmin.get_restaurant():
                print(f"{count}) {restaurant}: balance={RestaurantAdmin.restaurant_balance[restaurant]}")
                count += 1

        elif command == "logout":
            print("enter menu successful: You are in the login menu!")
            register()

        elif command == "show current menu":
            print("Snappfood admin menu")

        elif command == "exit":
            sys.exit()

        else:
            print("invalid command")
