import requests


class APICollector:
    def __init__(self):
        self._schema = None
        self._aws = None
        self._buffer = None
        pass

    def start(self):
        pass

    def getData(self, param: int):
        if param > 1:
            response = requests.get(
                f'http://127.0.0.1:8000/gerarcompras/{param}'
            ).json()
            return response
        else:
            response = requests.get(
                'http://127.0.0.1:8000/gerarcompras'
            ).json()
            return response

    def extractData(self):
        pass

    def transformDf(self):
        pass
