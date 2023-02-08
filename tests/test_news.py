# path
import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "src"
)
sys.path.append(SOURCE_PATH)

import modules

def test_article_attributes(article, amount):

    for i in range(amount):
        print("\n")
        print(article[i]["headline"])
        print(article[i]["subline"])
        print(article[i]["author"])
        print(article[i]["date"])
        print(article[i]["category"])
        print(article[i]["url"])
        print("\n")

def main():
    fox = modules.Fox()
    fox.get_articles()

    articles = fox.news_articles

    test_article_attributes(articles, 5)

if __name__ == "__main__":
    main()