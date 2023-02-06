import pyfiglet # ascii
import time # time 
import modules # app modules

USER = modules.User()
NEWS_AI_ASCII = pyfiglet.figlet_format("News AI")

def manage_user(prompt: str) -> True:
    global USER
    
    # create a new user
    if prompt == "create":
        status = USER.create_user()
        if status == None:
            print(f"Username is taken. Please provide a new one.")
        elif status:
            print(f"Welcome {USER.username}. You have been added to the database.")
        else:
            print("Error creating user. Try again")
    # login to existing user
    elif prompt == "login":
        status = USER.login_user()
        if status == None:
            print(f"Username does not exist. Please provide a new one.")
        elif status:
            print(f"Welcome {USER.username}.")
        else:
            print(f"Error logging in. Double check the password.")
    # change password
    elif prompt == "change":
        status = USER.change_user_password()
        if status == None:
            print("Error saving your new password.")
        elif status:
            print("Password successfully changed.")
        else:
            print("Your passwords do not match.")
    # logout
    elif prompt == "logout":
        USER.is_authenticated = False
        USER = modules.User()
        print("You have been logged out.")
    else:
        print("> Invalid request.")

def main():
    global USER

    print(NEWS_AI_ASCII)

    app_run = True
    while app_run:

        while not USER.is_authenticated:
            
            prompt = input("> Command (Not Authenticated): ")
            if prompt == "quit":
                return

            manage_user(prompt)

        prompt = input(f"> Command ({USER.username}): ").lower()
        if prompt == "logout" or prompt == "change":
            manage_user(prompt)

        if prompt == "quit":
            return

if __name__ == "__main__":
    main()
    
    print(f"\nGoodbye.")
    time.sleep(2)