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
    #Generando la orden de manera interna
    #Order.objects.create(complete=False)
    template_name="detalles.html"
    return render(request,template_name,context)


def add_to_cart(request,product_id):
    #Seleccionar cual es el producto que agregaremos al carrito
    product=Products.objects.get(pk=product_id)
    #Capturando la ultima orden generada
    last_order=Order.objects.last()
    #Anadiendo items generado
    OrderItem.objects.get_or_create(order=last_order,product=product,quantity=1)
    return redirect('index')

def cart(request):
    template_name="carts.html"
    order_detail=OrderItem.objects.all()
    context = {
        "detail" :order_detail
    }
    return render(request,template_name,context)


