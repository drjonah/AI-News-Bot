class Promt:
    def __init__(self) -> None:
        self.not_authenticated = "Actions\n- 1/login: log into an account\n- 2/create: create a new account"
        self.landing = "Actions\n- 1/news: access news module\n- 2/stocks: access stocks module\n- 3/change: change account password\n- 4/logout: logout of user\n- 5/quit: exit application"
        self.news = "Actions\n- 1/read [fox/cnn/all]: read articles 1 by 1"
        self.news_read = "Actions\n- 1/next: read next article"