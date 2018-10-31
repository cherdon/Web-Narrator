from scraper import BaseScraper

def show_content(model, website):
    scraper = model(website)
    print(scraper.run())

if __name__ == "__main__":
    ex_website = "http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm"
    website = input("What website do you want to hear?")
    if website == "" or website == None:
        show_content(BaseScraper, ex_website)
    else:
        show_content(BaseScraper, website)