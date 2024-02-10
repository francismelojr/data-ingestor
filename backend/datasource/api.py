from typing import List

import pandas as pd
import requests

from backend.contracts.schemas import GenericSchema


class APICollector:
    def __init__(self, schema):
        self._schema = schema
        self._aws = None
        self._buffer = None
        pass

    def start(self, param):
        response = self.getData(param)
        response = self.extractData(response)
        response = self.transformDf(response)
        return response

    def getData(self, param: int):
        if param > 0:
            response = requests.get(
                f'http://127.0.0.1:8000/gerarcompras/{param}'
            ).json()
            return response
        else:
            response = 'O parâmetro deve ser maior que 0!'
            return response

    def extractData(self, response):
        result: List[GenericSchema] = []
        for item in response:
            index = {}
            for key, value in self._schema.items():
                if type(item.get(key)) == value:
                    index[key] = item[key]
                else:
                    index[key] = None
            result.append(index)
        return result

    def transformDf(self, response):
        result = pd.DataFrame(response)
        return result
