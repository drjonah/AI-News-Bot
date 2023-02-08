import requests
from bs4 import BeautifulSoup as bs

class Fox:
    def __init__(self) -> None:
        self.homepage = "https://www.foxnews.com/"
        self.news_articles = []

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

            article_headline = bs_parser.find('h1', {'class' : 'headline'}).text.strip()
            article_subline = bs_parser.find('h2', {'class' : 'sub-headline speakable'}).text.strip()
            article_author = bs_parser.find('div', {'class' : 'author-byline'}).find("a").text.strip()
            article_date = bs_parser.find('div', {'class' : 'article-date'}).time.text.strip()
            article_category = bs_parser.find('div', {'class' : 'eyebrow'}).text.strip()
            
            return (article_headline, article_subline, article_author, article_date, article_category)
        else:
            return None

    def parse_homepage(self, homepage_content: str) -> list:
        """This function will scrape all articles availble on Fox New's homepage

        Args:
            homepage_content (str): This is all of the html that makes up Fox New's homepage at the given time

        Returns:
            list: The list is a list of dictionaries which include atributes of an article (ref scrape_article())
        """
        news_articles = []

        bs_parser = bs(homepage_content, 'html.parser')
        articles = set(bs_parser.find_all("article", {"class": lambda x: x and "article story" in x.split("-")}))

        for article in articles:
            try:
                article_url = article.find("div", {"class": "m"}).find("a")["href"].strip()
                article_headline, article_subline, article_author, article_date, article_category = self.scrape_article(article_url)

                news_articles.append({
                    "headline": article_headline,
                    "subline": article_subline,
                    "author": article_author,
                    "date": article_date,
                    "category": article_category,
                    "url": article_url
                })
                
            except:
                pass
        
        return news_articles

    def get_articles(self) -> bool:
        """ The function gets all articles and their attributes of Fox's homepage and stores them 

        Returns:
            bool: True indicates scraping was successful else False
        """
        r = requests.get(self.homepage)

        if r.status_code == 200:
            try:
                homepage_content = r.text
                self.news_articles += self.parse_homepage(homepage_content)

                return True
            except:
                return False
        else:
            return False