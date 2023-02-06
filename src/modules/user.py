import json

class User:
    def __init__(self) -> None:
        # file
        self.users_file = open('./db/users.json')
        self.users = json.load(self.users_file)
        # user
        self.username = ""
        self.password = ""
        self.is_authenticated = False

    def create_user(self) -> bool:

        username = input("> Username: ").lower().strip()
        if username in self.users['users']:
            return None

        password = input("> Password: ").strip()

        try:
            self.users['users'][username] = {
                "password": password,
                "news": {},
                "stocks": {}
            }
            users_file_write = open('./db/users.json', 'w')
            json.dump(self.users, users_file_write)

            self.username = username
            self.password = password
            self.is_authenticated = True

            return True
        except:
            print("Error creating user! Try again")
            return False

    def login_user(self) -> bool:
        
        username = input("> Username: ").lower().strip()
        if username not in self.users['users']:
            return None

        password = input("> Password: ").strip()

        try:
            if self.users['users'][username]["password"] == password:
                self.username = username
                self.password = password
                self.is_authenticated = True
                return True
            else:
                return False
        except:
            return False

    def change_user_password(self):

        new_password = input("> New Password: ").strip()
        if input("> Confirm Password: ").strip() == new_password:

            try:
                self.users['users'][self.username] = {"password": new_password}
                users_file_write = open('./db/users.json', 'w')
                json.dump(self.users, users_file_write)

                self.password = new_password

                return True
            except:
                return None
        else:
            return False