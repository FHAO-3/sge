from django.urls import path
from . import views


urlpatterns = [
    # URLs fullstack
    path('ai/', views.AIListView.as_view(), name='ai_list'),
]
