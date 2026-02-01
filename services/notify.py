# importante lembrar que ess arquivo é um client que tem as rotas para o webhook
import requests


class Notify:

    def __init__(self):
        self.__base_url = 'http://localhost:8001'

    def send_order_event(self, data):
        requests.post(
            url=f'{self.__base_url}/api/v1/webhooks/order',
            # esse é o link que o site webhook que gerou para fazermos testes
            json=data,
            # qunado vamos fazer um post não passamos `data` como parametro passamos `json`
        )
        # return response.json() não tem necessidade de enviar nenhum return pois o webhook não quer saber se deu erro ou não se a requisição der errada não tem o que fazer
