from django.urls import path
from skus import views

urlpatterns = [
    path('skus/', views.sku_list),
    path('skus/<int:pk>/', views.sku_detail),
]