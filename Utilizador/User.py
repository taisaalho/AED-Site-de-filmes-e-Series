import os
from tkinter import *
from tkinter import messagebox

user="User.txt"

#Main Window

mainWindow=Tk()
mainWindow.geometry("700x600")
mainWindow.title("")        #Nome do site
mainWindow.resizable(1,1)


#Register window

LSWindow=Tk()
LSWindow.geometry("100x50")
LSWindow.title("Register")
LSWindow.resizable(0.0)

Login=StringVar()
SignIn=StringVar()


Username=StringVar()
Password=StringVar()

username_lable = Label(LSWindow, text="Username")
username_entry = Entry(LSWindow, textvariable=Username)
password_lable = Label(LSWindow, text="Password")
password_entry = Entry(LSWindow, textvariable=Password, show='*')

 

#Buttons

#Button Login

logButton = Button 

#Button Sign In

signButton = Button

#Button Create Account

CreateAccButton = Button

#Button Enter

EnterButton = Button


#Funções
def Signin():
    criarConta = txt_texto.get("1.0","end")
    f = open(user,"w",encoding="utf-8")
    f.write(criarConta)
    f.close

def LogIn():
    f = open(user,"r",encoding="utf-8")
    linha = f.readlines()
    f.close
    txt_user.delete("1.0","end")
    for lin in linha:
        txt_user.insert("end",lin)

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return


#Pop Up
