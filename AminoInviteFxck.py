import pyfiglet
from configs import menu_configs, invite_functions
from tabulate import tabulate
from colored import fore, back, style, attr
attr(0)
print(fore.LIGHT_CORAL + style.BOLD)
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(pyfiglet.figlet_format("aminoinvitefxck", font="rectangles"))
print(tabulate(menu_configs.main_menu, tablefmt="psql"))
select = input("Select >> ")

if select == "1":
	invite_functions.invite_online_users()

elif select == "2":
	invite_functions.invite_recent_users()

elif select == "3":
	invite_functions.invite_user_followers()
