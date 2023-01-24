import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
    #write the code here
    #function to translate the input english string to french
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    frenchText=translation['translations'][0]['translation']
    return frenchText


def frenchToEnglish(frenchText):
    #write the code here
    #function to translate the input french string to english
    translation = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    return englishText



