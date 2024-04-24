import tkinter as tk
from tkinter import messagebox

class Producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad

    def calcular_total(self):
        return self.precio*self.cantidad
    

class VentanaSecundaria:
    def __init__(self,ventana_padre):
        self.ventana_secundaria=tk.Toplevel(ventana_padre)
        self.ventana_secundaria.title=("Ventana Secundaria")
        self.etiqueta=tk.Label(self.ventana_secundaria,text="Widget de la ventana secundaria")
        self.etiqueta.pack(padx=10,pady=10)
   

class FacturaApp:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Facturacion")        
        self.productos=[]

        self.lbl_nombre=tk.Label(ventana,text="Nombre del producto")
        self.lbl_nombre.grid(row=0,column=0,padx=5,pady=5)
        self.entry_nombre = tk.Entry(ventana)
        self.entry_nombre.grid(row=0,column=1,padx=5,pady=5)

        self.lbl_precio=tk.Label(ventana,text="Precio")
        self.lbl_precio.grid(row=1,column=0,padx=5,pady=5)
        self.entry_precio=tk.Entry(ventana)
        self.entry_precio.grid(row=1,column=1,padx=5,pady=5)

        self.lbl_cantidad=tk.Label(ventana,text="Cantidad")
        self.lbl_cantidad.grid(row=2,column=0,padx=5,pady=5)
        self.entry_cantidad=tk.Entry(ventana)
        self.entry_cantidad.grid(row=2,column=1,padx=5,pady=5)

        self.btn_agregar=tk.Button(ventana,text="Agregar Producto",command=self.agregar_producto)
        self.btn_agregar.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

        self.btn_factura=tk.Button(ventana,text="Facturar",command=self.generar_factura)
        self.btn_factura.grid(row=4,column=0,columnspan=2,padx=5,pady=5)

        self.lbl_factura=tk.Label(ventana,text="")
        self.lbl_factura.grid(row=5,column=0,columnspan=2,padx=5,pady=5)

        self.btn_secundaria=tk.Button(ventana,text="Ventana2",command=self.abrir_ventana_secundaria)
        self.btn_secundaria.grid(row=6,column=0,columnspan=2,padx=5,pady=5)

    def agregar_producto(self):
        nombre=self.entry_nombre.get()
        precio=float(self.entry_precio.get())
        cantidad=int(self.entry_cantidad.get())

        if precio is None or cantidad is None:
            messagebox.showerror("Error","El Precio y la cantidad deben ser numeros")
            return
        #ValueError

        producto=Producto(nombre,precio,cantidad)
        self.productos.append(producto)
        messagebox.showinfo("Producto Agregado","Producto Agregado Correctamente")

        self.entry_nombre.delete(0,tk.END)
        self.entry_precio.delete(0,tk.END)
        self.entry_cantidad.delete(0,tk.END)

    def generar_factura(self):
        #Hallo el total general de la factura
        total=sum(producto.calcular_total() for producto in self.productos)    
        #Para visualizacion o impresion
        factura="Factura:\n\n"
        for producto in self.productos:
            factura += f"{producto.nombre}:${producto.precio} x {producto.cantidad} = ${producto.calcular_total()}\n"
        factura +="\nTotal a Pagar:$" + str(total)
        self.lbl_factura.config(text=factura)

    def abrir_ventana_secundaria(self):
        ventana_secundaria=VentanaSecundaria(self.ventana)     




#Crear la ventana principal
ventana_principal=tk.Tk()
app = FacturaApp(ventana_principal)        
ventana_principal.mainloop()