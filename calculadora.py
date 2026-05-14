import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        # Configuración principal de la ventana (título, color y tamaño)
        self.root = root
        self.root.title("Calculadora Pro")
        self.root.config(bg="#2b2b2b")
        self.root.geometry("375x550")
        self.root.resizable(False, False)

        # Pantalla de entrada donde se muestran los números y resultados
        self.entrada = tk.Entry(root, width=17, font = ("Arial", 24), borderwidth=0,
                                relief = "solid", bg="#2b2b2b", fg="white", justify="right")
        self.entrada.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=(10,5))

        self.crear_botones()

    def crear_botones(self):
        # Lista de botones con su texto y el espacio que ocupan (span)
        botones = [
            ("c", 2), ("←", 1), ("/", 1),
            ("7", 1), ("8", 1), ("9", 1), ("*", 1),
            ("4", 1), ("5", 1), ("6", 1), ("-", 1),
            ("1", 1), ("2", 1), ("3", 1), ("+", 1),
            ("0", 2), (".", 1), ("=", 1)
        ]

        # Paleta de colores para identificar visualmente cada tipo de tecla
        colores_botones = {
            "numero" : "#4d4d4d",
            "operador" :"#fe9505",
            "igual" : "#03E6FF",
            "fondo" : "2E2E2E",
            "texto" : "#FFFFFF",
            "reset" : "#d32f2f",
            "borrar" : "#FF5722",
        }

        # Contenedor para organizar los botones en una cuadrícula (grid)
        frame_botones = tk.Frame(self.root, bg="#2E2E2E")
        frame_botones.grid(row=1, column=0, columnspan=4, pady=(0,10))

        fila = 0
        columna = 0

        # Ciclo para crear cada botón automáticamente según la lista de arriba
        for boton, span in botones:
            # Lógica para asignar colores según el tipo de botón
            color_fondo = colores_botones["operador"] if boton in ["/", "*", "-", "+", "=" "←"] else colores_botones ["numero"]
            if boton == "c":
                color_fondo = colores_botones["reset"]
            elif boton == "←":
                color_fondo = colores_botones["borrar"]
            elif boton == "=":
                color_fondo = colores_botones["igual"]

            # Creación física del botón con sus estilos y conexión a la función de clic
            tk.Button(frame_botones, text=boton, width=5*span, height=2, font=("Arial", 20),
                        bg=color_fondo, fg=colores_botones["texto"], borderwidth=0,
                        command=lambda b=boton: self.click_boton(b)).grid(row=fila, column=columna, columnspan=span, padx=1, pady=1,
                                                                    sticky="nsew")

            # Control de la cuadrícula para saltar de fila cada 4 columnas
            columna += span
            if columna >= 4:
                columna = 0
                fila += 1
            
            # Hace que los botones se estiren proporcionalmente
            for i in range(4):
                frame_botones.grid_columnconfigure(i, weight=1)
            for i in range(fila + 1):
                frame_botones.grid_rowconfigure(i, weight=1)

    def click_boton(self, valor):
        # Lógica para procesar las operaciones
        if valor == "=":
            try:
                # eval() calcula automáticamente la operación escrita en pantalla
                resultado = str(eval(self.entrada.get()))
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, resultado)
            except Exception as e:
                # Manejo de errores (ej: si intentas dividir por cero)
                messagebox.showerror("error", "NO FUNCIONA")
                self.entrada.delete(0, tk.END)
        
        # Limpiar toda la pantalla
        elif valor == "c":
            self.entrada.delete(0, tk.END)
        
        # Borrar el último carácter ingresado
        elif valor == "←":
            self.entrada.delete(len(self.entrada.get())-1, tk.END)
        
        # Insertar el número o símbolo presionado
        else:
            self.entrada.insert(tk.END, valor)

# Punto de inicio de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    Calculadora = Calculadora(root)
    root.mainloop()