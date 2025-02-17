import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

from ventana_altas import *

# Función para conectar con SQLite y crear la tabla si no existe
def conectar_db():
    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS empleados (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_apellidos varchar(50), fecha_ini date, fecha_nac date, direccion varchar(100), nif varchar(50), datos_bancarios varchar(100), afiliacion_ss varchar(60), genero varchar(50), departamento varchar(50), puesto varchar(50), telefono int, email varchar(50), salario_anual float, pagas_extra float , irpf float, seg_social varchar(50))")
    conexion.commit()
    conexion.close()


# Función para generar el fichero de empleados
def generar_fichero():
    conn = sqlite3.connect("empleados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    conn.close()
    
    with open("empleados.txt", "w", encoding="utf-8") as f:
        for emp in empleados:
            f.write(f"""
Nombre y Apellidos: {emp[1].upper()}    Teléfono: {emp[11]}    E-Mail: {emp[12]} 

Dirección: {emp[4]}  

NIF: {emp[5]}     Afiliación SS: {emp[7]}     Datos Bancarios: {emp[6]}

CONCEPTOS SALARIALES {("-" * 70)}

SALARIO ANUAL: {emp[13]:<10}  PAGAS: {emp[14]:<5}  IRPF: {emp[15]:<5}  SEGURIDAD SOCIAL: {emp[16]:<10}

{"=" * 90}

""")
    messagebox.showinfo("Éxito", "Fichero empleados.txt generado correctamente")

# Interfaz principal
principal = tk.Tk()
principal.title("Personal +")
principal.geometry("480x320")
principal.resizable(False,False) #de esta forma solo podremos ampliar el eje x. Si pongo True true, puedo ampliar los 2

tk.Label(principal, text="PERSONAL +", font=("Arial", 20)).pack(pady=10)

imagen = PhotoImage(file="seta.png").subsample(2)
imagen_label = tk.Label(principal, image=imagen)
imagen_label.pack(pady=10)

marco = ttk.Frame(principal)
marco.pack(expand=True)

style = ttk.Style()
style.configure("TButtonPrincipal.TButton",
                font=("Arial", 18, "bold"),
                padding=10,
                background="#d4ac0d",   #color borde botón
                foreground="black",     # color de texto
                relief="solid",         # tipo de botón
                width=18)               # Ancho de los botones

boton1 = ttk.Button(marco, text="Alta Empleado", command=altas, style="TButtonPrincipal.TButton")
boton1.pack(pady=5)

boton2 = ttk.Button(marco, text="Fichero Empleados", command=generar_fichero, style="TButtonPrincipal.TButton")
boton2.pack(pady=5)


conectar_db()
principal.mainloop()
