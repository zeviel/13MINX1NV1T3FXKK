import amino
from utils import configs
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor

def auth(client: amino.Client):
	while True:
		try:
			email = input("[Email]::: ")
			password = input("[Password]::: ")
			client.login(email=email, password=password)
			break
		except Exception as e:
 		  print(e)   

	def communities(client: amino.Client):
		while True:
			try:
				clients = client.sub_clients(start=0, size=100)
				for x, name in enumerate(clients.name, 1):
					print(f"[{x}][{name}]")
				return clients.comId[int(input("[Select the community]::: ")) - 1]
			except Exception as e:
				print(e)
				
	def chats(sub_client: amino.SubClient):
		while True:
			try:
				chats = sub_client.get_chat_threads(start=0, size=100)
				for z, title in enumerate(chats.title, 1):
					print(f"[{z}][{title}]")
				return chats.chatId[int(input("[Select the chat]::: ")) - 1]
			except Exception as e:
				print(e)


	def invite_online_users(sub_client: amino.SubClient):
		chat_id = chats(sub_client)
		while True:
			with ThreadPoolExecutor(max_workers=100) as executor:
				for i in range(100, 2000, 25000):
					try:
						online_users = sub_client.get_online_users(start=i, size=100).profile.userId
						for user_id in online_users:
							print(f"[Invited]::: [{user_id}]")
							executor.submit(
								sub_client.invite_to_chat,
								user_id,
								chat_id)
					except Exception as e:
					  print(e)


	def invite_recent_users(sub_client: amino.SubClient):
		chat_id = chats(sub_client)
		while True:
			with ThreadPoolExecutor(max_workers=100) as executor:
				for i in range(100, 2000, 25000):
					try:
						recent_users = sub_client.get_all_users(
							type="recent",
							start=i,
							size=100).profile.userId
						for user_id in recent_users:
							print(f"[Invited]::: [{user_id}]")
							executor.submit(
								sub_client.invite_to_chat,
								user_id,
								chat_id)
					except Exception as e:
					  print(e)


	def invite_user_followers(
			client: amino.Client, sub_client: amino.SubClient):
		chat_id = chats(sub_client)
		user_id = client.get_from_code(input("[User link]::: ")).objectId
		with ThreadPoolExecutor(max_workers=100) as executor:
			for i in range(100, 2000, 25000):
				try:
					user_followers = sub_client.get_member_followers(
							userId=user_id,
							start=i,
							size=100).profile.userId
					for user_id in user_followers:
						print(f"[Invited]::: [{user_id}]")
						executor.submit(
							sub_client.invite_to_chat,
							user_id,
							chat_id)
				except Exception as e:
				  print(e)
	
	def start():
		print(configs.LOGO)
		client = amino.Client()
		auth(client)
		com_id = communities(client)
		sub_client = amino.SubClient(comId=com_id, profile=client.profile)
		print(tabulate(configs.MAIN_MENU, tablefmt="psql"))
		select = int(input("[Select]::: "))
		if select == 1:
			invite_online_users(sub_client)
		elif select == 2:
			invite_recent_users(sub_client)
		elif select == 3:
			invite_user_followers(client, sub_client)

start()
