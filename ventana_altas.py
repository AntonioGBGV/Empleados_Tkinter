import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def altas():
    ventana_alta = Toplevel()
    ventana_alta.title("Alta Empleado")
    ventana_alta.geometry("930x400")

    entry_nombre_apellidos = tk.Entry(ventana_alta)
    entry_fecha_ini = tk.Entry(ventana_alta)
    entry_fecha_nac = tk.Entry(ventana_alta)
    entry_direccion = tk.Entry(ventana_alta)
    entry_nif = tk.Entry(ventana_alta)
    entry_datos_bancarios = tk.Entry(ventana_alta)
    entry_afiliacion_ss = tk.Entry(ventana_alta)
    entry_genero = tk.Entry(ventana_alta)
    entry_departamento = tk.Entry(ventana_alta)
    entry_puesto = tk.Entry(ventana_alta)
    entry_telefono = tk.Entry(ventana_alta)
    entry_email = tk.Entry(ventana_alta)
    entry_salario_anual = tk.Entry(ventana_alta)
    entry_pagas_extra = tk.Entry(ventana_alta)
    entry_irpf = tk.Entry(ventana_alta)
    entry_seg_social = tk.Entry(ventana_alta)
    
    tk.Label(ventana_alta, text="Nombre y apellidos:").grid(column=2, row=0, padx=15, pady=5)
    entry_nombre_apellidos.grid(column=0, row=1, columnspan=6, padx=15, pady=5, sticky=EW)

    tk.Label(ventana_alta, text="Fecha Inicio:").grid(column=0, row=3, padx=15, pady=5)
    tk.Label(ventana_alta, text="Fecha Nacimiento:").grid(column=1, row=3, padx=15, pady=5)
    tk.Label(ventana_alta, text="Dirección:").grid(column=4, row=3, padx=15, pady=5)
    entry_fecha_ini.grid(column=0, row=4, padx=15, pady=5)
    entry_fecha_nac.grid(column=1, row=4, columnspan=2, padx=15, pady=5, sticky=EW)
    entry_direccion.grid(column=3, row=4, columnspan=3, padx=15, pady=5, sticky=EW)

    tk.Label(ventana_alta, text="NIF:").grid(column=0, row=5, padx=15, pady=5)
    tk.Label(ventana_alta, text="Datos bancarios:").grid(column=1, row=5, padx=15, pady=5)
    tk.Label(ventana_alta, text="Número de afiliación SS:").grid(column=4, row=5, padx=15, pady=5)
    entry_nif.grid(column=0, row=6, padx=15, pady=5)
    entry_datos_bancarios.grid(column=1, row=6, columnspan=2, padx=15, pady=5, sticky=EW)
    entry_afiliacion_ss.grid(column=3, row=6, columnspan=3, padx=15, pady=5, sticky=EW)
    
    tk.Label(ventana_alta, text="Género:").grid(column=0, row=7, padx=15, pady=5)
    tk.Label(ventana_alta, text="Departamento:").grid(column=1, row=7, padx=15, pady=5)
    tk.Label(ventana_alta, text="Puesto:").grid(column=4, row=7, padx=15, pady=5)
    entry_genero.grid(column=0, row=8, padx=15, pady=5)
    entry_departamento.grid(column=1, row=8, columnspan=2, padx=15, pady=5, sticky=EW)
    entry_puesto.grid(column=3, row=8, columnspan=3, padx=15, pady=5, sticky=EW)

    tk.Label(ventana_alta, text="Teléfono:").grid(column=0, row=9, padx=15, pady=5)
    entry_telefono.grid(column=1, row=9, padx=15, pady=5)

    tk.Label(ventana_alta, text="Salario Anual:").grid(column=2, row=9, padx=15, pady=5)
    entry_salario_anual.grid(column=3, row=9, padx=15, pady=5)

    tk.Label(ventana_alta, text="IRPF:").grid(column=4, row=9, padx=15, pady=5)
    entry_irpf.grid(column=5, row=9, padx=15, pady=5)

    tk.Label(ventana_alta, text="E-Mail:").grid(column=0, row=10, padx=15, pady=5)
    entry_email.grid(column=1, row=10, padx=15, pady=5)

    tk.Label(ventana_alta, text="Pagas Extras:").grid(column=2, row=10, padx=15, pady=5)
    entry_pagas_extra.grid(column=3, row=10, padx=15, pady=5)

    tk.Label(ventana_alta, text="Seg. social:").grid(column=4, row=10, padx=15, pady=5)
    entry_seg_social.grid(column=5, row=10, padx=15, pady=5)

    Label(ventana_alta, text="").grid(column=0, row=11)

    def insertar_empleado():
        conn = sqlite3.connect("empleados.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO empleados(nombre_apellidos, fecha_ini, fecha_nac, direccion, nif, datos_bancarios, afiliacion_ss, genero, departamento, puesto, telefono, salario_anual, irpf, email, pagas_extra, seg_social)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                       (
            entry_nombre_apellidos.get(), entry_fecha_ini.get(), entry_fecha_nac.get(), entry_direccion.get(),
            entry_nif.get(), entry_datos_bancarios.get(), entry_afiliacion_ss.get(), entry_genero.get(),
            entry_departamento.get(), entry_puesto.get(), entry_telefono.get(), entry_salario_anual.get(),
            entry_irpf.get(), entry_email.get(), entry_pagas_extra.get(), entry_seg_social.get()
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Empleado insertado correctamente")
        ventana_alta.destroy()
    

    style = ttk.Style()
    style.configure("TButtonAltas.TButton",
                font=("Arial", 18, "bold"),
                padding=10,
                relief="solid",
                background="#d4ac0d",  # Color de fondo
                foreground="black",     # Color del texto
                width=10)               # Ancho de los botones

    boton3 = ttk.Button(ventana_alta, text="Insertar", command=insertar_empleado, style="TButtonAltas.TButton")
    boton3.grid(row=12, column=4)

    
    

