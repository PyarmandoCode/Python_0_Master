"""
Gestores de BD RELACIONALES
POSTGRESS - MYSQL - SQL SERVER -MARIADB -SQLITE
"""
import sqlite3
#Conectar a la base de datos (Crear el archivo si no existe)
conn=sqlite3.connect('empresa.db')
#Crear una Tabla
#Crear un cursor 

c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS empleados
          (id INTEGER PRIMARY KEY,
           nombre TEXT,
           area TEXT)
          ''')

# #Insertar Algunos datos
# c.execute("INSERT INTO empleados (nombre,area) VALUES(?,?)",('Claudia Ramos','Sistemas') )
# c.execute("INSERT INTO empleados (nombre,area) VALUES(?,?)",('Oscar Durand','Sistemas') )
# c.execute("INSERT INTO empleados (nombre,area) VALUES(?,?)",('Miguel Fuentes','RRHH') )
# c.execute("INSERT INTO empleados (nombre,area) VALUES(?,?)",('Maria Palacios','RRHH') )
# c.execute("INSERT INTO empleados (nombre,area) VALUES(?,?)",('Guillermo Oliva','Contabilidad') )
# #Confirmar los cambios
# conn.commit()

#Crear consultas
#Seleccionar todos los empleados

def seleccionar_empleados():
    c.execute("SELECT * FROM EMPLEADOS")
    #Obtener todos los resultados de la consulta
    filas=c.fetchall()
    for fila in filas:
        print(fila)

def actualizar_informacion():
    c.execute("UPDATE empleados SET area=? WHERE id=?",('Sistemas',6))
    conn.commit() #La Informacion se esta actualizando

def eliminar_empleado():
    c.execute("DELETE FROM empleados WHERE id=?",(6,))    
    conn.commit() #La Informacion se esta actualizando



#cerrar la conexion
#seleccionar_empleados()
eliminar_empleado()
seleccionar_empleados()

conn.close()