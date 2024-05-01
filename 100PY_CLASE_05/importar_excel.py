import openpyxl

#Ruta del archivo de excel
archivo_excel="datos.xlsx"

#Cargar el Libro de Trabajo(workbook)
libro_trabajo=openpyxl.load_workbook(archivo_excel)

#Seleccionar la hoja de trabajo(worksheet)
hoja_trabajo=libro_trabajo.active

#Lista para almacenar los datos

datos=[]

#iterar sobre las dilas y columnas del rango de celdas
for fila in hoja_trabajo.iter_rows():
    filas_datos=[]
    for celda in fila:
        filas_datos.append(celda.value)
    datos.append(filas_datos)    

for fila in datos:
    print(fila)