from django.urls import path
from .views import index,home,detail_product

urlpatterns = [
    path('index/', index,name="index"),
    path('detail_product/<int:id>/',detail_product,name="detail_product"),
    path('', home,name="home"),
    
]
