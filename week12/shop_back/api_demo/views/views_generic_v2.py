from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from api.models import Category, Product
from ..serializers import CategorySerializerNew, ProductSerializer, Product2Serializer
from rest_framework.permissions import IsAuthenticated

class CategoryListAPIView(generics.ListCreateAPIView, generics.GenericAPIView): # post and get

    def get_queryset(self):
        # return Category.objects.all(user = self.request.user)
        return Category.objects.all()
    # queryset = Category.objects.all()
    serializer_class = CategorySerializerNew
    permission_classes = (IsAuthenticated,)

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializerNew



class ProductListAPIView(generics.ListCreateAPIView, generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
