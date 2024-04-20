"""
Creear un Programa para automatizar la planilla de sueldos de una empresa
con las siguientes caracteristicas:
1.-Se debe tener algunos empleados ya registrados en diccionarios (3)
2.-Se debe tener la posibilidad de poder ingresar nuevos empleados
3.-Se debe calcular la suma de sueldos y se debe obtener el promedio de ese
mes
"""

pago_hora=20 #constante

trabajadores=[
    {"codigo":"Trab_01","ht":40},#0
    {"codigo":"Trab_02","ht":46},#1
    {"codigo":"Trab_03","ht":50} #2
]

def registro_empleado(codpar,htpar):
    nuevo_empleado = {
        "codigo":codpar,
        "ht":htpar
    } #el nuevo diccionario
    trabajadores.append(nuevo_empleado) #se agrega a la lista

def listar_empleado():
    try: 
        global pago_hora
        sum_horas=0
        for index,empleado in enumerate(trabajadores):#me devuelve el indice
            sueldo_trabajador=trabajadores[index]["ht"]*pago_hora
            sum_horas += sueldo_trabajador #Acumulador de sueldos
        return f"La Suma de los sueldos de mi planilla es {sum_horas} y el promedio  {round(sum_horas /len (trabajadores),2)}"  
    except Exception as err:
       return f"Ocurrio un error {err}"  
    
        
   

while True:
  try:  
    codigo=input("Ingrese codigo:")
    ht=int(input("Ingrese las HT:"))
    registro_empleado(codigo,ht)
    resp=input("¿Desea continuar:")
    if resp=="n":#True
        break
  except ValueError:
     print("Debes ingresar datos correctos")     
  else:   
     print(listar_empleado())    

   


#print(listar_empleado())
#datos = ("Televisor","Computador") #tuple
#datos[1]="Parlante"