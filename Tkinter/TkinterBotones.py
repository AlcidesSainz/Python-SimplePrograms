from tkinter import *
import random
import tkinter
from tkinter import messagebox

#Creando las funciones de las opciones
#Primera funcion en caso de SI
def CasoSi():
    messagebox.showinfo(message="Sabia que dirias que SI",title="")
    ventana.destroy()

def moverBoton(event):
    x2 =random.randint(10,400)
    y2 = random.randint(10,400)
    botonNo.place(x=x2,y=y2)

#Creando la ventana de la interfaz grafica 
ventana =Tk()

#Dimensiones de la ventana
ventana.geometry("600x480")

#Agregando un icono a la ventana
ventana.iconbitmap("C:/Users/alcid/Documents/MIS COSAS/Instituto/Programacion 1/Python/Tkinter/love.ico")

#Asignandole un color a la interfaz (#FFC0CB es el color rosado)
ventana.configure(background='#FFC0CB')

#Poniendole titulo a la interfaz
ventana.title("Responde")

#Se crea una variable llamada titulo donde se va a ingresar el texto del titulo de la interfas
#Label significa etiqueta ya que esta funcion es la encargada de crear un texto y darle formato
#bg(background) se refiere al fondo 
#fg(foreground) es la funcion encargada de darle color al texto,tamanio y fuente
titulo = Label(ventana,text="¿Quieres ser mi novia?",bg="#FFC0CB",fg="black",font=("Comic Sans MS",30))

#Posicionando el texto 
titulo.place(x=90,y=60)

#Creando el primer boton de las dos opciones
botonSi = Button(ventana,text="SI",width=5,height=1,font=("Comic Sans MS",30),bg = "red",fg="White",command=CasoSi)
botonSi.place(x=100,y=220)

#Creando el segundo boton
botonNo = Button(ventana,text="NO",width=5,height=1,font=("Comic Sans MS",30),bg = "red",fg="White")
#UTilizado para posicionar en la interfaz
botonNo.place(x=350,y=220)

botonNo.bind("<Enter>",moverBoton)
botonNo.bind("<Leave>",moverBoton)

#Permite que la ventana no se cierre y se siga ejecutando
ventana.mainloop()