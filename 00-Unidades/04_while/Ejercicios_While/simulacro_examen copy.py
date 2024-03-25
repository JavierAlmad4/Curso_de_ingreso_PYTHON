import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Javier Ivan
apellido: Almada
---
Ejercicio: SimulacroExamen
---
Enunciado:
Se desea desarrollar un programa que permita al usuario ingresar el nombre, año emitido (inferior al 2000, Superior a 2000 e inferior a 2015 y superior al 2015), si es online u offline y costo (500 a 10000) de 10 videojuegos.
Realizar las siguientes operaciones:

A - Encontrar el videojuego más caro y el más barato ingresado.
B - Calcular el promedio de los costos de los videojuegos, pero solo para aquellos que son online.
C - Encontrar los videojuegos con el costo máximo y mínimo de aquellos emitidos antes de 2015.
D - Calcular el porcentaje de videojuegos offline en relación al total de videojuegos ingresados.
E - Informar a que rango de año emitido pertenecen la mayor parte de los videojuegos vendidos.

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        video_juego = 2
        mas_caro = 0
        mas_barato = 0

        acu_costo_online = 0
        contador_costo_online = 0

        max_juego_inf_2015 = 0
        nombre_max_juego_inf_2015 = ""

        min_juego_inf_2015 = 0
        nombre_min_juego_inf_2015 = ""

        bandera_juego_previo_2015 = True

        contador_offline = 0

        contador_fecha_menor_2000 = 0
        contador_fecha_mayor_2000_menor_2015 = 0
        contador_fecha_mayor_2015 = 0



        for i in range(video_juego): #Creo un for con el rango de video juego
            nombre = prompt("","Ingrese su nombre") #PIDO NOMBRE

            while nombre == None or nombre == "": #Si nombre no es valido cierra.
                nombre = prompt("","Ingrese su nombre de nuevo.")

            fecha = int(prompt("","Ingrese año"))

            while fecha == None or fecha == "" or int(fecha) <0: #agrego int en el num.
                fecha = prompt("","Ingrese el año de nuevo.")

            modo = prompt("","¿Es 'online' u 'offline' el videojuego? ")#PIDO MODO
            while modo != "offline" and modo != "online":
                modo = prompt("Error","Ingrese el modo ´online' o 'offline' de nuevo.")
            
            costo = prompt("","Ingrese el costo.") #PIDO COSTO
            while int(costo) < 500 or int(costo) > 10000: #PONGO LOS VALORES MINIMOS Y MAXIMOS
                    costo = prompt ("","Ingrese el costo de nuevo.")

            costo = int(costo)

            if i == 0:
                mas_caro = costo
                mas_barato = costo
            else:
                if costo > mas_caro:
                    mas_caro = costo
                if costo < mas_barato:
                    mas_barato = costo

            if modo == "online": #Acumulador de online
                acu_costo_online += costo
                contador_costo_online += 1

            #ENCONTRAR LOS JUEGOS CON FECHAS
                
            if(fecha < 2015):
                if bandera_juego_previo_2015 == True: #Si es
                    bandera_juego_previo_2015 = False
                    max_juego_inf_2015= nombre
                    min_juego_inf_2015 = costo
                    nombre_max_juego_inf_2015 = nombre
                    nombre_min_juego_inf_2015 = nombre

            else:
                if costo > max_juego_inf_2015: 
                    max_juego_inf_2015 = costo
                    nombre_max_juego_inf_2015 = nombre
                if costo < min_juego_inf_2015:
                    min_juego_inf_2015 = costo
                    nombre_min_juego_inf_2015 = nombre

        ###########PORCENTAJE
                    
                    if(modo == "offline"):
                        contador_offline +=1
        
        ########RANGO vendidos
        
        if(fecha < 2000):
            contador_fecha_menor_2000 += 1
        elif(fecha < 2015):
            contador_fecha_mayor_2000_menor_2015 += 1
        else:
            contador_fecha_mayor_2015 += 1


            ###########################
        
        if(contador_costo_online != 0):
            promedio = acu_costo_online / contador_costo_online
        else:
            promedio = 0
            print("Promedio costo juegos online es {0}".format(promedio))

        print("","El minimo menos a 2015 es {0} y el maximo es {1}".format(nombre_min_juego_inf_2015, nombre_max_juego_inf_2015))

        if(video_juego != 0):
            porcentaje_offline = contador_offline *100 / video_juego
        else:
            porcentaje_offline = 0

        print("El porcentaje de videojuegos offline es {0}".format(porcentaje_offline))

        if(contador_fecha_menor_2000 > contador_fecha_mayor_2000_menor_2015 and contador_fecha_menor_2000 > contador_fecha_mayor_2015):
            print("Se vendio mas juegos antes del 2000")
        elif(contador_fecha_mayor_2000_menor_2015 > contador_fecha_menor_2000 and contador_fecha_mayor_2000_menor_2015 > contador_fecha_mayor_2015):
            print("Se vendio mas juegos despues del 2000 y antes del 2015")
        elif(contador_fecha_mayor_2015 > contador_fecha_menor_2000 and contador_fecha_mayor_2015 > contador_fecha_mayor_2000_menor_2015):
            print("Se vendio mas juegos despues del 2015")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
