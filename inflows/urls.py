from django.urls import path
from . import views


urlpatterns = [
    path('inflows/', views.InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', views.InflowCreateView.as_view(), name='inflow_create'),
    path('inflows/<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflow_detail'),
    # URLs APIs
    path('api/v1/inflows', views.InflowCreateListAPIView.as_view(), name='inflow-create-api-view'),
    path('api/v1/inflows/<int:pk>', views.InflowRetrieveUpdateDestroyAPIView.as_view(), name='inflow-create-api-view'),
]
