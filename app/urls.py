from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    # Como essa view `auth_view.LoginView` ja vem pronta ela tem uma tela de login padrão
    # Mas em `./app/settings.py` colocamos que todos os templates vão estar em `'DIRS': ['app/templates'],` então ao tentar
    # acessar a `url/login/` via dar erro pois o template padrão de login nao está no diretorio criado porm nos

    path('', views.home, name='home'),
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('suppliers.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
    path('', include('products.urls')),
]
