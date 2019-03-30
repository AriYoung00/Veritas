from bs4 import BeautifulSoup


def has_schema(soup: BeautifulSoup):
    attrs = soup.find("html").attrs
    try:
        return attrs['itemType'] == "http://schema.org/NewsArticle" or attrs['itemType'] == "http://schema.org/Article"
    except KeyError:
        return False
    