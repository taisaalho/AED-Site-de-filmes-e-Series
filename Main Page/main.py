
from calendar import c
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog


# Dimensões e Visual

mainWindow=tk.Tk()
mainWindow.title("You Chose")        #Nome do site
mainWindow.resizable(0,0)
mainWindow.geometry("900x600")
mainWindow.iconbitmap() #Icon 
mainWindow.configure(bg="LightSteelBlue4")


#Header

Login = Button(mainWindow, text="Login",width=8,height=2)
Login.place(x=680,y=25)

Registo = Button(mainWindow,text="Registo",width=8,height=2)
Registo.place(x=750,y=25)

Pesquisa = Button(mainWindow,text="Pesquisa",width=60,height=2)
Pesquisa.place(x=200,y=25)


#Funções 

#Login



#Registo



#Pesquisa



#Ir para Top 1



#Ir para Top 2



#Ir para Top 3




#Top Rated

#Imagem - TOP 1

imagemAvatar = ImageTk.PhotoImage(Image.open("Avatar.jpg"))
top1_canvas = Canvas(mainWindow,width=250,height=153,bd=2)
resized_image= imagemAvatar.resize((300,205), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

top1_canvas.place(x=59,y=380)
top1_canvas.create_image(10,19,image = imagemAvatar)

#Button TOP 1.

top1_label = Button(mainWindow,text="Avatar")
top1_label.place(x=164,y=550)

#Button TOP 2

Top2 = Button(mainWindow,text="Top2",width=35,height=10)
Top2.place(x=324,y=380)
top2_label = Label(mainWindow,text="NOME")
top2_label.place(x=429,y=550)

#Button TOP 3

Top3 = Button(mainWindow,text="Top3",width=35,height=10)
Top3.place(x=584,y=380)
top3_label = Label(mainWindow,text="NOME")
top3_label.place(x=689,y=550)

#Recomendado

Recomendado = Button(mainWindow,text="Recomendado",width=119,height=15)
Recomendado.place(x=30,y=100)




mainWindow.mainloop() 
