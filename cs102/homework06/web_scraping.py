import requests
from typing import List, Dict
from db import *
from bs4 import BeautifulSoup

def extract_news(parser: BeautifulSoup) -> List[Dict]:
    """
    Extract news from a given web page
    :param parser: BeautifulSoup object
    :return: news array
    """
    news_list = []

    titles = parser.findAll('tr', attrs={'class': 'athing'})
    subtexts = parser.findAll('td', attrs={'class': 'subtext'})

    for i in range(len(titles)):
        a = titles[i].findAll('td', attrs={'class': 'title'})[1].find('a')
        title = a.get_text()
        url = a['href']
        author = subtexts[i].find('a', attrs={'class': 'hnuser'})

        if author:
            author = author.get_text()

        comments = subtexts[i].findAll('a')[-1].get_text()
        if 'comments' in comments:
            comments = comments.split("\xa0")[0]
        else:
            comments = 0

        points = subtexts[i].find('span', attrs={'class': 'score'})
        if points:
            points = points.get_text()

        news_list.append({
            'author': author,
            'comments': comments,
            'points': points,
            'title': title,
            'url': url
        })

    return news_list


def extract_next_page(parser: BeautifulSoup) -> str:
    """
    Extract next page URL
    :param parser: BeautifulSoup object
    :return: next page URL or empty string
    """
    more_link = parser.find('a', attrs={'class': 'morelink'})
    return "" if not more_link else more_link['href']


def get_news(url: str, n_pages: int = 1) -> List[Dict]:
    """
    Collect news from a given web page
    :param url: web url
    :param n_pages: number of pages
    :return: array with news
    """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news