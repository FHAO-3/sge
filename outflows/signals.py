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
def send_outflow_event(sender, instance, **kwargs):
    notify = Notify()
    data = {
        'event_type': 'create_outflow',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'product': str(instance.product),
        # colocado como uma string pois o product é um objeto e nao é possivel parsear quando fazemos um `post`
        'quantity': instance.quantity,
    }
    notify.send_event(data)
