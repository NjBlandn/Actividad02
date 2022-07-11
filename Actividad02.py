# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 09:40:32 2022

@author: Dell
"""

import tkinter as tk

##Crear una instancia de Tkinter
ventana = tk.Tk()
ventana.geometry("900x800")

#Configurar color de fondo
ventana.config(bg='black')

## Grados Decimales
#Agregar primera etiqueta
Label = tk.Label(ventana, text = "Grados Decimales:", bg = "white", fg = "black", font = "Calibri 18")
Label.grid (row = 0, column = 3, pady = 30)

#Agregar una variable
Variable = tk.Label(ventana, text="Latitud", bg="black", fg="white", font = "Calibri 14")
Variable.grid (row = 1, column = 0)

#Agregar primer recuadro
Cuadro = tk.Entry(ventana, font = "Calibri 14", justify = "left")
Cuadro.grid (row = 1, column = 5)

#Agregar el simbolo de grado fuera del recuadro
Text = tk.Label(ventana, text="°", bg="black", fg="white", font = "Calibri 14")
Text.grid (row = 1, column = 6)

#Agregar segunda variable
Variable_2 = tk.Label(ventana, text="Longitud", bg="black", fg="white", font = "Calibri 14")
Variable_2.grid (row = 1, column = 4)

#Agregar segundo recuadro
Cuadro_2 = tk.Entry(ventana, font = "Calibri 14", justify = "right")
Cuadro_2.grid (row = 1, column = 1)

#Agregar el simbolo de grado fuera del recuadro
Text_2 = tk.Label(ventana, text="°", bg="black", fg="white", font = "Calibri 14")
Text_2.grid (row = 1, column = 2)

##Grado, minutos y segundos
#Se repite el mismo procedimiento que el pasado
Label_2 = tk.Label(ventana, text = "Grados, Minutos y Segundos:", bg = "white", fg = "black", font = "Calibri 16")
Label_2.grid (row = 4, column = 3, pady = 30)


Variable_3 = tk.Label(ventana, text="Latitud", bg="black", fg="white", font = "calibri 14")
Variable_3.grid (row = 5, column = 0)


Cuadro_3 = tk.Entry(ventana, font = "Calibri 14", justify = "left")
Cuadro_3.grid (row = 5, column = 1)

Texto = tk.Label(ventana, text="°", bg="black", fg="white", font = "Calibri 14")
Texto.grid (row = 5, column = 2)

Cuadro_3_1 = tk.Entry(ventana, font = "Calibri 14", justify = "left")
Cuadro_3_1.grid (row = 5, column = 3)

Texto_2 = tk.Label(ventana, text= "'", bg="black", fg="white", font = "Calibri 14")
Texto_2.grid (row = 5, column = 4)


Cuadro_3_2 = tk.Entry(ventana, font = "Calibri 14", justify = "left")
Cuadro_3_2.grid (row = 5, column = 5,)

Texto_3 = tk.Label(ventana, text="''", bg="black", fg="white", font = "Calibri 15")
Texto_3.grid (row = 5, column = 6)

######################################
Variable_4 = tk.Label(ventana, text="Longitud", bg="black", fg="white", font = "Calibri 14")
Variable_4.grid (row = 6, column = 0)


Cuadro_4 = tk.Entry(ventana, font = "Calibri 14", justify = "left")
Cuadro_4.grid (row = 6, column = 1)

Texto_4 = tk.Label(ventana, text="°", bg="black", fg="white", font = "Calibri 14")
Texto_4.grid (row = 6, column = 2)

Cuadro_4_1 = tk.Entry(ventana, font = "Calibri 14", justify = "left")
Cuadro_4_1.grid (row = 6, column = 3)

Texto_5 = tk.Label(ventana, text= "'", bg="black", fg="white", font = "Calibri 14")
Texto_5.grid (row = 6, column = 4)


Cuadro_4_2 = tk.Entry(ventana, font = "Calibri 14", justify = "left")
Cuadro_4_2.grid (row = 6, column = 5)

Texto_6 = tk.Label(ventana, text="''", bg="black", fg="white", font = "Calibri 14")
Texto_6.grid (row = 6, column = 6)


# Muestra de resultados
textoResult = tk.Text(ventana)
textoResult.grid(row = 8, column = 1, columnspan = 8)

# Cálculo de conversión
def resultados_1():
    textoResult.delete(1.0, tk.END)
    lat = float(Cuadro.get())
    lon = float(Cuadro_2.get())
    
    ## DD -> DMS
    grados_lat = abs(int(lat))
    Grados = abs(float((lat)))-abs(int(lat))
    Minutos = int(Grados * 60)
    minutos2 = float(Grados *60)
    a = abs(float((minutos2)))-abs(int(minutos2))
    Segundos = float(a*60)
    if lat >= 0:
        hem_lat = "N"
    else:
        hem_lat = "S"
    textoResult.insert(tk.END, f" {grados_lat}, ° , {Minutos}, ' , {Segundos}, '' , {hem_lat}\n")
    
    grados_lon = abs(int(lon))
    Grados_2 = abs(float((lon)))-abs(int(lon))
    minutos = int(Grados_2 * 60)
    Minutos_2 = float(Grados_2 *60)
    deci_grados_min2 = abs(float((Minutos_2)))-abs(int(Minutos_2))
    Segundos_2 = float(deci_grados_min2*60)
    if lon >= 0:
        hem_lon = "E"
    else:
        hem_lon = "W"
    textoResult.insert(tk.END, f" {grados_lon}, ° , {minutos}, ' , {Segundos_2}, '' , {hem_lon}\n")

#Cálculo de Conversión
def resultados_2():
    textoResult.delete(1.0, tk.END)
    Grados = float(Cuadro_3.get())
    Minutos = float(Cuadro_3_1.get())
    Segundos = float(Cuadro_3_2.get())
    Grados_2 = float(Cuadro_4.get())
    Minutos_2 = float(Cuadro_4_1.get())
    Segundos_2 = float(Cuadro_4_2.get())
    
    
    ## DMS -> DD
    min_x = Segundos_2/60 + Minutos_2
    grados_x = round(((min_x)/60 + Grados_2), 3)
    textoResult.insert(tk.END, f" {grados_x}, °\n")
    
#Botones de cálculos de DMS como DD
boton_calculo = tk.Button(text = "Calcular DMS", font= 'Calibri 12', command = resultados_1)
boton_calculo.grid(row = 3, column = 3, pady = 30)

boton_calculo_2 = tk.Button(text = "Calcular DD", font= 'Calibri 12', command = resultados_2)
boton_calculo_2.grid(row = 7, column = 3, pady = 30)

#Titulo de la ventana
ventana.title("Conversor de Coordenadas")
# Ejecutar el GUI
ventana.mainloop()