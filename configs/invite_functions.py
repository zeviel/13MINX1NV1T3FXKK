import amino
from concurrent.futures import ThreadPoolExecutor

client = amino.Client()

def auth():
    while True:
        try:
            email = input("-- Email::: ")
            password = input("-- Password::: ")
            client.login(email=email, password=password)
            return False
        except Exception as e:
            print(e)
            

def communities():
    try:
        clients = client.sub_clients(size=100)
        for x, name in enumerate(clients.name, 1):
            print(f"-- {x}:{name}")
        while True:
            com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
            return com_id
    except BaseException:
        communities()


def chats(sub_client: amino.SubClient):
    try:
        chats = sub_client.get_chat_threads(size=100)
        for z, title in enumerate(chats.title, 1):
            print(f"-- {z}:{title}")
        while True:
            chat_id = chats.chatId[int(input("-- Select the chat::: ")) - 1]
            return chat_id
    except BaseException:
        return

 # invite online users


def invite_online_users():
    auth()
    sub_client = amino.SubClient(comId=communities(), profile=client.profile)
    chat_id = chats(sub_client=sub_client)
    while True:
        with ThreadPoolExecutor(max_workers=100) as executor:
            for i in range(0, 2000, 250):
                try:
                	online_users = sub_client.get_online_users(start=i, size=100).profile.userId
                	for user_id in online_users:
                        	print(f"-- Invited::: {user_id} to chat!")
                        	[
                        	executor.submit(
                        	sub_client.invite_to_chat,
                        	user_id,
                        	chat_id)]
                except Exception as e:
                      print(e)

 # invite recent users


def invite_recent_users():
    auth()
    sub_client = amino.SubClient(comId=communities(), profile=client.profile)
    chat_id = chats(sub_client=sub_client)
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(0, 2000, 15000):
            try:
            	recent_users = sub_client.get_all_users(type="recent", start=i, size=100).profile.userId
            	for user_id in recent_users:
                    	print(f"-- Invited::: {user_id} to chat!")
                    	[
                    	executor.submit(
                    	sub_client.invite_to_chat,
                        user_id,
                        chat_id)]
            except Exception as e:
                  print(e)

 # invite user followers


def invite_user_followers():
    auth()
    sub_client = amino.SubClient(comId=communities(), profile=client.profile)
    chat_id = chats(sub_client=sub_client)
    user_info = client.get_from_code(input("-- User link::: "))
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(0, 2000, 15000):
            try:
            	user_followers = sub_client.get_member_followers(userId=user_info.objectId, start=i, size=100).profile.userId
            	for user_id in user_followers:
                    	print(f"-- Invited::: {nickname} to chat!")
                    	[
                    	executor.submit(
                    	sub_client.invite_to_thread,
                        user_id,
                        chat_id)]
            except Exception as e:
                    print(e)
