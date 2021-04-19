from django.db import models

#same as

'''
# create table core_product (
#     id INTEGER,
#     name VARCHAR (300),
#     price NUMBER DEFAULT 0
# );
'''

class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __str__(self):
        return f'{self.id}: {self.name}'

class Product(models.Model): #by default primary key id
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField()
    isActive = models.BooleanField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.id}: {self.name} | {self.price}'

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products') #CASCADE, SET_NULL null=True, SET_DEFAULT default=1
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'isActive': self.isActive
        }

