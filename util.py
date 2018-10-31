from scrapers.base import BaseScraper
from scrapers.STNews import STNews

scrapers_list = {
    "straitstimes": STNews
}

def get_source(website):
    website = website.strip("https://www")
    source = website.split(".")[1]
    return source

def get_scraper(source):
    if source in scrapers_list:
        scraper = scrapers_list[source]
    else:
        scraper = BaseScraper
    return scraper