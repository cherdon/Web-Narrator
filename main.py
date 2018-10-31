from util import get_source, get_scraper
from gtts import gTTS
import winsound

def site_content(model, website):
    scraper = model(website)
    text_list = scraper.run()
    return text_list

def get_text(text_list):
    text = '. '.join(text_list)
    return text

def get_audio(model, website, language='en'):
    text_list = site_content(model, website)
    text = get_text(text_list)
    speech_obj = gTTS(text=text, lang=language, slow=False)
    return speech_obj

if __name__ == "__main__":
    website = input("What website do you want to hear?\n")
    print("The source is from: " + source)
    scraper = get_scraper(get_source(website))
    audio = get_audio(scraper, website)
    audio.save("test.mp3")

    winsound.PlaySound('test.mp3', winsound.SND_FILENAME | winsound.SND_ASYNC)