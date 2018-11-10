from selenium import webdriver
from scrapers.base import BaseScraper
from scrapers.STNews import STNewsScraper
from scrapers.Noba import NobaScraper

scrapers_list = {
    "straitstimes": STNewsScraper,
    "nobaproject": NobaScraper
}

def get_source(website):
    website = website.strip("https://www.")
    source = website.split(".")[0]
    return source

def get_scraper(source):
    if source in scrapers_list:
        scraper = scrapers_list[source]
    else:
        scraper = BaseScraper
    return scraper

class article:
    def __init__(self, content, headline=None, author=None, introduction=None, conclusion=None):
        self.headline = headline
        self.content = content
        self.author = author
        self.intro = introduction
        self.conclusion = conclusion

def init_driver(chromepath):
    options = webdriver.ChromeOptions()
    options.add_argument('chrome_headless')
    options.add_argument('window-size=1200x2400')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(executable_path=chromepath, chrome_options=options)
    return driver
