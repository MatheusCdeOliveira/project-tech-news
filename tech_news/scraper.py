import requests
import time
# Requisito 1


def fetch(url):
    user_agent = {"user-agent": "Fake user-agent"}
    try:
        data = requests.get(url, headers=user_agent, timeout=3)
        time.sleep(1)
        if data.status_code != 200:
            return None
        return data.text
    except requests.ReadTimeout:
        return None

    """Seu código deve vir aqui"""


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
