from rest_framework import serializers
from api.models import Category, Product

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) #list all fields that we want to serialize
    name = serializers.CharField()

    def create(self, validated_data): # case save
        #creating new category
        category = Category.objects.create(name=validated_data.get('name'))
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance

class Product2Serializer(serializers.ModelSerializer):
    # category = CategorySerializerNew(read_only=True)
    # category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'category', 'count', 'isActive', 'category_id')


class CategorySerializerNew(serializers.ModelSerializer):

    name = serializers.CharField()
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # products = serializers.StringRelatedField(many=True, read_only=True)
    products = Product2Serializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'products')



class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializerNew(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'category', 'count', 'isActive', 'category_id')