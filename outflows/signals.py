from django.db.models.signals import post_save
from django.dispatch import receiver

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
        'product': instance.product,
        'quantity': instance.quantity,
    }
    notify.send_event(data)
    print('>> saida')
