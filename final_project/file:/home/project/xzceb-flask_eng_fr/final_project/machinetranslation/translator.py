"""This module contains functions for language translation."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def english_to_french(english_text):
    """
    Translates the given english text to french.
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)

    translation_response = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    french_text = translation_response['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translates the given french text to english.
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)

    translation_response = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()

    english_text = translation_response['translations'][0]['translation']
    return english_text
