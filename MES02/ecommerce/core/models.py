from django.db import models

class Products(models.Model):
    name=models.CharField(max_length=60)
    description=models.TextField(null=True,blank=True)
    state=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    picture=models.CharField(max_length=200,blank=True,null=True)
    price_base=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)

    def __str__(self):
        return self.name
    
class Price_Products(models.Model):
    price_1=models.DecimalField(max_digits=10,decimal_places=2)
    price_2=models.DecimalField(max_digits=10,decimal_places=2)
    price_3=models.DecimalField(max_digits=10,decimal_places=2)
    products=models.ForeignKey(Products,on_delete=models.CASCADE)


class Order(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE) 
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.product.name} of {self.order}'

    @property
    def get_total(self):
        total=self.product.price_base * self.quantity
    
        







