# Imports the Google Cloud client library
from google.cloud import translate

def run_quickstart():

   # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = 'My Test'

    # The target language
    target = 'ja'

    # Translates input text to Japanese
    translation = translate_client.translate(
        text, target_language=target)

    # Print the translated text
    trans_txt = str(translation['translatedText'])
    print('Translated text')
    print(translation['translatedText'])

    #return trans_txt


run_quickstart()
