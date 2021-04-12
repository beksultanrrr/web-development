from django.urls import path

from api.views import *

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:company_id>/', company_details),
    path('companies/<int:id>/vacancies/', company_vacancies),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:id>/', vacancy_details),
    path('vacancies/top_ten/', vacancies_top_ten)
    ]