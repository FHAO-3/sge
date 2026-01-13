# importante lembrar que ess arquivo é um client que tem as rotas para o webhook
import requests


class Notify:

    def __init__(self):
        self.__base_url = 'https://webhook.site'

    def send_event(self, data):
        requests.post(
            url=f'{self.__base_url}/35648e9a-b03d-4486-ba3d-0c3d8307abda',
            # esse é o link que o site webhook que gerou para fazermos testes
            data=data,
        )
        # return response.json() não tem necessidade de enviar nenhum return pois o webhook não quer saber se deu erro ou não se a requisição der errada não tem o que fazer
        print(type(data))
        print(f'{self.__base_url}/35648e9a-b03d-4486-ba3d-0c3d8307abda')
