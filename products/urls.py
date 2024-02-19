from django.urls import path
from . import views

from .views import products_list, update_sku_status, product_detail, create_sku, active_categories_with_sku_count, all_skus_with_categories

urlpatterns = [
    path('products/', views.products_list, name='products_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('skus/create/', views.create_sku, name='create_sku'),
    path('sku/<int:pk>/update-status/', update_sku_status, name='update_sku_status'),
    path('active-categories-with-sku-count/', active_categories_with_sku_count, name='active_categories_with_sku_count'),
    path('all-skus-with-categories/', all_skus_with_categories, name='all_skus_with_categories'),
]