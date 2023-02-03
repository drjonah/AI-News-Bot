import json

users_file = open('./db/users.json')
users = json.load(users_file)

def create_user() -> tuple:

    username = input("> Username: ").lower()

    if username in users['users']:
        print(f"> Username \"{username}\" is taken! Please provide a new one.")
        return (False, None)

    password = input("> Password: ")

    try:
        users['users'][username.lower()] = {"password": password}
        users_file_write = open('./db/users.json', 'w')
        json.dump(users, users_file_write)

        print(f"> Welcome {username}! You have been added to the database!")

        return (True, username)
    except:
        print("> Error creating user! Try again")
        return (False, None)

def login_user():
    pass

def logout_user():
    pass

def change_user_password():
    pass