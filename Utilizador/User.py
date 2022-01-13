from curses import window
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

user="User.txt"


#Main Window

mainWindow=Tk()
mainWindow.geometry("700x600")
mainWindow.title("")        #Nome do site
mainWindow.resizable(1,1)


#Registo window

RWindow=mainWindow(mainWindow)
RWindow.geometry("100x50")
RWindow.title("Register")
RWindow.resizable(0.0)

Username=StringVar()
Password=StringVar()

username_lable = Label(RWindow, text="Username")
username_entry = Entry(RWindow, textvariable=Username)
password_lable = Label(RWindow, text="Password")
password_entry = Entry(RWindow, textvariable=Password, show='*')


#Log in Window
 
LWindow=mainWindow(mainWindow)
LWindow.geometry("100x50")
LWindow.title("Register")
LWindow.resizable(0.0)

Username=StringVar()
Password=StringVar()

username = Label(LWindow, text="Username")
username = Entry(LWindow, textvariable=Username)
password = Label(LWindow, text="Password")
password = Entry(LWindow, textvariable=Password, show='*')


#Buttons

#Button Login

logButton = Button (mainWindow,text="Log In",relief="sunken",command=LogIn ,width=10,height=1)
logButton.place(x=500,y=50)

#Button Sign In

registoButton = Button(mainWindow,text="Registo",relief="sunken",command=Registar ,width=10,height=1)
registoButton.place(x=600,y=50)


#Funções
def Registar(username,password):
    if username == "" or password == "":
        messagebox.showerror("Criar Conta", "O username e a password não podem ser vazios!")
        return         
    f=open(user, "r", encoding="utf-8")
    listaUsers = f.readlines()
    f.close()
    for linha in listaUsers:
        fields = linha.split(";")
        if fields[0] == username:
            messagebox.showerror("Criar Conta", "Já existe um utilizador com esse username!")
            return 
    f = open(user, "a")
    linha = username + ";" + password + "\n"
    f.write(linha)
    f.close()
    messagebox.showinfo("Criar Conta", "Conta criada com sucesso!")

def LogIn(username,password):
    f=open(user, "r", encoding="utf-8")
    listaUsers = f.readlines()
    f.close()
    for linha in listaUsers:
        fields = linha.split(";")
        if fields[0] == username and fields[1][:-1] == password:
            msg = "Bem-Vindo " + username
            messagebox.showinfo("Iniciar Sessão", msg)
            return username
    messagebox.showerror("Iniciar Sessão", "O UserName ou a Password estão incorretos!")
    return ""
 

#Pop Up



mainWindow.mainloop()