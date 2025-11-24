import time
import module_api
from abc import ABC
from abc import abstractmethod

class retry_wrapper(ABC):
    def __init__(self, module, tries, delay):
        self.module = module
        self.retry_maximum = tries
        self.retry_delay= delay

    @abstractmethod
    def retry_call_api(self, headers): 
        pass

class retry_recipes(retry_wrapper):
    def __init__(self, module, tries, delay):
        super().__init__(module, tries, delay)

    def retry_call_api(self, headers):
        attempt = 0
        response = 0

        while attempt < self.retry_maximum:
            time.sleep(self.retry_delay * attempt)
            response = self.module.call_api(headers + attempt)  # suma attempt simulando el posible cambio
            attempt += 1

            if response == 200:
                print(f"Success code {response}")
                return
            elif response == 400:  # no se reintenta si esperar no va a cambiar nada
                print(f"Cancel retry: code {response}")
                return
            else:
                print(f"Retry after delay: code {response}")

        print(f"Cancel retry: maximum attempts reached")
    


            

