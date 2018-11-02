import util
from gtts import gTTS
import winsound


# generate an article based on the scraper and website given
def fill_article_class(model, website):
    scraper = model(website)
    article = scraper.run()
    return article

# join a list of text by using spaces
def join_text(text_list):
    text = ' '.join(text_list)
    return text

# generate speech/text content with article attributes
def generate_content(article):
    final_text = ""
    try:
        final_text += article.headline + ". "
    except:
        pass
    content = join_text(article.content)
    final_text += content
    return final_text

# generate audio object
def get_audio(model, website, language='en'):
    article = fill_article_class(model, website)
    text = generate_content(article)
    speech_obj = gTTS(text=text, lang=language, slow=False)
    return speech_obj


def main():
    website = "https://nobaproject.com/textbooks/new-textbook-4782ff3c-3de1-4700-a262-9cc372550395/modules/sensation-and-perception"

    # find out the source of the website and if it has a specific scraper for it
    source = util.get_source(website)
    print(source)
    scraper = util.get_scraper(source)

    # create article attributes based on the content scraped
    article = fill_article_class(scraper, website)
    print(generate_content(article))

    # # parse to get the audio version
    # audio = get_audio(scraper, website, 'en')
    # audio.save('test.mp3')
    #
    # winsound.PlaySound('test.mp3', winsound.SND_FILENAME | winsound.SND_ASYNC)

if __name__ == "__main__":
    main()