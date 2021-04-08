from django.urls import path
from api.views import products, products_id, categories, categories_id

urlpatterns = [
    path('products/', products),
    path('products/<int:product_id>/', products_id),
    path('categories/', categories),
    path('categories/<int:categories_id>/', categories_id),
]