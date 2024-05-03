import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog


class CRUD:#logica del negocio
    def __init__(self):
        self.conn=sqlite3.connect("crud.db")
        self.c=self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS personas (id INTEGER PRIMARY KEY,nombre TEXT NOT NULL,edad INTEGER)''')
        self.conn.commit() #Crear fisicamente la tabla en la bd

    def insertar_personas(self,nombre,edad):
        self.c.execute("INSERT INTO personas (nombre,edad) VALUES(?,?)",(nombre,edad))
        self.conn.commit()  

    def delete_personas(self,id):
        self.c.execute("DELETE FROM personas WHERE ID=?",(id,))      
        self.conn.commit()

    def update_personas(self,id,new_nombre):
        self.c.execute("UPDATE personas SET nombre=? WHERE id=?",(new_nombre,id))   
        self.conn.commit() 

    def fetch_all_records(self):
        self.c.execute("SELECT * FROM personas")    
        return self.c.fetchall()


class CRUD_App:#la interfaz
    def __init__(self,root):
        self.root=root
        self.root.title("CRUD con SQLITE y Tkinter")
        self.crud=CRUD()

        self.lbl_nombre=tk.Label(root,text="Nombre")
        self.lbl_nombre.grid(row=0,column=0)

        self.entry_nombre=tk.Entry(root)
        self.entry_nombre.grid(row=0,column=1)

        self.lbl_edad=tk.Label(root,text="Edad")
        self.lbl_edad.grid(row=1,column=0)

        self.entry_edad=tk.Entry(root)
        self.entry_edad.grid(row=1,column=1)

        self.btn_create=tk.Button(self.root,text="Crear",command=self.create_record)
        self.btn_create.grid(row=2,column=1,padx=10,pady=5)

        self.btn_delete=tk.Button(self.root,text="Eliminar",command=self.delete_record)
        self.btn_delete.grid(row=2,column=2,padx=10,pady=5)

        self.btn_actualizar=tk.Button(self.root,text="Actualizar",command=self.update_record_dialog)
        self.btn_actualizar.grid(row=2,column=3,padx=10,pady=5)

        self.tree=ttk.Treeview(self.root,columns=("ID","Nombre","Edad"),show="headings")
        self.tree.heading("ID",text="ID")
        self.tree.heading("Nombre",text="Nombre")
        self.tree.heading("Edad",text="Edad")

        self.tree.grid(row=3,column=1,columnspan=3,padx=10,pady=5)

        self.populate_treeview()

    def create_record(self):
        nombre=self.entry_nombre.get()
        edad=self.entry_edad.get()
        if nombre:
            self.crud.insertar_personas(nombre,edad)
            self.populate_treeview()#Actualizar el treview
        else:
            messagebox.showwarning("Advertencia","Por Favor debe ingresar los datos correctamente")   


    def populate_treeview(self):
        records=self.crud.fetch_all_records()
        #Limpiar el Treevie antes de repoblarlo
        for item in self.tree.get_children():
            self.tree.delete(item)
        #repoblarlo    
        for record in records:
            self.tree.insert("","end",values=record)     

    def get_selected_record_id(self):
        selected_item=self.tree.selection()
        if selected_item:
            item=self.tree.item(selected_item)           
            record_id=item["values"][0]
            return record_id
        else:
            return None

    def delete_record(self):
        record_id=self.get_selected_record_id()
        if record_id:
            confirm=messagebox.askyesno("Eliminar el Registro","¿Estas Seguro de eliminar el registro")
            if confirm:
                self.crud.delete_personas(record_id)#elimina de la tabla
                self.tree.delete(self.tree.selection())#elimina el item seleccionado del treeview    

    def update_record_dialog(self):
        record_id=self.get_selected_record_id()
        if record_id:
            old_nombre=self.tree.item(self.tree.selection())["values"][1]
            new_nombre=simpledialog.askstring("Actualizar Registro","Nuevo Nombre ",initialvalue=old_nombre)
            if new_nombre:
                self.crud.update_personas(record_id,new_nombre)
                self.populate_treeview()
            else:
                messagebox.showwarning("Advertencia","Por Favor Ingrese el Nombre")    



if __name__=="__main__":
    root=tk.Tk()
    app=CRUD_App(root)
    root.mainloop()

        
