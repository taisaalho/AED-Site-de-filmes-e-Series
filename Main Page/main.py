from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import ttk # treeview



# Dimensões e Visual

mainWindow=tk.Tk()
mainWindow.title("You Chose!")        #Nome do site
mainWindow.resizable(0,0)
mainWindow.geometry("900x700")
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

Login = Button(mainWindow, text="Login",width=8,height=2)
Login.place(x=680,y=25)

Registo = Button(mainWindow,text="Registo",width=8,height=2)
Registo.place(x=750,y=25)

Pesquisa = Button(mainWindow,text="Pesquisa",width=60,height=2)
Pesquisa.place(x=200,y=25)

Logo = Label(mainWindow,text="You Chose!",width=11,height=2,font="Helvica",bg="LightSteelBlue4",highlightthickness=0)
Logo.place(x=45,y=25)

#Top Rated

TRlabel = Label(mainWindow,text="TOP RATED",relief=SUNKEN)
TRlabel.place(x=420,y=370)

#Imagem - TOP 1

imagemAvatar = Image.open("Main Page//Avatar.jpg")
imgAvatar = imagemAvatar.resize((250,229), Image.ANTIALIAS)
AvatarResized = ImageTk.PhotoImage(imgAvatar)

top1_canvas = Canvas(mainWindow,width=250,height=225,bg="gray")
top1_canvas.place(x=64,y=400)
top1_canvas.create_image(127,112,image = AvatarResized)

#Button TOP 1

top1_label = Button(mainWindow,text="Avatar the Last Airbend - TOP OVERALL")
top1_label.place(x=86,y=640)

#Image TOP 2

imagemRM = Image.open("Main Page//rick-morty-portal.jpg")
imgRM = imagemRM.resize((250,229), Image.ANTIALIAS)
RMResized = ImageTk.PhotoImage(imgRM)

top2_canvas = Canvas(mainWindow,width=250,height=225,bg="gray")
top2_canvas.place(x=324,y=400)
top2_canvas.create_image(127,112,image = RMResized)

#Button TOP 2

top2_label = Button(mainWindow,text="Rick and Morty - TOP SERIES")
top2_label.place(x=372,y=640)

#Imagem TOP 3

imagemSA = Image.open("Main Page//spirited-away.jpg")
imgSA = imagemSA.resize((250,229), Image.ANTIALIAS)
SAResized = ImageTk.PhotoImage(imgSA)

top3_canvas = Canvas(mainWindow,width=250,height=225,bg="gray")
top3_canvas.place(x=584,y=400)
top3_canvas.create_image(127,112,image = SAResized)

#Button TOP 3

top3_label = Button(mainWindow,text="Spirit Away - TOP FILME")
top3_label.place(x=648,y=640)


#Recomendado

Recomendo = LabelFrame(mainWindow,height=255,width=390,relief="sunken",text="RECOMENDADO A VER!!")
Recomendo.place(x=30,y=100)

imagemKO = Image.open("Main Page//knives_out_ver13.jpg")
imgKO = imagemKO.resize((235,200), Image.ANTIALIAS)
KOResized = ImageTk.PhotoImage(imgKO)

nov_canvas = Canvas(Recomendo,width=230,height=200,bg="gray")
nov_canvas.place(x=80,y=20)
nov_canvas.create_image(115,100,image = KOResized)

Recomendado = Button(Recomendo,width=10,height=1,text="Knives Out",command="8-Knives Out")     
Recomendado.place(x=156,y=10)


#Novo

Novo = LabelFrame(mainWindow,height=255,width=390,relief="sunken",text="NOVO!!")
Novo.place(x=480,y=100)

imagemSB = Image.open("Main Page//shadow-bone.jpg")
imgSB = imagemSB.resize((235,200), Image.ANTIALIAS)
SBResized = ImageTk.PhotoImage(imgSB)

nov_canvas = Canvas(Novo,width=230,height=200,bg="gray")
nov_canvas.place(x=80,y=20)
nov_canvas.create_image(115,100,image = SBResized)

NoV = Button(Novo,width=10,height=1,text="Shadow Bone")
NoV.place(x=156,y=10)


#Imagem Utilizador

imagemUT = Image.open("Main Page//747376.png")
imgUT = imagemUT.resize((60,54), Image.ANTIALIAS)
UTResized = ImageTk.PhotoImage(imgUT)

utilizador_canvas = Canvas(mainWindow,width=60,height=54,bg="LightSteelBlue4",bd=0,highlightthickness=0)
utilizador_canvas.place(x=827,y=18)
utilizador_canvas.create_image(30,27,image = UTResized)


mainWindow.mainloop() 
