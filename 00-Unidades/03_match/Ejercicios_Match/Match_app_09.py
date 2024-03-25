import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Javier Ivan
apellido: Almada
---
Ejercicio: Match_09
---
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        temporada = self.combobox_estaciones.get()
        destino = self.combobox_destino.get()
        tarifa_base = 15000
        
        match (temporada, destino):
            case "Invierno", "Bariloche":
                    tarifa_base *= 1.20
            case "Invierno", "Cataratas" | "Cordoba":
                    tarifa_base *= 0.90
            case "Invierno", "Mar del plata":
                    tarifa_base *= 0.80
        ##################################
            case "Verano", "Bariloche":
                    tarifa_base *= 0.80
            case "Verano", "Cataratas" | "Cordoba":
                    tarifa_base *= 1.10
            case "Verano", "Mar del plata":
                    tarifa_base *= 1.20
        ###################################
            case "Primavera" | "Otoño", "Bariloche" | "Cataratas":
                    tarifa_base *= 1.10
            case "Primavera" | "Otoño", "Cordoba":
                    tarifa_base *= 1
            case "Primavera" | "Otoño", "Mar del plata":
                    tarifa_base *= 1.10
                

        alert("", f"El importe es: $ {tarifa_base}")
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()