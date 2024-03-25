import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Javier Ivan
apellido: Almada
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y 
el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("","Ingrese un numero")

        

        for i in range(1,int(numero)):
            es_primo = True
            for j in range (2, i):
                if (i % j == 0):
                    es_primo = False
                    break
            if(es_primo):
                print(i)
        alert("",f"En total son: {es_primo} encontrados. ")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()