"""
This module provides functions to translate text from french to english and vice-versa.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates the english input text to french.

    Args:
        english_text (str): The english text to translate.

    Returns:
        str: The translated text in french.
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates the french input text to english.

    Args:
        french_text (str): The french text to translate.

    Returns:
        str: The translated text in english.
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
