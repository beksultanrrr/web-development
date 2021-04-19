from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from api.models import Category
from ..serializers import CategorySerializerNew

class CategoryListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializerNew

    def post(self, request, *args, **kwargs):
        return self.create(self, request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializerNew
    # lookup_field = 'category_id'

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)
