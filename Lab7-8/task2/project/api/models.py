from django.db import models

#same as

'''
# create table core_product (
#     id INTEGER,
#     name VARCHAR (300),
#     price NUMBER DEFAULT 0
# );
'''

class Product(models.Model): #by default primary key id
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField()
    isActive = models.BooleanField()
    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'isActive': self.isActive
        }


class Category(models.Model):
    name = models.CharField(max_length=300)
    def toJson(self):
        return {
            'id': self.id,
            'name': self.name
        }