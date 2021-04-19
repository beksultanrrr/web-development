import json

from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from .models import Category, Product
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

@csrf_exempt
def products_id(request, product_id):
    # SELECT * FROM core_product WHERE id = <product_id>;
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)})
    return JsonResponse(product.to_json())

@csrf_exempt
def categories(request):
    if request.method == 'GET':
        # categories = Category.objects.filter(name='category 5')
        # categories = Category.objects.filter(name__startswith='cat')
        # categories = Category.objects.filter(name__endswith='ed')
        # categories = Category.objects.filter(name__contains='update')
        # categories = Category.objects.filter(id__in=[1, 2, 3, 4])
        categories = Category.objects.filter(name__contains='5').order_by('-id')
        categories_json = [category.to_json() for category in categories]
        return JsonResponse(categories_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            category = Category.objects.create(name=data['name'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(category.to_json())

@csrf_exempt
def categories_id(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(category.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        category.name = data['name']
        category.save()
        return JsonResponse(category.to_json())
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'message': 'deleted'}, status=204)
