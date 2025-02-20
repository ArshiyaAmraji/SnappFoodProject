from controller.login_menu import register
from model.models import SnappFood
SFA_username = input("Enter Snappfood Admin username: ")
SFA_password = input("Enter Snappfood Admin password: ")
SnappFood.add_snappfood_admin(SFA_username, SFA_password)


while True:
    register()

