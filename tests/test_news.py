# changes the path to access src
import os
import sys

project_path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
src_path = os.path.join(project_path, "src")
sys.path.append(src_path)

# modules to test
import modules
from pprint import pprint

def test_article_attributes(articles, amount):

    articles_read = 0

    for value in articles.values():
        for article in value:
            if articles_read == amount: break

            print("\n")
            print(article["headline"])
            print(article["subline"])
            print(article["author"])
            print(article["date"])
            print(article["category"])
            print(article["url"])
            print("\n")

            articles_read += 1

def main():
    fox = modules.Fox()

    print("fetching articles...")
    fox.get_articles()

    articles = fox.news_articles
    amount = fox.number_of_articles

    print("number: ", amount)
    test_article_attributes(articles, 5)

if __name__ == "__main__":
    main()