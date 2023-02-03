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
        pass
    elif prompt == "logout":
        pass
    elif prompt == "change":
        pass
    else:
        print("> Invalid request!")

def main():
    while not AUTHENTICATED:
        prompt = input("> Command: ")
        manage_user(prompt)


if __name__ == "__main__":
    main()