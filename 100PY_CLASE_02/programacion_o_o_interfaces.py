#Crear Interfaces Graficas (GUI)
import tkinter as tk

class SumadorApp:
    def __init__(self,master):
        self.master=master
        master.title("Sumador") 
        
        #creacion de widgets
        self.label1=tk.Label(master,text="Numero 1")
        self.label1.grid(row=0,column=0)

        self.entry1=tk.Entry(master)
        self.entry1.grid(row=0,column=1)

        self.label2=tk.Label(master,text="Numero 2")
        self.label2.grid(row=1,column=0)

        self.entry2=tk.Entry(master)
        self.entry2.grid(row=1,column=1)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=2, columnspan=2)

        self.sumar_button=tk.Button(master,text="Sumar",command=self.sumar)
        self.sumar_button.grid(row=3,columnspan=2)

    def sumar(self):
        num1=float(self.entry1.get())    
        num2=float(self.entry2.get())    
        resultado=num1+num2
        self.result_label.config(text=f"La Suma es {resultado}")


if __name__=="__main__":
    root=tk.Tk()
    #Creando un objeto de tipo interface en tkinter
    app=SumadorApp(root)
    root.mainloop()        