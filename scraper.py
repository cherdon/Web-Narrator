import requests
from bs4 import BeautifulSoup

class BaseScraper:
    def __init__(self, website):
        self.website = website

    def run(self):
        return self.scrape()

    def scrape(self):
        try:
            html = requests.get(self.website).content
            soup = BeautifulSoup(html, 'html.parser')
            df = []
            for sentence in soup.find_all('p'):
                df.append(sentence.get_text())
            return df

        except Exception as e:
            return e