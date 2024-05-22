from django.contrib import admin
from .models import Products,Price_Products,Order,OrderItem

admin.site.register([Products,Price_Products,Order,OrderItem])



