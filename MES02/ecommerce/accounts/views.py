from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login

def home_view(request):
    template_name="accounts/home.html"
    return render(request,template_name)

def login_view(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        print(f"Que me muestra el {user}")
        if user is not None:
            login(request,user)#ingresar al administrador de forma automatica
            context ={
                "logueado":user
            }
            return render(request,'home.html',context)
        else:
            context ={
                "error":"Credenciales Invalidadas"
            }
            return render(request,'accounts/login.html',context)
    else:
        return render(request,'accounts/login.html')    

