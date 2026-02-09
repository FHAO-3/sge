from django.urls import path
from . import views


urlpatterns = [
    # URLs fullstack
    path('brands/', views.BrandListView.as_view(), name='brands_list'),
    path('brands/create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('brands/<int:pk>/detail/', views.BrandDetailView.as_view(), name='brands_detail'),
    path('brands/<int:pk>/update/', views.BrandUpdateView.as_view(), name='brands_update'),
    path('brands/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brands_delete'),
    # URLs APIs
    path('api/v1/brands', views.BrandCreateListAPIView.as_view(), name='brand-create-api-view'),
    path('api/v1/brands/<int:pk>', views.BrandRetrieveUpdateDestroyAPIView.as_view(), name='brand-create-api-view'),
]
