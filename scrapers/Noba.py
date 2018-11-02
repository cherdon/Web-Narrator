import util
from scrapers.base import BaseScraper
import requests
from bs4 import BeautifulSoup

class NobaScraper(BaseScraper):
    def scrape(self):
        try:
            html = requests.get(self.website).text
            soup = BeautifulSoup(html, 'html.parser')
            df = []
            headline = soup.find('h1').get_text()
            content = soup.find_all('p')
            for sentence in content:
                df.append(sentence.get_text())
            article = util.article(df, headline)
            return article
        except Exception as e:
            print(e)

website = "https://nobaproject.com/textbooks/new-textbook-4782ff3c-3de1-4700-a262-9cc372550395/modules/sensation-and-perception"
html = requests.get(website).text
soup = BeautifulSoup(html, 'html.parser')
df = []
headline = soup.find('h1').get_text()
print(headline)
content = soup.find_all('p')
for sentence in content:
    print(sentence)
    df.append(sentence.get_text())
