import modules

AUTHENTICATED = False
USER = ""

def manage_user(prompt: str) -> True:
    global AUTHENTICATED, USER

    if prompt == "create":
        status, username = modules.create_user()
        if status:
            AUTHENTICATED = True
            USER = username
    elif prompt == "login":
        status, username = modules.login_user()
        if status:
            AUTHENTICATED = True
            USER = username
    elif prompt == "change":
        status = modules.change_user_password()
        if status:
            AUTHENTICATED = True
    else:
        print("> Invalid request!")

def main():
    global AUTHENTICATED, USER

    app_run = True
    while app_run:

        while not AUTHENTICATED:
            prompt = input("> Command: ")
            manage_user(prompt)

        prompt = input(f"> Command ({USER}): ")
        if prompt == "logout":
            AUTHENTICATED = False
            USER = ""


if __name__ == "__main__":
    main()