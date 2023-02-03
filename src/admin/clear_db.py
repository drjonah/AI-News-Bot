import json

def clear_all_users():
    try:
        default = {"users": {"admin": {"password": "123"}}}
        users_file_write = open('./db/users.json', 'w')
        json.dump(default, users_file_write)

        print("> User database has been clear :(")
    except:
        print("> Error clearing user database!")

clear_all_users()