from django.shortcuts import render
from django.http import JsonResponse
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def companies_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)


def company_details(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(company.to_json())


def company_vacancies(request, id):
    try:
        vacancies = Vacancy.objects.filter(company=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_details(request, id):
    try:
        vacancy = Company.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(vacancy.to_json())


def vacancies_top_ten(request):
    vacancies = Vacancy.objects.order_by("-salary")[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

