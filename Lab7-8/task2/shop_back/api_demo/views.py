from django.shortcuts import render
from django.http import JsonResponse
from api.models import Category
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def category_list(request):
    if request.method == "GET":
        # categories = Category.objects.filter(name='category 5')
        # categories = Category.objects.filter(name__startswith='cat')
        # categories = Category.objects.filter(name__endswith='ed')
        # categories = Category.objects.filter(name__contains='update')
        # categories = Category.objects.filter(id__in=[1, 2, 3, 4])
        categories = Category.objects.all()
        categories_json = [category.to_json() for category in categories]
        return JsonResponse(categories_json, safe=False)
    elif request.method == "POST":
        # return JsonResponse({'message': 'New item created.'})
        data = json.loads(request.body)
        try:
            category = Category.objects.create(name=data['name'])
        except Exception as e:
            return JsonResponse({'message': str(e)})
        return JsonResponse(category.to_json())

@csrf_exempt
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(category.to_json())

    elif request.method == 'PUT':
        data = json.loads(request.body)
        category.name = data["name"]
        category.save()
        return JsonResponse(category.to_json())

    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'message': 'deleted'}, status=204) #204 - no content