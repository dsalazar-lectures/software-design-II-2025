import time
from abc import ABC
from abc import abstractmethod

class module(ABC):
    def __init__(self, url):
        self.api_url = url

    @abstractmethod
    def call_api(self, headers): 
        pass

class module_recipes(module):
    def __init__(self, url):
        super().__init__(url)
        self.call = 0

    def call_api(self, headers):
        if headers <= 0:
            return 408  # timeout
        elif headers == 1:
            return 200  # ok
        elif headers == 2:
            return 505  # internal server error
        else:
            return 400  # bad request

