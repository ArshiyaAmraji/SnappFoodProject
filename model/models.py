class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class RestaurantAdmin:
    restaurant_balance = {}
    menu = {}
    food_cost = {}

    @staticmethod
    def add_restaurant_balance(name, restaurant_amount):
        RestaurantAdmin.restaurant_balance[name] += restaurant_amount

    @staticmethod
    def deduct_balance(name, restaurant_amount):
        if restaurant_amount > 0:
            RestaurantAdmin.restaurant_balance[name] -= restaurant_amount

    @staticmethod
    def add_food(name, price, cost, res_name):
        import re
        valid_pattern = r"^[a-z-]+$"

        if not re.fullmatch(valid_pattern, name):
            print("Add food failed: invalid food name")
            return

        if res_name not in RestaurantAdmin.menu:
            RestaurantAdmin.menu[res_name] = {}

        if res_name not in RestaurantAdmin.food_cost:
            RestaurantAdmin.food_cost[res_name] = {}

        if name not in RestaurantAdmin.menu[res_name]:
            if price > 0 and cost > 0:
                RestaurantAdmin.menu[res_name][name] = price
                RestaurantAdmin.food_cost[res_name][name] = cost
                print("Add food successful")
            else:
                print("Add food failed: invalid price or cost")
        else:
            print("Add food failed: food already exists")


class SnappFood:
    customers = {}
    snappfood_admin = {}
    restaurant_admins = {}
    balance = {}
    cart = {}

    @staticmethod
    def add_customer(username, password):
        SnappFood.customers[username] = password
        SnappFood.balance[username] = 0

    @staticmethod
    def add_snappfood_admin(username, password):
        SnappFood.snappfood_admin[username] = password

    @staticmethod
    def add_restaurant_admin(username, password):
        SnappFood.restaurant_admins[username] = password

    @staticmethod
    def get_user():
        return SnappFood.customers | SnappFood.restaurant_admins | SnappFood.snappfood_admin

    @staticmethod
    def add_balance(username, amount):
        SnappFood.balance[username] += amount

    @staticmethod
    def add_to_cart(username, food_name, restaurant_name, number):
        if restaurant_name not in SnappFood.restaurant_admins:
            print("add to cart failed: restaurant not found")
        elif food_name not in RestaurantAdmin.menu[restaurant_name]:
            print("add to cart failed: food not found")
        elif number <= 0:
            print("add to cart failed: invalid number")
        else:
            price = number * RestaurantAdmin.menu[restaurant_name][food_name]
            SnappFood.cart.setdefault(username, {}).setdefault(restaurant_name, {})[food_name] = price
            print("add to cart successful")

    @staticmethod
    def remove_from_cart(username, food_name, restaurant_name, number):
        if restaurant_name not in SnappFood.cart[username]:
            print("remove from cart failed: not in cart")
        elif food_name not in SnappFood.cart[username][restaurant_name]:
            print("remove from cart failed: not in cart")
        elif number > SnappFood.cart[username][restaurant_name][food_name]:
            print("remove from cart failed: not enough food in cart")
        elif number <= 0:
            print("remove from cart failed: invalid number")
        elif number > SnappFood.cart[username][restaurant_name][food_name] / RestaurantAdmin.menu[restaurant_name][food_name]:
            print("remove from cart failed: not enough food in cart")
        elif number == SnappFood.cart[username][restaurant_name][food_name] / RestaurantAdmin.menu[restaurant_name][food_name]:
            del SnappFood.cart[username][restaurant_name][food_name]
            print("remove from cart successful")
        elif number < SnappFood.cart[username][restaurant_name][food_name] / RestaurantAdmin.menu[restaurant_name][food_name]:
            SnappFood.cart[username][restaurant_name][food_name] -= number * RestaurantAdmin.menu[restaurant_name][food_name]
            print("remove from cart successful")

    @staticmethod
    def purchase(username, total):
        if total > SnappFood.balance[username]:
            print("purchase failed: inadequate money")
        else:
            for res_name in SnappFood.cart[username].keys():
                add_money = 0
                decrease = 0
                for food_name in SnappFood.cart[username][res_name].keys():
                    add_money += SnappFood.cart[username][res_name][food_name]
                    decrease += RestaurantAdmin.food_cost[res_name][food_name] * (
                        SnappFood.cart[username][res_name][food_name] / RestaurantAdmin.menu[res_name][food_name]
                    )
                RestaurantAdmin.add_restaurant_balance(res_name, add_money)
                RestaurantAdmin.deduct_balance(res_name, decrease)

            SnappFood.balance[username] -= total
            del SnappFood.cart[username]
            print("purchase successful")


class SnappFoodAdmin:
    restaurants = {}

    @staticmethod
    def add_restaurant(name, password):
        if name in SnappFoodAdmin.restaurants:
            print("add restaurant failed: username already exists")
        else:
            SnappFoodAdmin.restaurants[name] = password
            RestaurantAdmin.restaurant_balance[name] = 0
            print("add restaurant successful")

    @staticmethod
    def get_restaurant():
        return SnappFoodAdmin.restaurants.keys()
