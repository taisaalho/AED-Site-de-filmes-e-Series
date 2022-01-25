
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog


# Dimensões e Visual

mainWindow=tk.Tk()
mainWindow.title("You Chose!")        #Nome do site
mainWindow.resizable(0,0)
mainWindow.geometry("900x700")
mainWindow.iconbitmap() #Icon 
mainWindow.configure(bg="LightSteelBlue4")


#Funções 

user = "User.txt"

#Login

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

#Registo

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

#Pesquisa



#Ir para Top 1



#Ir para Top 2



#Ir para Top 3



#Header

Login = Button(mainWindow, text="Login",width=8,height=2,function=LogIn)
Login.place(x=680,y=25)

Registo = Button(mainWindow,text="Registo",width=8,height=2)
Registo.place(x=750,y=25)

Pesquisa = Button(mainWindow,text="Pesquisa",width=60,height=2,function=Pesquisa)
Pesquisa.place(x=200,y=25)


#Top Rated

#Imagem - TOP 1

imagemAvatar = Image.open("Main Page//Avatar.jpg")
imgAvatar = imagemAvatar.resize((250,229), Image.ANTIALIAS)
AvatarResized = ImageTk.PhotoImage(imgAvatar)

top1_canvas = Canvas(mainWindow,width=250,height=225,bg="gray")
top1_canvas.place(x=59,y=380)
top1_canvas.create_image(127,112,image = AvatarResized)

#Button TOP 1

top1_label = Button(mainWindow,text="Avatar the Last Airbend - Top Overall")
top1_label.place(x=87,y=620)

#Image TOP 2

imagemRM = Image.open("Main Page//rick-morty-portal.jpg")
imgRM = imagemRM.resize((250,229), Image.ANTIALIAS)
RMResized = ImageTk.PhotoImage(imgRM)

top2_canvas = Canvas(mainWindow,width=250,height=225,bg="gray")
top2_canvas.place(x=324,y=380)
top2_canvas.create_image(127,112,image = RMResized)

#Button TOP 2

top2_label = Button(mainWindow,text="Rick and Morty - Top Series")
top2_label.place(x=372,y=620)

#Imagem TOP 3

imagemSA = Image.open("Main Page//spirited-away.jpg")
imgSA = imagemSA.resize((250,229), Image.ANTIALIAS)
SAResized = ImageTk.PhotoImage(imgSA)

top3_canvas = Canvas(mainWindow,width=250,height=225,bg="gray")
top3_canvas.place(x=584,y=380)
top3_canvas.create_image(127,112,image = SAResized)

#Button TOP 3

top3_label = Button(mainWindow,text="Spirit Away - TOP FILME")
top3_label.place(x=645,y=620)


#Recomendado

Recomendado = Button(mainWindow,text="Recomendado",width=119,height=15)
Recomendado.place(x=30,y=100)




mainWindow.mainloop() 
