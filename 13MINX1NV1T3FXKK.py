from tabulate import tabulate
from pyfiglet import figlet_format
from colored import fore, style, attr
from configs import menu_configs, invite_functions
attr(0)
print(f"""{fore.LIGHT_CORAL + style.BOLD}
Script by zeviel
Github : https://github.com/zeviel""")
print(figlet_format("13MINX1NV1T3FXKK", font="rectangles"))
print(tabulate(menu_configs.main_menu, tablefmt="psql"))
select = int(input("-- Select::: "))

if select == 1:
	invite_functions.invite_online_users()

elif select == 2:
	invite_functions.invite_recent_users()

elif select == 3:
	invite_functions.invite_user_followers()
