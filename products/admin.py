from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'title brand category description serie_number cost_price selling_price quantity created_at updated_at'.split(' ')