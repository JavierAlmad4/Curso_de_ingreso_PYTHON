import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        #DATOS NOMBRE:
        while True:
            apellido = prompt("","Introduzca su apellido. ")
        
            if apellido == None: #NONE PARA QUE SEA SOLO LETRA
                break
        #EDAD
            edad = prompt("","Introduzca su edad")

            if edad == None:
                break
            while True:
                  if not edad.isdigit() or not int(edad) <18:
                    alert("","Tiene que ser mayor de edad.")
                    break
            #GENERO
            F = "femenino"
            M = "masculino"
            NB = "nobinario"
            genero = F | M | NB
            while True:
                if genero is str(F) or str(M) or str(NB):
                    prompt ("","Introduzca su genero (F,M,NB).")
                else:
                    break      
            


        #


'''
        contador_nb = 0
        menor_edad_jr = None
        menor_edad_jr_nombre = None
        bandera_primera_iteracion_jr = True

        acumulador_sexo_f = 0
        acumulador_sexo_m = 0
        acumulador_sexo_nb = 0
        contador_sexo_f = 0
        contador_sexo_m = 0
        contador_sexo_nb = 0
        contador_js = 0
        contador_python = 0
        contador_asp_net = 0
        CANTIDAD_ITERACIONES = 10

        ...
        for i in range(0, CANTIDAD_ITERACIONES):
            print("Postulante", i + 1)

            nombre = None

            sexo = prompt("Sexo", "Ingrese su sexo (F-M-NB)")

            while True:
                match sexo:
                    case "F":
                        print("Femenino")
                        break
                    case "M":
                        print("Masculino")
                        break
                    case "NB":
                        print("No binario")
                        break
                    case _:
                        print("Error")
                        sexo = prompt("Sexo", "Error! Ingrese su sexo (F-M-NB)")
            
            while nombre == "" or nombre == None:
                nombre = prompt("Nombre", "Ingrese dsu nombre")

            while True:
                edad = prompt("Edad", "Ingrese su edad")
                if edad == None or int(edad) < 18:
                    alert("Error", "Debe ser mayor de edad")
                else:
                    break
            
            # edad = prompt("Edad", "Ingrese su edad")

            # while edad == None or int(edad) < 18:
            #     edad = prompt("Edad", "Error! Ingrese su edad")

            edad = int(edad)
            
            genero = prompt("Genero", "Ingrese su genero (F-M-NB)")
            # & T     =>   V                V                 V
            # & F     =>   F                V                 V
            # OR T   =>   V                V                 V 
            # OR F   =>   F                V                 V
            while genero != "F" and genero != "M" and genero != "NB":
                genero = prompt("Genero", "Error! Ingrese su genero (F-M-NB)")

            tecnologia = prompt("Tecnologia", "Ingrese su tecnologia (PYTHON - JS - ASP.NET)")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("Tecnologia", "Error! Ingrese su tecnologia (PYTHON - JS - ASP.NET)")

            puesto = prompt("Puesto", "Ingrese su puesto (Jr - Ssr - Sr)")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt("Puesto", "Error! Ingrese su puesto (Jr - Ssr - Sr)")

            # A PARTIR DE AQUI TODOS LOS DATOS SON VALIDOS
            if puesto == "Ssr":
                """
                a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
                cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
                """
                if (tecnologia == "ASP.NET" or tecnologia == "JS") and (edad >= 25 and edad <= 40) and genero == "NB":
                    contador_nb += 1

            # b. Nombre del postulante Jr con menor edad.
            elif puesto == "Jr":
                if bandera_primera_iteracion_jr:
                    bandera_primera_iteracion_jr = False
                    menor_edad_jr = edad
                    menor_edad_jr_nombre = nombre
                elif edad < menor_edad_jr:
                    menor_edad_jr = edad
                    menor_edad_jr_nombre = nombre

            # c. Promedio de edades por género.                    
            match genero:
                case "F":
                    # acumulador => variable1 = variable1 + variable2
                    # contador => variable1 = variable1 + constante
                    acumulador_sexo_f += edad
                    contador_sexo_f += 1
                case "M":
                    acumulador_sexo_m += edad
                    contador_sexo_m += 1
                case "NB":
                    acumulador_sexo_nb += edad
                    contador_sexo_nb += 1

            # d. Tecnologia con mas postulantes (solo hay una).
            if tecnologia == "PYTHON":
                contador_python += 1
            else:
                if tecnologia == "JS":
                    contador_js += 1
                else:
                    contador_asp_net += 1

        # e. Porcentaje de postulantes de cada genero.
        porcentaje_f = (contador_sexo_f / CANTIDAD_ITERACIONES) * 100
        porcentaje_m = (contador_sexo_m / CANTIDAD_ITERACIONES) * 100
        porcentaje_nb = (contador_sexo_nb / CANTIDAD_ITERACIONES) * 100



        if contador_python > contador_js and contador_python > contador_asp_net:
            tecnologia_mas_postulantes = "PYTHON"
        elif contador_js > contador_python and contador_js > contador_asp_net:
            tecnologia_mas_postulantes = "JS"
        else:
            tecnologia_mas_postulantes = "ASP.NET"

        if contador_sexo_f > 0:
            promedio_edad_f = acumulador_sexo_f / contador_sexo_f
        else:
            promedio_edad_f = "No hay postulantes de genero F"
'''


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

