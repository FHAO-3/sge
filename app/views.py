from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import metrics
from ai.models import AIResult
import json


# vamos lembrar que quando passamos so o nome igual no caso do `login_url` e o `name` que colcamos em URLs
@login_required(login_url='login')
def home(request):
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_data()
    graphic_product_category_metric = metrics.get_graphic_product_category_metric()
    graphic_product_brand_metric = metrics.get_graphic_product_brand_metric()
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    ai_result = AIResult.objects.first().result
    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
        'product_count_by_category': json.dumps(graphic_product_category_metric),
        'product_count_by_brand': json.dumps(graphic_product_brand_metric),
        'ai_result': ai_result,
    }
    return render(request, 'home.html', context)
