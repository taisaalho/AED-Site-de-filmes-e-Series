from json.tool import main
from tkinter import *
from tkinter import messagebox
import tkinter as tk


# Dimensões e Visual

mainWindow=tk.Tk()
mainWindow.title("You Chose")        #Nome do site
mainWindow.resizable(0,0)
mainWindow.geometry("900x600")
mainWindow.iconbitmap() #Icon 
mainWindow.configure(bg="grey")

#Buttons

Login = Button(mainWindow, text="Login",width=8,height=2)
Login.place(x=750,y=25)

Registo = Button(mainWindow,text="Registo",width=8,height=2)
Registo.place(x=820,y=25)

Pesquisa = Button(mainWindow,text="Pesquisa",width=60,height=2)
Pesquisa.place(x=250,y=25)

#Funções dos buttons









mainWindow.mainloop() 
