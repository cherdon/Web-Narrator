from scrapers.base import BaseScraper
import requests
from bs4 import BeautifulSoup

class STNews(BaseScraper):
    def scrape(self):
        try:
            html = requests.get(self.website).text
            soup = BeautifulSoup(html, 'html.parser')
            df = []
            headline = soup.find('h1', class_='headline').get_text()
            df.append(headline)
            content = soup.find('div', class_='odd field-item').find_all('p')
            for sentence in content:
                df.append(sentence.get_text())
            return df
        except Exception as e:
            print(e)