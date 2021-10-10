import samino
import concurrent.futures
client = samino.Client(None)


def auth():
    while True:
        try:
            email = input("Email >> ")
            password = input("Password >> ")
            client.login(email=email, password=password)
            return False
        except Exception as e:
            print(e)
        except BaseException:
            return


def communities():
    try:
        clients = client.get_my_communitys(size=100)
        for x, name in enumerate(clients.name, 1):
            print(f"{x}.{name}")
        while True:
            com_Id = clients.comId[int(input("Select the community >> ")) - 1]
            return com_Id
    except ValueError:
        print("ValueError")
        communities()
    except Exception as e:
        print(e)
    except BaseException:
        return


def chats(local: str):
    try:
        chats = local.get_chat_threads(size=100)
        for z, title in enumerate(chats.title, 1):
            print(f"{z}.{title}")
        while True:
            chat_Id = chats.chatId[int(input("Select The Chat >> ")) - 1]
            return chat_Id
    except ValueError:
        print("ValueError")
        return
    except Exception as e:
        print(e)
        return
    except BaseException:
        return

 # invite online users


def invite_online_users():
    auth()
    local = samino.Local(communities())
    chat_Id = chats(local)
    while True:
        with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
            for i in range(0, 2000, 250):
                try:
                	online_users = local.get_online_users(start=i, size=100)
                	for nickname, user_Id in zip(
                        online_users.nickname, online_users.userId):
                        	print(f"{nickname} Invited to chat")
                        	_ = [
                        	executor.submit(
                        	local.invite_to_chat,
                        	user_Id,
                        	chat_Id)]
                except Exception as e:
                      print(e)

 # invite recent users


def invite_recent_users():
    auth()
    local = samino.Local(communities())
    chat_Id = chats(local)
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        for i in range(0, 2000, 250):
            try:
            	recent_users = local.get_all_users(type="recent", start=i, size=100)
            	for nickname, user_Id in zip(
                    recent_users.nickname, recent_users.userId):
                    	print(f"{nickname} Invited to chat")
                    	_ = [
                    	executor.submit(
                    	local.invite_to_chat,
                        user_Id,
                        chat_Id)]
            except Exception as e:
                  print(e)

 # invite user followers


def invite_user_followers():
    auth()
    local = samino.Local(communities())
    chat_Id = chats(local)
    user_info = client.get_from_link(input("User Link >> "))
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        for i in range(0, 2000, 250):
            try:
            	user_followers = local.get_member_followers(userId=user_info.objectId, start=i, size=100)
            	for nickname, user_Id in zip(
                    user_followers.nickname, user_followers.userId):
                    	print(f"{nickname} Invited to chat")
                    	_ = [
                    	executor.submit(
                    	local.invite_to_thread,
                        user_Id,
                        chat_Id)]
            except Exception as e:
                    print(e)
