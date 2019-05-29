from django.db import models

class ProductData(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=50)
    product_cost=models.IntegerField()
    product_color=models.CharField(max_length=100)
    product_class=models.CharField(max_length=100)
    customer_name=models.CharField(max_length=100)
    customer_mobile=models.BigIntegerField()
    customer_email=models.EmailField(max_length=100)

