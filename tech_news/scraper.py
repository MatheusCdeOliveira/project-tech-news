import requests
import time
from parsel import Selector

# Requisito 1


def fetch(url):
    user_agent = {"user-agent": "Fake user-agent"}
    try:
        data = requests.get(url, headers=user_agent, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None

    if data.status_code != 200:
        return None
    return data.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    content = selector.css(".entry-header h2 a::attr(href)").getall()
    if content:
        return content
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    content = selector.css(".next.page-numbers::attr(href)").get()
    print(type(content))
    if content == "":
        return None
    else:
        return content


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
