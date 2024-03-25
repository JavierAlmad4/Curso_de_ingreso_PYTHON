import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: Javier Ivan 
apellido: Almada
---
Ejercicio: EXAMEN 01/03/24
---
Enunciado:
De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos
Marca (no validar) *
Categoría (peligroso, comestible, indumentaria)*
Peso ( entre 100 y 800)*
Tipo de material ( aluminio, hierro , madera)*
Costo en $ (mayor a 0)*

Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue la categoría menos ingresada (peligroso, comestible, indumentaria)
Informe B- El porcentaje de contenedores por Tipo de material ( aluminio, hierro , madera)
Informe C- La marca y tipo del contenedor menos pesado
Informe D- La marca del contenedor peligroso con mayor costo
Informe E- El promedio de peso de todos los contenedores

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Ingresar Datos", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):

        contenedores = 20

        cat_peligroso = 0
        cat_comestible = 0
        cat_indumentaria = 0
        
        porcentaje_aluminio = 0
        porcentaje_hierro = 0
        porcentaje_madera = 0

        contenedor_menos_pesado = 999999999 #PONGO VALOR GRANDE PARA AGARRAR EL MENOR
        marca_menos_pesado = ""
        tipo_menos_pesado = ""

        marca_contenedor = ""
        mayor_costo = 0

        suma_de_pesos = 0
        acum_contenedores = 0



        for i in range(contenedores): #pongo el rango
            #MARCA DEL CONTENEDOR:
            marca = prompt("Marca","Ingrese la marca del contenedor") #ingreso el nombre
            #SIN VALIDAR

            #CATEGORIA DEL CONTENEDOR:
            categoria = prompt("Categoria","Ingrese la categoria 'peligroso', 'comestible' o 'indumentaria'.")
            while categoria != "peligroso" and categoria != "comestible" and categoria != "indumentaria":
                categoria = prompt("Error","Ingrese una categoria valida 'peligroso','comestible' o 'indumentaria'.")

            #PESO DEL CONTENEDOR:
            peso = prompt("Peso","Ingrese el peso del contenedor (entre 100 y 800 kilos).") #PIDO PESO
            while int(peso) < 100 or int(peso) > 800: #PONGO RANGOS DEL PESO
                peso = prompt("Error","Ingrese un peso entre 100 y 800 kilos.") 

            #TIPO DE MATERIAL:
            tipo = ("Tipo de material","Ingrese el tipo de material 'aluminio', 'hierro' o 'madera'.") #Pido material
            while tipo != "aluminio" and tipo != "hierro" and tipo != "madera": #VALIDO SOLO ESTOS
                tipo = prompt("Error","Ingrese una categoria valida 'aluminio', 'hierro' o 'madera'.")
            
            #COSTO:
            costo = prompt("COSTO","Ingrese el costo.")
            while not costo.isdigit() or int(costo) <= 0: #IS DIGIT PARA NUMEROS, <=0 PARA BREAK
                costo = prompt("Error","Ingrese un costo mayor a 0.")
            
            #Informe A- Cuál fue la categoría menos ingresada (peligroso, comestible, indumentaria)
                
            if(categoria == "peligroso"): #creo CONTADOR PARA CADA CATEGORIA
                cat_peligroso += 1
            elif(categoria == "comestible"):
                cat_comestible += 1
            else:
                cat_indumentaria += 1
            
            if(cat_peligroso < cat_comestible and cat_peligroso < cat_indumentaria): #MENOR
                print("La categoria menos ingresada fue peligroso.")
            elif(cat_comestible < cat_peligroso and cat_comestible < cat_indumentaria): #MENOR
                print("La categoria menos ingresada fue comestible.")
            elif(cat_indumentaria < cat_peligroso and cat_indumentaria < cat_comestible): #MENOR
                print("La categoria menos ingresada fue indumentaria")

            #Informe B- El porcentaje de contenedores por Tipo de material ( aluminio, hierro , madera)
            #Sumo contadores
            if(tipo == "aluminio"):
                porcentaje_aluminio +=1
            elif(tipo == "hierro"):
                porcentaje_hierro +=1
            else:
                porcentaje_madera +=1

            suma = porcentaje_madera + porcentaje_aluminio + porcentaje_hierro #SUMO LOS 3 PARA LUEGO DIVIDIRLO

            if suma != 0:  #PARA NO TENER DIVISON DE 0
                porcentaje_aluminio = int((porcentaje_aluminio / suma) * 100) #DIVIDO Y MULTIPLICO
                porcentaje_hierro = int((porcentaje_hierro / suma) * 100) #DIVIDO Y MULTIPLICO
                porcentaje_madera = int((porcentaje_madera / suma) * 100) #DIVIDO Y MULTIPLICO
                #MULTIPLICO EN 3 PARA SU PORCENTAJE

            #CREO PRINT CON CADA PORCENTAJE
        print("Porcentaje de contenedores de aluminio: %{0}".format(porcentaje_aluminio))
        print("Porcentaje de contenedores de hierro: %{0}".format(porcentaje_hierro))
        print("Porcentaje de contenedores de madera: %{0}".format(porcentaje_madera))

            #Informe C- La marca y tipo del contenedor menos pesado
        
        if int(peso) < contenedor_menos_pesado: #CREO IF DEL PESO Y CREO VARIABLE MENOR PESO
            marca_menos_pesado = marca #AGARRO  MARCA
            tipo_menos_pesado = tipo #AGARRO TIPO 
            contenedor_menos_pesado = int(peso) #AGARRO CONTENEDOR MENOS PESO
        print("Contenedor menos pesado es: {0}, su tipo es {1} y su peso es {2}".format(marca_menos_pesado,tipo_menos_pesado,contenedor_menos_pesado))

            #Informe D- La marca del contenedor peligroso con mayor costo:
        
        if categoria == "peligroso" and int(costo) > mayor_costo: #SI CATEGORIA = PELIGROSO Y MAYOR A COSTO
            marca_contenedor = marca
            mayor_costo = int(costo)
            print("El contenedor mas peligroso es {0}, tambien tiene el mayor costo de {1}".format(marca_contenedor,mayor_costo))

            #Informe E- El promedio de peso de todos los contenedores
        
        suma_de_pesos += int(peso) #CREO VARIABLE DE SUMA DE PESOS
        acum_contenedores += 1 #CREO ACUMULADOR
        if acum_contenedores != 0: #PARA QUE NO DIVIDA EN 0
            promedio = suma_de_pesos / acum_contenedores #DIVIDOR
        else:
            promedio = 0 
        print("El promedio de todos los contenedores es: ", promedio) #SACO PROMEDIO

                

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()