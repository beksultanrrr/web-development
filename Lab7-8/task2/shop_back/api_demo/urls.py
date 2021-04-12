from django.urls import path
from api_demo.views import category_list, category_detail
urlpatterns = [
    path('categories/', category_list),
    path('categories/<int:category_id>/', category_detail)
]