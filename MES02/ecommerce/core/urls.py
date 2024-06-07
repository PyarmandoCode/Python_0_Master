from django.urls import path
from .views import index,home,detail_product,add_to_cart,cart,logout_view

urlpatterns = [
    path('index/', index,name="index"),
    path('detail_product/<int:id>/',detail_product,name="detail_product"),
    path('', home,name="home"),
    path('add_to_cart/<int:product_id>',add_to_cart,name="add_to_cart"),
    path('cart/',cart,name="cart"),
    path('logout/',logout_view,name="logout")
   
    
]
