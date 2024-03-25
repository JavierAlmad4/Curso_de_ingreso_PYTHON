import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Javier Ivan
apellido: Almada
---
Ejercicio: while_03
---
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volver a solicitarla hasta que coincidan.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        contraseña = "utn750"

        while True: #True para que se repita hasta que sea verdadero
            contraseña = prompt("", "Ingrese la contraseña:") #prompt para insertar
            if contraseña == 'utn750': #Si contraseña es ==
                alert("", "Contraseña correcta!") #alert para correcta
                break #rompo el codigo para que no entre en bucle
            else: #en caso que no sea correcto
                alert("Error", "Contraseña incorrecta. Inténtelo de nuevo.") #alert para error
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()