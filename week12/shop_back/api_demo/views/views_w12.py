from django.shortcuts import render
from django.http import JsonResponse
from api.models import Category, Product
# from WD.week12.shop_back.api.models import Category, Product
from ..serializers import CategorySerializerNew
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
# Create your views here.

@csrf_exempt
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializerNew(categories, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        # return JsonResponse({'message': 'New item created.'})
        data = json.loads(request.body)
        serializer = CategorySerializerNew(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

@csrf_exempt
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = CategorySerializerNew(category)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CategorySerializerNew(instance=category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'message': 'deleted'}, status=204) #204 - no content