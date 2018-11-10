import util
from scrapers.base import BaseScraper
from bs4 import BeautifulSoup

class NobaScraper(BaseScraper):
    def scrape(self):
        try:
            self.driver.get(self.website)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            df = []
            headline = soup.find('h1').get_text()
            for elm in soup.select('p'):
                try:
                    if  "text-muted" in elm['class']:
                        continue
                except:
                    df.append(elm.get_text())
            article = util.article(df, headline)
            return article
        except Exception as e:
            print(e)

