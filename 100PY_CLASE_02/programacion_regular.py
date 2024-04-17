#Creacion de funciones
def calcular_edad(nac,nom):
    edad=2024-nac
    mensaje=f"{nom} tu edad es {edad}"
    return mensaje

#print(calcular_edad(1970,"Armando"))

def calcular_bonificacion(area):
    if area=="sistemas":
        bon=20
    elif area=="marketing":
        bon=40
    elif area=="contabilidad":
        bon=15        
    return bon
#print(calcular_bonificacion("contabilidad"))

def ingreso_cajero():
    #supongamos que la clave y el documento estan predefinidos
    documento="10210906"
    clave="124"
    intentos=3
    #*******************************************
    while intentos >0:#va a continuar
        ingreso_docu=input("Ingrese documento:")
        ingreso_clave=input("Ingrese la clave:")
        if ingreso_docu==documento and ingreso_clave==clave:
            print("Bienvenido al Sistema")
            break #salir del buccle
        else:
            intentos -= 1
            if intentos > 0:
                print("documento o clave incorrectos")    
            else:    
                print("Has excedido el numero de intentos tu cuenta se bloqueara por 24 horas")
                break    
#        return mensaje    


ingreso_cajero()


    