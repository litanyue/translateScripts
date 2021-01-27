import json
from typing import List

import requests
from requests import Response

from Settings import CaiYun_Token


class CaiYun:
    def __init__(self):
        self.__url: str = "https://api.interpreter.caiyunai.com/v1/translator"
        self.__token: str = CaiYun_Token
        self.__headers = {
            'content-type': "application/json",
            'x-authorization': "token " + self.__token,
        }

    def translate(self, source: List[str], direction: str) -> str:
        detect = False
        if direction == "en":
            direction += "2zh"
        elif direction == "zh":
            direction += "2en"
        else:
            direction = "auto2zh"
            detect = True

        payload = {
            "source": source,
            "trans_type": direction,
            "request_id": "demo",
            "detect": detect,
        }

        response: Response = requests.request("POST", self.__url, data=json.dumps(payload), headers=self.__headers)

        return json.loads(response.text)['target'][0]
