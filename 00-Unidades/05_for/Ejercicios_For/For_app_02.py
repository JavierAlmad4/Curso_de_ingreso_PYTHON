import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Javier Ivan
apellido: Almada
---
Ejercicio: for_02
---
Enunciado:
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números DESCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        for i in range(5,0, -1): #0=start,5=end,1=step*pasos 
            alert("", "Numero {}".format(i))
                 #print(i) #o para comenzar en 1 (i+1)
       
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()