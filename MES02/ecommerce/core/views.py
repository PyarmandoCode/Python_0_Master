from django.shortcuts import render,get_object_or_404,redirect
from .models import Products,Order,OrderItem


#Vista basada en funcion
def index(request):
    products=Products.objects.all()
    context = {
        "products":products
    }
    template_name="index.html"
    return render(request,template_name,context)

def home(request):
    template_name="home.html"
    return render(request,template_name)

def detail_product(request,id):
    #ORM Queryset
    #select * from products whete pk=id
    product=Products.objects.get(pk=id)
    context ={
        "product":product
    }
    template_name="detalles.html"
    return render(request,template_name,context)

def add_to_cart(request,product_id):
    product=get_object_or_404(Products,id=product_id)
    order,created=Order.objects.get_or_create(complete=False)
    order_item,created=OrderItem.objects.get_or_create(order=order,product=product)
    order_item.quantity +=1
    order_item.save()
    return redirect('index')

def cart(request):
    template_name="carts.html"
    #order,created=Order.objects.get_or_create(complete=False)
    order_detail=OrderItem.objects.all()
    context = {
        "detail" :order_detail
    }
    print(f'este es el contexto {context}')
    return render(request,template_name,context)


