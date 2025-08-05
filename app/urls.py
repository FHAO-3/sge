from django.contrib import admin
from django.urls import path

from django.shortcuts import render


def home_view(request):
    return render(
        request,
        'base.html',
    )


urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', home_view)
]
