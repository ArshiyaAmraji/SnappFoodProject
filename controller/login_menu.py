import re
from model.models import *
from controller.main_menu import enter_menu
import sys

valid_pattern = re.compile(r"^[a-zA-Z0-9_]{4,}$")

def register():
    while True:
        command = input("> ").strip().lower()
        command_parts = command.split()

        users = SnappFood.get_user()

        if len(command_parts) == 3 and command_parts[0] == "register":
            username, password = command_parts[1], command_parts[2]

            if not valid_pattern.match(username):
                print("register failed: invalid username format")
                continue
            if not valid_pattern.match(password):
                print("register failed: invalid password format")
                continue
            if username in users:
                print("register failed: username already exists")
                continue

            SnappFood.add_customer(username, password)
            print("register successful")
            register()

        elif len(command_parts) == 3 and command_parts[0] == "login":
            username, password = command_parts[1], command_parts[2]

            if username in users:
                if password == users[username]:
                    print("login successful")
                    enter_menu(username)
                    return
                else:
                    print("login failed: incorrect password")
            else:
                print("login failed: username not found")

        elif len(command_parts) == 5 and command_parts[:2] == ["change", "password"]:
            username, old_password, new_password = command_parts[2], command_parts[3], command_parts[4]

            if username not in users:
                print("password change failed: username not found")
                continue
            if users[username] != old_password:
                print("password change failed: incorrect password")
                continue
            if not valid_pattern.match(new_password):
                print("password change failed: invalid new password")
                continue


            if username in SnappFood.customers:
                SnappFood.customers[username] = new_password
            elif username in SnappFood.snappfood_admin:
                SnappFood.snappfood_admin[username] = new_password
            elif username in SnappFood.restaurant_admins:
                SnappFood.restaurant_admins[username] = new_password

            print("password change successful")

        elif command == "show current menu":
            print("login menu")

        elif command == "exit":
            sys.exit()
        else:
            print("invalid command!")
