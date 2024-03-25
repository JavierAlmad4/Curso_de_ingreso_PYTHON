import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Javier Ivan
apellido: Almada
---
Ejercicio: Match_08
---
Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el botón 
‘Informar’ indicar mediante alert si en el destino hace frío o calor la mayoría 
de las estaciones del año.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        eleccion = self.combobox_destino.get()

        match(eleccion):
            case "Bariloche":
                mensaje = "En verano suelen alcanzarse los 36 °C y en invierno hasta -25,4, los veranos son secos, suaves y cortos, con precipitaciones concentradas en el invierno que son en forma de lluvia, cellisca y nevada."
            case "Mar del plata":
                mensaje = "Los veranos son suaves, con temperaturas medias por debajo de los 35 °C y los inviernos frescos con temperatura media de -3/-2 °C"
            case "Cataratas":
                mensaje = "El clima es subtropical húmedo, por lo tanto llueve muy seguido y siempre hace calor."
            case _:
                mensaje = "Durante todo el año predomina el frío y el viento, con una temperatura promedio de 6º C"
        alert("", mensaje)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()