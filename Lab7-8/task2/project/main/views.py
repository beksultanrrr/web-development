from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest

def hello(request):
    return HttpResponse('<h1>Hello view function response</h1>')

products = [
    {
        'id': i,
        'name': f'Product {i}',
        'price': 1000
    }
    for i in range(1, 10)
]

def productList(request):
    # return HttpResponse('<h1>List of products</h1>')
    return JsonResponse(products, safe=False)

def productDetail(request, id):
    for product in products:
        if product['id'] == id:
            return JsonResponse(product)
    return JsonResponse({'message': 'Product with selected id not found'}) #to avoid error
    # return HttpResponse(f'<h1>Product details page: {id}</h1>')