from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=models.Inflow)
def update_product_quantity(sender, instance, created, **kwargs):
    '''
    `sender` == models.Inflow (default)
    `instance` == data from inflows (default)
    `created` == boolean (se estiver uma entrada de dado vai ser igual a `True`, se for consertando algum dado no cadastro vai ser `False`) (default)
    Por padrão quando vamos criar um `update` de `Signals` vamos passar sempre esses parametro por padrão
    '''
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity += instance.quantity
            product.save()