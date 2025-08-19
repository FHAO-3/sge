from django.utils.formats import number_format
from django.db.models import Sum
from products.models import Product
from outflows.models import Outflow


def get_product_metrics():
    products = Product.objects.all()
    total_cost_price = sum(product.cost_price * product.quantity for product in products)
    total_selling_price = sum(product.selling_price * product.quantity for product in products)
    total_quantity = sum(product.quantity for product in products)
    total_profit = total_selling_price - total_cost_price
    return dict(
        total_cost_price=number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        total_selling_price=number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        total_quantity=total_quantity,
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
    )
    # essa função `number_format` formata o valor para dinheiro
    # primeiro parametro `value` é o valor que vamos formatar
    # segundo parametro `decimal_pos` numero de casas decimais apos a virgula
    # terceiro parametro `force_grouping` com o valor `True` é para evitar de agrupar as casas decimais


def get_sales_metrics():
    total_sales = Outflow.objects.count()
    total_products_solde = Outflow.objects.aggregate(
        total_products_solde=Sum('quantity')  # `Sum` do django
    )['total_products_solde'] or 0
    # o `aaggregate` é como se adiciona-se dados calculados na `query`
    total_sales_value = sum(outflow.quantity * outflow.product.selling_price for outflow in Outflow.objects.all())
    total_sales_cost = sum(outflow.quantity * outflow.product.cost_price for outflow in Outflow.objects.all())
    total_sales_profit = total_sales_value - total_sales_cost
    return dict(
        total_sales=number_format(total_sales),
        total_products_solde=number_format(total_products_solde, decimal_pos=2, force_grouping=True),
        total_seles_value=number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        total_sales_profit=number_format(total_sales_profit, decimal_pos=2, force_grouping=True)
    )