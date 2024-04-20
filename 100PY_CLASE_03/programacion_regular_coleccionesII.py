"""
Una coleccion en Python es una estructura de datos que me permite
almacenar mas de un dato a la vez
Diccionario (Key-Value)
"""
mi_diccionario={}
mi_diccionario=dict() #Constructor

mi_diccionario={
    "nombre":"Juan",
    "edad":30,
    "ciudad":"Londres"
}
print(mi_diccionario["edad"])
print(mi_diccionario["ciudad"])
print(mi_diccionario["nombre"])

for k,v in mi_diccionario.items():
    print(f"La clave {k} y el valor es {v}")