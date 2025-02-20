from controller.customer_menu import customer_command
from model.models import SnappFood
import sys

def enter_menu(username):
    while True:
        user_command = input("> ")
        user_command = user_command.lower().strip()
        user_command_parts = user_command.split()

        if user_command == "enter customer menu":
            if username in SnappFood.customers:
                print("enter menu successful: You are in the customer menu!")
                customer_command(username)
            else:
                print("enter menu failed: access denied")

        elif user_command == "show current menu":
            print("main menu")

        elif user_command == "enter restaurant admin menu":
            if username in SnappFood.restaurant_admins:
                print("enter menu successful: You are in the restaurant admin menu!")
                from controller.restaurant_admin_menu import restaurant_admin
                restaurant_admin(username)
            else:
                print("enter menu failed: access denied")

        elif user_command == "enter snappfood admin menu":
            if username in SnappFood.snappfood_admin:
                print("enter menu successful: You are in the snappfood admin menu!")
                from controller.snappfood_admin_menu import snappfood_admin
                snappfood_admin()
            else:
                print("enter menu failed: access denied")

        elif user_command == "logout" or user_command == "log out":
            print("enter menu successful: You are in the login menu!")
            from controller.login_menu import register
            register()

        elif user_command == "exit":
            sys.exit()

        elif len(user_command_parts) == 4 and (
                user_command_parts[1] != "restaurant" or user_command_parts[2] != "admin"):
            print("enter menu failed: invalid menu name")

        elif len(user_command_parts) == 3 and user_command_parts[1] != "customer" and user_command_parts[0] == "enter":
            print("enter menu failed: invalid menu name")

        else:
            print("invalid command")
