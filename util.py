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
