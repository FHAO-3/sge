from django.conf import settings
from django.core import serializers
# `serializers` tranforma uma `queryset` em json

from ai.prompts import SYSTEM_PROMPT, USER_PROMPT
from outflows.models import Outflow
from products.models import Product
from ai.models import AIResult

from openai import OpenAI
import json


class SGEAgent:
    def __init__(self):
        self.__client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

    def __get_data(self):
        products = Product.objects.all()
        outflow = Outflow.objects.all()
        return json.dumps({
            'products': serializers.serialize('json', products),
            'outflow': serializers.serialize('json', outflow),
            # `serialize` ele pode serializar para varios formatos tambem como por exemplo `xml, jsonl, python` que no caso é passado antes do que queremos serializar
        })
        # `json.dumps()` transfrma um `dict` em `str`

    def invoke(self):
        response = self.__client.responses.create(
            model=settings.OPENAI_MODEL,
            input=[
                {
                    'role': 'system',
                    'content': SYSTEM_PROMPT
                },
                {
                    'role': 'user',
                    'content': USER_PROMPT.replace('{{data}}', self.__get_data())
                },
            ],
        )
        result = response.output_text
        AIResult.objects.create(result=result)
        # salvando os dados na base de dados
