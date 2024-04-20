"""
Una coleccion en Python es una estructura de datos que me permite
almacenar mas de un dato a la vez
"""
producto="Televisor" #str
precio=1200 #int
igv=0.18 #float

lista_productos=["Televisor","Computador","Parlantes",200,210.20] #lista
#print(lista_productos[4])
#metodos de lista
lista_productos.append("Laptop") #Al Final
lista_productos.insert(2,"Teclado") #Posicion Indicada en el argumento
lista_productos[2]="Mouse" #Actualizar el elemento por su posicion
lista_productos.pop(2) #Eliminando un elemento de la lista por su posicion
lista_productos.remove("Parlantes") #Eliminando por su nombre

for elemento in lista_productos: #desempaquetar 
    if elemento =="Televisor":
        continue #Obviar el elemento
    elif elemento==210.2:
        break #Salir del bucle
    else:
        print(elemento)
        

#print(lista_productos)
