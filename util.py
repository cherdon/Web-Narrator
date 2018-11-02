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


# format of update
# {'update_id': 211750268, 'message': {'message_id': 2, 'from': {'id': 99456745, 'is_bot': False, 'first_name': 'Cher Don 🐶', 'username': 'Cherdon', 'language_code': 'en-US'}, 'chat': {'id': 99456745, 'first_name': 'Cher Don 🐶', 'username': 'Cherdon', 'type': 'private'}, 'date': 1541048109, 'text': 'Hello!'}}
