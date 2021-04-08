from django.urls import path
from main.views import hello, productList, productDetail

urlpatterns = [
    path('hi/', hello),
    path('products/', productList),
    path('products/<int:id>', productDetail)
]