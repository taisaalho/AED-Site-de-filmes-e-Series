from distutils import command
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import ttk # treeview
from tkVideoPlayer import TkinterVideo
import os


# Dimensões e Visual

mainWindow=tk.Tk()
mainWindow.title("You Chose!")        #Nome do site
mainWindow.resizable(0,0)
mainWindow.geometry("900x700")
mainWindow.configure(bg="LightSteelBlue4")
mainWindow.iconbitmap("item-pages\item-pages\Martynamru-Leather-Movie.ico")

#Funções 

user = "User.txt"

#Login e Registo


def login_registo():

    Users = "Main Page\\User.txt"

    mainWindow=Tk()
    mainWindow.geometry("700x600")
    mainWindow.title("")        #Nome do site
    mainWindow.resizable(1,1)

    user = "User.txt"

    
    def registo():
        global register_screen
        register_screen = Toplevel(mainWindow)
        register_screen.title("Register")
        register_screen.geometry("300x250")
    
        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()
    
        Label(register_screen, text="Please enter details below").pack()
        Label(register_screen, text="").pack()
        username_lable = Label(register_screen, text="Username * ")
        username_lable.pack()
        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()
        password_lable = Label(register_screen, text="Password * ")
        password_lable.pack()
        password_entry = Entry(register_screen, textvariable=password, show='*')
        password_entry.pack()
        Label(register_screen, text="").pack()
        Button(register_screen, text="Register", width=10, height=1, command = register_user).pack()
    
    
    # Designing window for login 
    
    def login():
        global login_screen
        login_screen = Toplevel(mainWindow)
        login_screen.title("Login")
        login_screen.geometry("300x250")
        Label(login_screen, text="Please enter details below to login").pack()
        Label(login_screen, text="").pack()
    
        global username_verify
        global password_verify
    
        username_verify = StringVar()
        password_verify = StringVar()
    
        global username_login_entry
        global password_login_entry
    
        Label(login_screen, text="Username * ").pack()
        username_login_entry = Entry(login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Password * ").pack()
        password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
        password_login_entry.pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    
    # Implementing event on register button
    
    def register_user():
    
        username_info = username.get()
        password_info = password.get()
    
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
    
        username_entry.delete(0, END)
        password_entry.delete(0, END)
    
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    
    # Implementing event on login button 
    
    def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
    
        list_of_files = os.listdir()
        if username1 in user:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                login_sucess()
    
            else:
                password_not_recognised()
    
        else:
            user_not_found()
    
    # Designing popup for login success
    
    def login_sucess():
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK", command=delete_login_success).pack()
    
    # Designing popup for login invalid password
    
    def password_not_recognised():
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(login_screen)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        Label(password_not_recog_screen, text="Invalid Password ").pack()
        Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
    
    # Designing popup for user not found
    
    def user_not_found():
        global user_not_found_screen
        user_not_found_screen = Toplevel(login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found").pack()
        Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
    
    # Deleting popups
    
    def delete_login_success():
        login_success_screen.destroy()
    
    
    def delete_password_not_recognised():
        password_not_recog_screen.destroy()
    
    
    def delete_user_not_found_screen():
        user_not_found_screen.destroy()
    
    
        mainWindow.mainloop()
    
 

#Pesquisa



#Ir para Top 1



#Ir para Top 2



#Ir para Top 3



#Knives Out

def function8():
    page = Toplevel()
    page.geometry("1150x540")
    page.title("Knives Out")
    page.resizable(0, 0)
    page.iconbitmap("item-pages\\item-pages\\Martynamru-Leather-Movie.ico")


    #Canvas para póster
    poster_space = Canvas(page, width=298, height=441, bd=2, relief="sunken")
    poster_space.place(x=20, y=20)

    #Imagem póster
    img = PhotoImage(file="knives-out-poster.gif")
    poster_space.create_image(253, 375, image=img)

    #Campo de título
    titulo = Label(page, text="Knives Out (2019)", fg="#5E239D", font=("Calisto MT", "16", "bold"))
    titulo.place(x=350, y=20)

    #Campo de Categorias
    cat = Label(page, text="Categorias:", fg="blue", font=("Calisto MT", "10", "bold"))
    cat.place(x=350, y=60)

    cat2 = Label(page, text="Comédia, Mistério", font=("Calisto MT", "10"))
    cat2.place(x=420, y=60)

    #Classificação
    clas = Label(page, text="Classificação:", fg="blue", font=("Calisto MT", "10", "bold"))
    clas.place(x=350, y=80)

    clas2 = Label(page, text="7.9", font=("Calisto MT", "10"))
    clas2.place(x=435, y=80)

    #Elenco
    cast = Label(page, text="Elenco:", fg="blue", font=("Calisto MT", "10", "bold"))
    cast.place(x=350, y=100)

    cast2 = Label(page, text="Daniel Craig, Jamie Lee Curtis", font=("Calisto MT", "10"))
    cast2.place(x=400, y=100)

    #Campo de descrição
    desc = Text(page, height=6, width=52, font=("Calisto MT", "10", "bold"))
    desc.place(x=340, y=125)
    desc.insert(1.0, "Depois de fazer 85 anos, Harlan Thrombey, um famoso escritor de histórias policiais, é encontrado morto. Contratado para investigar o caso, o detetive Benoit Blanc descobre que, entre os funcionários misteriosos e a família conflituosa de Harlan, todos podem ser considerados suspeitos do crime.")
    desc.config(state="disabled")
    desc.config(wrap=WORD)

    #Campo de trailer
    trailer_space = Canvas(page, bg="gray", width=370, height=268, bd=2, relief="sunken")
    trailer_space.place(x=335, y=250)

    videoplayer = TkinterVideo(trailer_space, scaled=True, pre_load=False)
    videoplayer.load(r"knives-out-trailer.mp4")

    #Buttons play/pause
    def playVideo() :
        videoplayer.play()

    def pauseVideo():
        videoplayer.pause()

    btn_play = Button(trailer_space, bg="blue", text="Play", height=1, width=8, fg="white", font=("Calisto MT", "8", "bold"),command=playVideo())
    btn_play.place(x=20, y=230)

    btn_pause = Button(trailer_space, bg="blue", text="Pause", height=1, width=8, fg="white", font=("Calisto MT", "8", "bold"), command = pauseVideo())
    btn_pause.place(x=100, y=230)

    #Check button, marcar como visto e adicionar aos favoritos
    val = IntVar()
    val1 = IntVar()

    check1 = Checkbutton(page, text="Adicionar aos favoritos",variable = val)
    check2 = Checkbutton(page, text="Marcar como visto", variable = val1)

    check1.place(x=25, y=480)
    check2.place(x=25, y=505)

    def salvar_alteracoes():

        if val.get() == 1 and val1.get() == 0:
            f = open("lista_favoritos.txt","a")
            frase = "Knives Out (2019)" + "\n"
            f.write(frase)
            f.close

        elif val.get() == 1 and val1.get() == 1:
            f = open("lista_vistos.txt", "a")
            frase = "Knives Out (2019)" +"\n"
            f.write(frase)
            f.close
            f = open("lista_favoritos.txt","a")
            frase = "Knives Out (2019)" + "\n"
            f.write(frase)
            f.close
        elif val.get() == 0 and val1.get() == 1:
            f=open("lista_vistos.txt", "a")
            frase = "Knives Out (2019)" + "\n"
            f.write(frase)
            f.close

    def comment():
        linha=txt_coment.get("1.0","end")
        ficheiro="com_knivesout.txt"
        f=open(ficheiro,"w", encoding="utf-8")
        f.write(linha)
        f.close
        f=open(ficheiro,"r",encoding="utf-8")
        ficheiro=f.readlines()
        f.close
        for linha in ficheiro:
            lbox_coment.insert("end",linha)
        txt_coment.delete("1.0","end")
        txt_coment("end", "")

    def selecao_item(event):
        indice = lbox_coment.curselection()
        texto = lbox_coment.get(indice)
        coment.set(texto)

    def remover():
        lbox_coment.delete(lbox_coment.curselection())
        coment.set("")
        f = open("com_knivesout.txt", "w", encoding="utf-8")
        cont = lbox_coment.size()
        for i in range(cont):
            com = lbox_coment.get(i) 
            if com.find("\n") == -1:
                com = com + "\n"
            f.write(com)
        f.close()

    def read_comment():
        f=open("com_knivesout.txt", "r")
        ficheiro=f.readlines()
        f.close()
        for linha in ficheiro:
            lbox_coment.insert("end",linha)
        txt_coment.delete("1.0","end")
        txt_coment("end", "")

    def num_likes():
        f=open("like_knivesout.txt", "r", encoding="utf-8")
        ficheiro=f.readlines()
        f.close()
        count=0
        for linha in ficheiro:
            count=count+1
        count_likes.set(str(count))

    def give_like():
        if rd_like.get()==True:
            f=open("like_knivesout.txt","a")
            frase="Like"+"\n"
            f.write(frase)
            f.close
        num_likes()

    #Button salva dados do filme
    favButton = Button(page, text="Salvar alterações",bg = "#FA6B6B",fg = "black",relief = "solid",bd = 2,font = "Arial 11",command=salvar_alteracoes)
    favButton.place(x=200, y=490) 

    #Campo likes/comentários
    eval_space = Canvas(page, bg="gray", width=400, height=500, bd=2, relief="sunken")
    eval_space.place(x=720, y=20)

    #Campo de likes
    like_space = LabelFrame(eval_space, text="Likes", width=380, height=60, bd=2, relief="raised", fg="red", font=("Calisto MT", "10", "bold"))
    like_space.place(x=15, y=15)

    rd_like=IntVar()

    rd_like=Checkbutton(like_space,text="Like",font=("Helvetica", 10) ,variable=rd_like, command=give_like)
    rd_like.place(x=15,y=7)

    lbl_count_likes=Label(like_space, text="Nº de Likes:", font=("Helvetica", 9))
    lbl_count_likes.place(x=70, y=10)

    count_likes = StringVar()
    txt_count_likes=Entry(like_space, width = 5, textvariable= count_likes)
    txt_count_likes.place(x=140, y=10)

    #Campo de comentários
    com_space = LabelFrame(eval_space, text="Comentários", width=380, height=410, bd=2, relief="raised", fg="red", font=("Calisto MT", "10", "bold"))
    com_space.place(x=15, y=85)

    coment = StringVar()

    #Button
    btn_guardar=Button(com_space, text="Comentar", width=10, height=2 , fg="blue", command=comment)
    btn_guardar.place(x=15, y=30)

    btn_limpar=Button(com_space, text="Apagar", width=10, height=2, fg="blue", command=remover)
    btn_limpar.place(x=120, y=30)

    btn_ler=Button(com_space, text="Ver comentarios", width=15, height=2, fg="blue", command=read_comment)
    btn_ler.place(x=220, y=30)

    #Label
    lbl_dcom=Label(com_space, text="Deixe aqui o seu comentario:", bd=2)
    lbl_dcom.place(x=15,y=80)

    #text
    txt_coment=Text(com_space, width=40, height=3, relief="sunken", bd=3)
    txt_coment.place(x=15, y=100)

    #Label
    lbl_com=Label(com_space, text="Comentários", bd=2)
    lbl_com.place(x=15,y=157)

    #listbox
    lbox_coment=Listbox(com_space, width=55, height=12, bd="3", selectmode = "single", selectbackground="blue")
    lbox_coment.place(x=15, y= 180)
    lbox_coment.bind("<<ListboxSelect>>", selecao_item)

    page.mainloop()


#Shadow Bone

def function16():
    page = Toplevel()
    page.geometry("1150x540")
    page.title("Shadow and Bone")
    page.resizable(0, 0)
    page.iconbitmap("imagens\\Martynamru-Leather-Movie.ico")


    #Canvas para póster
    poster_space = Canvas(page, width=298, height=441, bd=2, relief="sunken")
    poster_space.place(x=20, y=20)

    #Imagem póster
    img = PhotoImage(file="item-pages\\item-pages\\1-Aquaman\\16-Shadow and Bone\\shadow-and-bone-poster.gif")
    poster_space.create_image(253, 375, image=img)

    #Campo de título
    titulo = Label(page, text="Shadow and Bone (2021)", fg="#5E239D", font=("Calisto MT", "16", "bold"))
    titulo.place(x=350, y=20)

    #Campo de Categorias
    cat = Label(page, text="Categorias:", fg="blue", font=("Calisto MT", "10", "bold"))
    cat.place(x=350, y=60)

    cat2 = Label(page, text="Fantasia, Mistério", font=("Calisto MT", "10"))
    cat2.place(x=420, y=60)

    #Classificação
    clas = Label(page, text="Classificação:", fg="blue", font=("Calisto MT", "10", "bold"))
    clas.place(x=350, y=80)

    clas2 = Label(page, text="7.7", font=("Calisto MT", "10"))
    clas2.place(x=435, y=80)

    #Elenco
    cast = Label(page, text="Elenco:", fg="blue", font=("Calisto MT", "10", "bold"))
    cast.place(x=350, y=100)

    cast2 = Label(page, text="Jessie Mei Li, Ben Barnes", font=("Calisto MT", "10"))
    cast2.place(x=400, y=100)

    #Campo de descrição
    desc = Text(page, height=6, width=52, font=("Calisto MT", "10", "bold"))
    desc.place(x=340, y=125)
    desc.insert(1.0, "Num mundo dividido em dois por uma barreira maciça de escuridão perpétua, onde criaturas sobrenaturais festejam em carne humana, uma jovem soldada descobre um poder que pode finalmente unir seu país. Mas enquanto ela luta para aprimorar seu poder, forças perigosas tramam contra ela.")
    desc.config(state="disabled")
    desc.config(wrap=WORD)

    #Campo de trailer
    trailer_space = Canvas(page, bg="gray", width=370, height=268, bd=2, relief="sunken")
    trailer_space.place(x=335, y=250)

    videoplayer = TkinterVideo(trailer_space, scaled=True, pre_load=False)
    videoplayer.load(r"Main Page\\8-Knives Out\\knives-out-trailer.mp4")

    #Buttons play/pause
    def playVideo() :
        videoplayer.play()

    def pauseVideo():
        videoplayer.pause()

    btn_play = Button(trailer_space, bg="blue", text="Play", height=1, width=8, fg="white", font=("Calisto MT", "8", "bold"), command = playVideo)
    btn_play.place(x=20, y=230)

    btn_pause = Button(trailer_space, bg="blue", text="Pause", height=1, width=8, fg="white", font=("Calisto MT", "8", "bold"), command = pauseVideo)
    btn_pause.place(x=100, y=230)

    #Check button, marcar como visto e adicionar aos favoritos
    val = IntVar()
    val1 = IntVar()

    check1 = Checkbutton(page, text="Adicionar aos favoritos",variable = val)
    check2 = Checkbutton(page, text="Marcar como visto", variable = val1)

    check1.place(x=25, y=480)
    check2.place(x=25, y=505)

    def salvar_alteracoes():

        if val.get() == 1 and val1.get() == 0:
            f = open("lista_favoritos.txt","a")
            frase = "Shadow and Bone (2021)" + "\n"
            f.write(frase)
            f.close

        elif val.get() == 1 and val1.get() == 1:
            f = open("lista_vistos.txt", "a")
            frase = "Shadow and Bone (2021)" +"\n"
            f.write(frase)
            f.close
            f = open("lista_favoritos.txt","a")
            frase = "Shadow and Bone (2021)" + "\n"
            f.write(frase)
            f.close
        elif val.get() == 0 and val1.get() == 1:
            f=open("lista_vistos.txt", "a")
            frase = "Shadow and Bone (2021)" + "\n"
            f.write(frase)
            f.close

    def comment():
        linha=txt_coment.get("1.0","end")
        ficheiro="com_shadow.txt"
        f=open(ficheiro,"w", encoding="utf-8")
        f.write(linha)
        f.close
        f=open(ficheiro,"r",encoding="utf-8")
        ficheiro=f.readlines()
        f.close
        for linha in ficheiro:
            lbox_coment.insert("end",linha)
        txt_coment.delete("1.0","end")
        txt_coment("end", "")

    def selecao_item(event):
        indice = lbox_coment.curselection()
        texto = lbox_coment.get(indice)
        coment.set(texto)

    def remover():
        lbox_coment.delete(lbox_coment.curselection())
        coment.set("")
        f = open("com_shadow.txt", "w", encoding="utf-8")
        cont = lbox_coment.size()
        for i in range(cont):
            com = lbox_coment.get(i) 
            if com.find("\n") == -1:
                com = com + "\n"
            f.write(com)
        f.close()

    def read_comment():
        f=open("com_shadow.txt", "r")
        ficheiro=f.readlines()
        f.close()
        for linha in ficheiro:
            lbox_coment.insert("end",linha)
        txt_coment.delete("1.0","end")
        txt_coment("end", "")

    def num_likes():
        f=open("like_shadow.txt", "r", encoding="utf-8")
        ficheiro=f.readlines()
        f.close()
        count=0
        for linha in ficheiro:
            count=count+1
        count_likes.set(str(count))

    def give_like():
        if rd_like.get()==True:
            f=open("like_shadow.txt","a")
            frase="Like"+"\n"
            f.write(frase)
            f.close
        num_likes()

    #Button salva dados do filme
    favButton = Button(page, text="Salvar alterações",bg = "#FA6B6B",fg = "black",relief = "solid",bd = 2,font = "Arial 11",command=salvar_alteracoes())
    favButton.place(x=200, y=490) 

    #Campo likes/comentários
    eval_space = Canvas(page, bg="gray", width=400, height=500, bd=2, relief="sunken")
    eval_space.place(x=720, y=20)

    #Campo de likes
    like_space = LabelFrame(eval_space, text="Likes", width=380, height=60, bd=2, relief="raised", fg="red", font=("Calisto MT", "10", "bold"))
    like_space.place(x=15, y=15)

    rd_like=IntVar()

    rd_like=Checkbutton(like_space,text="Like",font=("Helvetica", 10) ,variable=rd_like, command=give_like())
    rd_like.place(x=15,y=7)

    lbl_count_likes=Label(like_space, text="Nº de Likes:", font=("Helvetica", 9))
    lbl_count_likes.place(x=70, y=10)

    count_likes = StringVar()
    txt_count_likes=Entry(like_space, width = 5, textvariable= count_likes)
    txt_count_likes.place(x=140, y=10)

    #Campo de comentários
    com_space = LabelFrame(eval_space, text="Comentários", width=380, height=410, bd=2, relief="raised", fg="red", font=("Calisto MT", "10", "bold"))
    com_space.place(x=15, y=85)

    coment = StringVar()

    #Button
    btn_guardar=Button(com_space, text="Comentar", width=10, height=2 , fg="blue", command=comment())
    btn_guardar.place(x=15, y=30)

    btn_limpar=Button(com_space, text="Apagar", width=10, height=2, fg="blue", command=remover())
    btn_limpar.place(x=120, y=30)

    btn_ler=Button(com_space, text="Ver comentarios", width=15, height=2, fg="blue", command=read_comment)
    btn_ler.place(x=220, y=30)

    #Label
    lbl_dcom=Label(com_space, text="Deixe aqui o seu comentario:", bd=2)
    lbl_dcom.place(x=15,y=80)

    #text
    txt_coment=Text(com_space, width=40, height=3, relief="sunken", bd=3)
    txt_coment.place(x=15, y=100)

    #Label
    lbl_com=Label(com_space, text="Comentários", bd=2)
    lbl_com.place(x=15,y=157)

    #listbox
    lbox_coment=Listbox(com_space, width=55, height=12, bd="3", selectmode = "single", selectbackground="blue")
    lbox_coment.place(x=15, y= 180)
    lbox_coment.bind("<<ListboxSelect>>", selecao_item)

    page.mainloop()



#Header

Login = Button(mainWindow, text="Login",width=8,height=2,command=login_registo())
Login.place(x=680,y=25)

Registo = Button(mainWindow,text="Registo",width=8,height=2,command=login_registo())
Registo.place(x=750,y=25)

Pesquisa = Button(mainWindow,text="Pesquisa",width=60,height=2,command=pesquisa())
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

Recomendado = Button(Recomendo,width=10,height=1,text="Knives Out",command=lambda: function8())     
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

NoV = Button(Novo,width=10,height=1,text="Shadow Bone",command=lambda: function16())
NoV.place(x=156,y=10)


#Imagem Utilizador

imagemUT = Image.open("Main Page//747376.png")
imgUT = imagemUT.resize((60,54), Image.ANTIALIAS)
UTResized = ImageTk.PhotoImage(imgUT)

utilizador_canvas = Canvas(mainWindow,width=60,height=54,bg="LightSteelBlue4",bd=0,highlightthickness=0)
utilizador_canvas.place(x=827,y=18)
utilizador_canvas.create_image(30,27,image = UTResized)


mainWindow.mainloop() 
