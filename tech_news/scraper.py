import requests
import time
import re
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
    if content:
        return content
    else:
        return None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    reading_time = selector.css(".meta-reading-time::text").get()
    response = {
        "url": selector.xpath("//link[@rel='canonical']/@href").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".post-meta .meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "reading_time": int(re.findall("\d+", reading_time)[0]),
        "summary": selector.xpath(
            "string(//div[@class='entry-content']/p[position()=1])"
        )
        .get()
        .strip(),
        "category": selector.css(".label::text").get(),
    }
    return response


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
