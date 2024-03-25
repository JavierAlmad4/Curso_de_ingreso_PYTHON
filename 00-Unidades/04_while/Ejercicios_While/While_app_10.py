import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Javier Ivan
apellido: Almada
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números
 que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
         
         acumulativo_n = 0
         acumulativo_p = 0
         acumulativo_z = 0

         suma_n = 0
         suma_p = 0

         while True:
            numero = prompt("Ingreso","Ingresar numero")
            if numero == None:
                break

            numero = int(numero)

            if numero < 0:
                 acumulativo_n += 1
                 suma_n += numero
            else:
                if numero > 0:
                    acumulativo_p += 1
                    suma_p += numero

                else:
                    acumulativo_z += 1
         
         dif = acumulativo_p - acumulativo_n

         alert("", "El acumulador de numero positivos es {0}, acumulador de numero negativo es {1}, suma de numeros positivos es {2}, la suma de numero negativos es {3}, el acumulador de zeros es {4} y la diferencia es {5}".format(acumulativo_p, acumulativo_n, suma_p, suma_n, acumulativo_z, dif))
             


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
