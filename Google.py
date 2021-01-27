"""Translates text into the target language.

Target must be an ISO 639-1 language code.
See https://g.co/cloud/translate/v2/translate-reference#supported_languages
"""
import json
from typing import List

import requests
from requests import Response

from Settings import Google_Token


class Google:
    def __init__(self):
        self.__url: str = "https://translation.googleapis.com/language/translate/v2"
        self.__token: str = Google_Token

    def translate(self, source: List[str], lang: str) -> str:
        payload = {
            "q": source,
            "format": "text",
            "source": lang,
            "key": self.__token,
        }

        if lang == "zh":
            payload.setdefault("target", "en")
        else:
            payload.setdefault("target", "zh")

        response: Response = requests.get(self.__url, params=payload)
        return json.loads(response.text).get("data").get("translations")[0].get("translatedText")
