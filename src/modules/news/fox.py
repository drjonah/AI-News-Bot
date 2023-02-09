import requests # requests
from bs4 import BeautifulSoup as bs # scraper
from datetime import datetime # dates
from tqdm import tqdm # progress bar

class Fox:
    def __init__(self) -> None:
        self.homepage = "https://www.foxnews.com/"
        self.news_articles = {}
        self.number_of_articles = 0

    def add_article(self, article_category: str, article_details: tuple, location: int) -> None:
        """This function appends the article to its category in a specified location

        Args:
            article_category (str): Category to store the article
            article_details (tuple): Contains article details
            location (int): Index where the article will be stored
        """
        self.news_articles[article_category].insert(location, {
            "headline": article_details[0],
            "subline": article_details[1],
            "author": article_details[2],
            "date": article_details[3],
            "category": article_details[4],
            "url": article_details[5]
        })

    def sort_articles(self, article_details: tuple) -> None:
        """This function takes article details and sorts them into a dictionary by category

        Args:
            article_details (tuple): This contains a tuple of an article's attributes
        """
        article_date = article_details[3]
        article_category = article_details[4]

        # add category if not avalable
        if article_category not in self.news_articles.keys():
            self.news_articles[article_category] = list()
            self.add_article(article_category, article_details, 0)
            return

        # sorts by date
        article_datetime = datetime(*article_date[3])
        for location, article in enumerate(self.news_articles[article_category]):
            article_datetime_compare = datetime(*article["date"])

            if article_datetime <= article_datetime_compare:
                self.add_article(article_category, article_details, location)
                return

        # oldest article, goes to the end
        self.add_article(article_category, article_details, len(self.news_articles[article_category]))

    def scrape_article(self, article_url: str) -> tuple:
        """This function goes to an articles URL and scrapes attributes of it

        Args:
            article_url (str): This is the URL of an article

        Returns:
            tuple: returns a tuple including the articles headline, subline, author, and date written
        """
        r = requests.get(article_url)

        if r.status_code == 200:
            bs_parser = bs(r.text, 'html.parser')

            # scrapes all of an article's attributes
            article_headline = bs_parser.find('h1', {'class' : 'headline'}).text.strip()
            article_subline = bs_parser.find('h2', {'class' : 'sub-headline speakable'}).text.strip()
            article_author = bs_parser.find('div', {'class' : 'author-byline'}).find("a").text.strip()
            article_date = bs_parser.find('div', {'class' : 'article-date'}).time.text.strip()

            # converts date to an object using datetime
            month, day, year, time = article_date.replace(",", "").split(" ")[0:-1] # splits each part
            month = datetime.strptime(month, '%B').month # uses datetime to convert month to number
            hour, minute = list(map(int, time[0:-2].split(":"))) # gets hour and minute and converts to int
            if time[-2:] == "pm": hour += 12 # adjusts for pm
            article_date = [int(year), month, int(day), hour, minute] # creates a time list

            article_category = bs_parser.find('div', {'class' : 'eyebrow'}).text.strip()
            
            return (article_headline, article_subline, article_author, article_date, article_category, article_url)
        else:
            return None

    def parse_homepage(self, homepage_content: str) -> None:
        """This function will scrape all articles availble on Fox New's homepage

        Args:
            homepage_content (str): This is all of the html that makes up Fox New's homepage at the given time
        """

        # finds all article classes that exist on the homepage
        bs_parser = bs(homepage_content, 'html.parser')
        articles = set(bs_parser.find_all("article", {"class": lambda x: x and "article story" in x.split("-")}))

        print("Fetching recent articles from Fox New's...")
        for article in tqdm(articles, bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):
            try:
                # scrapes the article's URL from each artile class
                article_url = article.find("div", {"class": "m"}).find("a")["href"].strip()
                article_details = self.scrape_article(article_url)

                self.sort_articles(article_details)
                self.number_of_articles += 1
            except:
                pass

    def get_articles(self) -> bool:
        """ The function gets all articles and their attributes of Fox's homepage and stores them 

        Returns:
            bool: True indicates scraping was successful else False
        """
        r = requests.get(self.homepage)

        if r.status_code == 200:
            homepage_content = r.text
            self.parse_homepage(homepage_content)

            # fetching and storing articles on the homepage is a success
            return True
        else:
            return False