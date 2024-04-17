"""
Definir una clase y crear los objetos
"""

class Persona:
    #definiendo un constructor
    #Atributos caracteristicas
    def __init__(self,nombre,edad,sueldo,ts):
        self.nombre=nombre
        self.edad=edad
        self.sueldo=sueldo
        self.ts=ts
    #Definir Metodos   
    def mensaje(self):
        return f"Hola {self.nombre} Ya Usas POO?" 
    def calcular_bon(self):
        if self.ts>5:
            return f"Ud Tiene una bonificacion del 2% de su sueldo"
        else:
            return f"{self.nombre} Aun No Cuenta con una Bonificacion"


#aprendiendo a crear el objeto (Instanciar)
persona1=Persona("Jorge",28,1500,15)
persona2=Persona("Alicia",19,500,1)
#print(persona2.__dict__)
#print(f"{persona1.nombre} {persona1.edad}")
#print(persona2.mensaje())
print(persona2.calcular_bon())




