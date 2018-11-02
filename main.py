import util
from gtts import gTTS
import winsound


def site_content(model, website):
    scraper = model(website)
    text_list = scraper.run()
    return text_list

def join_text(text_list):
    text = '. '.join(text_list)
    return text

def get_audio(model, website, language='en'):
    text_list = site_content(model, website)
    text = join_text(text_list)
    speech_obj = gTTS(text=text, lang=language, slow=False)
    return speech_obj

def main():
    website = ""
    source = util.get_source(website)
    scraper = util.get_scraper(source)

    # parse to get the audio version
    audio = get_audio(scraper, website, 'en')
    audio.save('test.mp3')

    winsound.PlaySound('test.mp3', winsound.SND_FILENAME | winsound.SND_ASYNC)

if __name__ == "__main__":
    main()