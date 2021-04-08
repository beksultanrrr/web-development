from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.request import HttpRequest
from core.models import Product

def productList(request):
    #SELECT * FROM core_product
    products = Product.objects.all()
    productsJson = [product.toJson() for product in products]
    print(productsJson)
    return JsonResponse(productsJson, safe=False)

def productDetail(request, id):
    # SELECT * FROM core_product WHERE id = <product_id>;
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(product.toJson())