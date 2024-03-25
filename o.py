import tkinter as tk
from tkinter import messagebox

def calcular_incremento():
    try:
        # Obtener el número del cliente y el porcentaje de entrada
        cliente = float(entry_cliente.get())
        porcentaje = float(entry_porcentaje.get())

        # Calcular el incremento
        incremento = cliente * (porcentaje / 100)

        # Calcular el resultado
        resultado = cliente + incremento

        # Mostrar el resultado en una ventana emergente
        messagebox.showinfo("Resultado", f"El resultado después del incremento es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de incremento")

# Crear etiquetas y campos de entrada
label_cliente = tk.Label(root, text="Cliente:")
label_cliente.grid(row=0, column=0, padx=5, pady=5)
entry_cliente = tk.Entry(root)
entry_cliente.grid(row=0, column=1, padx=5, pady=5)

label_porcentaje = tk.Label(root, text="Porcentaje:")
label_porcentaje.grid(row=1, column=0, padx=5, pady=5)
entry_porcentaje = tk.Entry(root)
entry_porcentaje.grid(row=1, column=1, padx=5, pady=5)

# Botón para calcular el incremento
btn_calcular = tk.Button(root, text="Calcular Incremento", command=calcular_incremento)
btn_calcular.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()