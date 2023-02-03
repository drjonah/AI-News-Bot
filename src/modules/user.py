import json

users_file = open('./db/users.json')
users = json.load(users_file)

def create_user() -> tuple:

    username = input("> Username: ").lower()
    if username in users['users']:
        print(f"Username \"{username}\" is taken! Please provide a new one.")
        return (False, None)

    password = input("> Password: ")

    try:
        users['users'][username] = {"password": password}
        users_file_write = open('./db/users.json', 'w')
        json.dump(users, users_file_write)

        print(f"Welcome {username}! You have been added to the database!")
        return (True, username)
    except:
        print("Error creating user! Try again")
        return (False, None)

def login_user() -> tuple:
    
    username = input("> Username: ").lower()
    if username not in users['users']:
        print(f"Username \"{username}\" does not exist! Please provide a new one.")
        return (False, None)

    password = input("> Password: ")

    try:
        if users['users'][username]["password"] == password:
            print(f"Welcome {username}!")
            return (True, username)
        else:
            print(f"Incorrect password for {username}")
            return (False, None)
    except:
        print("Error logging in! Try again")
        return (False, None)

def change_user_password(username: str):

    new_password = input("> New Password: ")
    if input("> Confirm Password: ") == new_password:

        try:
            users['users'][username] = {"password": new_password}
            users_file_write = open('./db/users.json', 'w')
            json.dump(users, users_file_write)

            print("Password successfully changed!")
            return True
        except:
            print("Error saving your new password!")
            return False
    else:
        print("Your passwords do not match!")
        return False