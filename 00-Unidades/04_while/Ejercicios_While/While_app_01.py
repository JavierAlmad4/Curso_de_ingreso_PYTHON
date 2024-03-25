import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Javier Ivan
apellido: Almada
---
Ejercicio: while_01
---
Enunciado:
Al presionar el botón ‘Mostrar Interación’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        inicio = 1 #variable de comienzo
        while inicio <= 10: #se inicia bucle while y se ejecuta hasta <=10 
            alert("Repeticiones", str(inicio))
            inicio += 1 #despues de mostrar el mensaje se incrementa de a 1 hasta el maximo (10)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()