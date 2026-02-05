from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import datetime

from . import models

from services.notify import Notify
# por mais que o client nao tenha nada ver com o django aqui estamos importando para dentro do django entao `importamos` de modo padrão django


# o `receiver` fica escultando para saber quando execltar
@receiver(post_save, sender=models.Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    '''
    `sender` == models.Outflow (default)
    `instance` == data from Outflows (default)
    `created` == boolean (se estiver uma entrada de dado vai ser igual a `True`, se for consertando algum dado no cadastro vai ser `False`) (default)
    Por padrão quando vamos criar um `update` de `Signals` vamos passar sempre esses parametro por padrão
    '''
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()


@receiver(post_save, sender=models.Outflow)
def send_outflow_event(sender, instance, created, **kwargs):
    '''
    Deixamos essa funcão a ser execultada dentro de um `try` para evitar de quebrar o projeto sge pois vamos lebrar que essa função é usada para levar informacoes para fora deste projeto e por esse motivo caso for dear algum erro não é para execultar nada
    '''
    try:
        if created:
            notify = Notify()
            data = {
                'event_type': 'create_outflow',
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'product': instance.product.title,
                'product_cost_price': float(instance.product.cost_price),
                'product_selling_price': float(instance.product.selling_price),
                'quantity': instance.quantity,
                'description': instance.description
            }
            notify.send_order_event(data)
    except:
        # caso de algum erro somente ignorar
        pass
