from rest_framework.decorators import api_view

from django.shortcuts import render
from django.http import JsonResponse
from api.models import Category
from ..serializers import CategorySerializerNew
import json
from rest_framework.request import Request
from rest_framework.response import Response

from django.http.response import HttpResponse
from django.http.request import HttpRequest

@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializerNew(categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializerNew(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'DELETE', 'PUT'])
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = CategorySerializerNew(category)
        return Response(serializer.data, safe=False)

    elif request.method == 'PUT':
        serializer = CategorySerializerNew(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        category.delete()
        return Response({'message': 'deleted'}, status=204) #204 - no content