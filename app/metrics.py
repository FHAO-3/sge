from django.db.models import Sum, F
from django.utils import timezone
from django.utils.formats import number_format
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


def get_daily_sales_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    # lista de datas que é o dia de hoje mais 6 dias atras
    values = list()

    for date in dates:
        sales_total = Outflow.objects.filter(
            created_at__date=date  # buscando via ORM qual foi o némero de `vendas` do dia
        ).aggregate(  # vamos realizar um calculo por isso usamos o `aggregate` como uma `subquery` calculada
            total_sales=Sum(F('product__selling_price') * F('quantity'))  # `F` Ele serve para referenciar o valor de um campo diretamente no banco de dados
        )['total_sales'] or 0

        values.append(float(sales_total))

    return dict(
        dates=dates,
        values=values,
    )


def daily_sales_quantity_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    # lista de datas que é o dia de hoje mais 6 dias atras
    quantities = list()

    for date in dates:
        sales_quantities = Outflow.objects.filter(
            created_at__date=date
        ).count()
        # acima estamos pegando a qunatitdade de vendas
        quantities.append(sales_quantities)

    return dict(
        dates=dates,
        values=quantities,
    )