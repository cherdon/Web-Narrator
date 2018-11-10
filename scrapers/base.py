import util
from bs4 import BeautifulSoup

class BaseScraper:
    def __init__(self, website, driver):
        self.website = website
        self.driver = driver

    def run(self):
        return self.scrape()

    def scrape(self):
        try:
            self.driver.get(self.website)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            df = []
            for sentence in soup.find_all('p'):
                df.append(sentence.get_text())
            article = util.article(df)
            return article

        except Exception as e:
            return e