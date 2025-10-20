from retry_wrapper import *
from module_api import *


if __name__ == "__main__":
    
    url_servicio = "sampletext"
    modulo_recetas = module_recipes(url_servicio)
    intentos = 3
    intervalo_seg = 2
    wrapper_retry_modulo_recetas = retry_recipes(modulo_recetas, intentos, intervalo_seg)

    wrapper_retry_modulo_recetas.retry_call_api(0)
    wrapper_retry_modulo_recetas.retry_call_api(2)
    wrapper_retry_modulo_recetas.retry_call_api(-5)