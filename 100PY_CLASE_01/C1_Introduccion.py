"""
Comentarios en
Varias Lineas
"""
#Comentario en Una Linea
#print("Hola Mundo desde Python") #Este es un comentario
#Tipos de datos Primitivos
"""
numericos : int - float
cadenas : str
logicos : bool
estructura: list , tuples, diccionarios , set
"""
edad_persona = 24 #int
nombre_persona="Armando" #str
apellido_persona='Ruiz' #str
estado_civil=True #bool
sueldo_persona=1200.90 #float
#type(edad_persona)
#type(nombre_persona)
#type(estado_civil)
#type(sueldo_persona)

cadena= nombre_persona + str(edad_persona)
cadena= nombre_persona , apellido_persona
cadena= f"El Nombre es:{nombre_persona} y el apellido:{apellido_persona} la edad de la persona {edad_persona}"

#pago_hora=18.90
#horas_trabajadas=int(input("Ingrese Horas Trabajadas:"))
#pago_diario = horas_trabajadas * pago_hora
#round(pago_diario,4)

"""
MUTABLES
"""
precios =[200,100,50,40,20,10,"Manzanas",True,[12,80,12]] #list
paises = {"colombia":"bogota","argentina":"bsn aires" ,"costa rica":"san jose"}#dict
"""
INMUTABLES
"""
codigo = (100,200,400) #tuple
precios.append("Soy Mutable")
precios[6]="Mangos"
#codigo[0]=800
#precios
#codigo.append("Soy Mutable")
