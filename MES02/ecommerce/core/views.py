from django.shortcuts import render
from .models import Products


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