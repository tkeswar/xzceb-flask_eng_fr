import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
print (apikey)
print (url)
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
    #write the code here
    return frenchText


def frenchToEnglish(frenchText):
    #write the code here
    return englishText

translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-fr').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))
