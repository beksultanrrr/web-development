from django.urls import path
from core.views import productList, productDetail

urlpatterns = [
    path('products/', productList),
    path('products/<int:id>', productDetail)
]