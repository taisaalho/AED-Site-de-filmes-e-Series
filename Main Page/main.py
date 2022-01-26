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

global userAutenticado
userAutenticado = StringVar()

global panelUsers

#Login e Registo

#Registo

def registar(funcao, btnSessao):
   if userAutenticado.get() != "":     # SE JÁ EXISTE um user autenticado, a ieia é terminar sessão
      userAutenticado.set("")
      btnSessao.config(text = "Iniciar Sessão")
      return

   panelUsers.place(x=580, y=28)
# Username
   labelUsers = Label(panelUsers, text ="Username:")
   labelUsers.place(x=10, y= 10)
   userName = StringVar()
   txtUser = Entry(panelUsers, width=20, textvariable=userName)
   txtUser.place(x=80, y= 10)
#Password
   labelPass = Label(panelUsers, text ="Password:")
   labelPass.place(x=10, y= 60)
   userPass = StringVar()
   txtPass = Entry(panelUsers, width=20, textvariable = userPass, show = "*")
   txtPass.place(x=80, y= 60)
#Buttons
   if funcao == 1:   # Abre painel para criar conta
      btnUsers = Button(panelUsers, text = "Criar Conta", width = 12, height = 2, 
                 command = lambda: [criaConta(userName.get(), userPass.get()), fechaPanelUsers()])
      btnUsers.place(x=10, y= 110)
      btnCalcel = Button(panelUsers, text = "Cancelar", width = 12, height = 2, command = fechaPanelUsers)
      btnCalcel.place(x=120, y= 110)
   else:         # Abre painel para iniciar sessão
      btnUsers = Button(panelUsers, text = "Iniciar Sessão", width = 12, height = 2, 
                 command = lambda: iniciarSessao(userName.get(), userPass.get())   )
      btnUsers.place(x=10, y= 110)
      btnCalcel = Button(panelUsers, text = "Cancelar", width = 12, height = 2, command = fechaPanelUsers)
      btnCalcel.place(x=120, y= 110)

#Login
 
def iniciarSessao(userName, userPass):
   userAutenticado.set(validaConta(userName, userPass))
   if userAutenticado.get() != "":
      btnSessao.config(text = "Terminar Sessão")
      fechaPanelUsers()


#Pesquisa

def pesquisa():

    window=Tk()   
    window.title('Pesquisa')
    global screenHeight
    global screenWidth
    global appHeight, appWidth
    global x,y
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    appWidth = 900
    appHeight = 600
    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))

    ficheiro="lista_f_s.txt"

    def w_pesquisados():
        f=open("pesquisados.txt", "r")
        ficheiro=f.readlines()
        f.close
        for linha in ficheiro:
            lbox_filmes.insert("end",linha)
        

    def pes_nome():
        f=open("lista_f_s.txt", "r", encoding="utf-8")
        ficheiro=f.readlines()
        f.close()
        for linha in ficheiro:
            campos=linha.split(";")
            if campos[1]==filme.get():
                if campos[1] not in "pesquisados.txt":
                    f=open("pesquisados.txt","a")
                    frase=campos[1]+"\n"
                    f.write(frase)
                    f.close
        w_pesquisados()

    def pes_filme():
        if rd_a.get()==True:
            f=open("lista_f_s.txt", "r", encoding="utf-8")
            ficheiro=f.readlines()
            f.close()
            for linha in ficheiro:
                campos=linha.split(";")
                if campos[0]=="Filme":
                    if campos[1] not in "pesquisados.txt":
                        f=open("pesquisados.txt","a")
                        frase=campos[1]+"\n"
                        f.write(frase)
                        f.close
        pes_serie()

    def pes_serie():
        if rd_b.get()==True:
            f=open("lista_f_s.txt", "r", encoding="utf-8")
            ficheiro=f.readlines()
            f.close()
            for linha in ficheiro:
                campos=linha.split(";")
                if campos[0]=="Série":
                    if campos[1] not in "pesquisados.txt":
                        f=open("pesquisados.txt","a")
                        frase=campos[1]+"\n"
                        f.write(frase)
                        f.close
        w_pesquisados()


    def pes_ação():
        text1=""
        f=open("pesquisados.txt","w")
        f.write(text1)
        f.close()
        if rd_1.get()==True:
            f=open("lista_f_s.txt", "r", encoding="utf-8")
            ficheiro=f.readlines()
            f.close()
            for linha in ficheiro:
                campos=linha.split(";")
                if campos[2]=="Ação" or campos[3]=="Ação":
                    if campos[1] not in "pesquisados.txt":
                        f=open("pesquisados.txt","a")
                        frase=campos[1]+"\n"
                        f.write(frase)
                        f.close
        pes_animacao()

    def pes_animacao():
        if rd_2.get()==True:
            f=open("lista_f_s.txt", "r", encoding="utf-8")
            ficheiro=f.readlines()
            f.close()
            for linha in ficheiro:
                campos=linha.split(";")
                if campos[2]=="Animação" or campos[3]=="Animação":
                    if campos[1] not in "pesquisados.txt":
                        f=open("pesquisados.txt","a")
                        frase=campos[1]+"\n"
                        f.write(frase)
                        f.close
        pes_comedia()

    def pes_comedia():
        if rd_3.get()==True:
            f=open("lista_f_s.txt", "r", encoding="utf-8")
            ficheiro=f.readlines()
            f.close()
            for linha in ficheiro:
                campos=linha.split(";")
                if campos[2]=="Comédia" or campos[3]=="Comédia":
                    if campos[1] not in "pesquisados.txt":
                        f=open("pesquisados.txt","a")
                        frase=campos[1]+"\n"
                        f.write(frase)
                        f.close
        pes_fantasia()

    def pes_fantasia():
        if rd_4.get()==True:
            f=open("lista_f_s.txt", "r", encoding="utf-8")
            ficheiro=f.readlines()
            f.close()
            for linha in ficheiro:
                campos=linha.split(";")
                if campos[2]=="Fantasia" or campos[3]=="Fantasia":
                    if campos[1] not in "pesquisados.txt":
                        f=open("pesquisados.txt","a")
                        frase=campos[1]+"\n"
                        f.write(frase)
                        f.close
        pes_misterio()
        
    def pes_misterio():
        if rd_5.get()==True:
            f=open("lista_f_s.txt", "r", encoding="utf-8")
            ficheiro=f.readlines()
            f.close()
            for linha in ficheiro:
                campos=linha.split(";")
                if campos[2]=="Mistério" or campos[3]=="Mistério":
                    if campos[1] not in "pesquisados.txt":
                        f=open("pesquisados.txt","a")
                        frase=campos[1]+"\n"
                        f.write(frase)
                        f.close
        pes_filme()

    def select_filme(event):
        indice = lbox_filmes.curselection()
        texto = lbox_filmes.get(indice)
        print(texto)

    #Menu Window principal
    barra_Menu=Menu(window)

    sim_Menu=Menu(barra_Menu)
    barra_Menu.add_command(label="Pesquisa")
    barra_Menu.add_command(label="Sair", command=window.quit)

    window.configure(menu=barra_Menu)

    filme = StringVar()
    rd_a=IntVar()
    rd_b=IntVar()
    rd_1=IntVar()
    rd_2=IntVar()
    rd_3=IntVar()
    rd_4=IntVar()
    rd_5=IntVar()

    #Texto Window principal
    txt_pes=Entry(window, width=50, textvariable= filme)
    txt_pes.place(x=10, y=20)

    #Botão pesquisa por nome 
    button_name=Button(window, text="Pesquisar", width=10, height=1, fg="black", command=pes_nome)
    button_name.place(x=430, y=20)

    #Painel de filmes e series
    frame_tipo=LabelFrame(window, text="Tipo", width=140, height=90, relief="sunken", bd="3", fg="black")
    frame_tipo.place(x=10,y=60)

    rd_filme=Checkbutton(text="Filme", variable=rd_a)
    rd_filme.place(x=15,y=80)

    rd_serie=Checkbutton(text="Serie", variable=rd_b)
    rd_serie.place(x=15,y=110)

    #Painel das categorias
    frame_categoria=LabelFrame(window, text="Categoria", width=150, height=130, relief="sunken", bd="3", fg="black")
    frame_categoria.place(x=10, y=170)

    #Botão das categorias
    button_categorias=Button(window, text="Pesquisa", width=20, height=2, fg="black", relief="raised", command=pes_ação)
    button_categorias.place(x=230, y=210)

    #Seleção das categorias
    rd_açao=Checkbutton(text="Ação",variable=rd_1)
    rd_açao.place(x=15,y=190)

    rd_animacao=Checkbutton(text="Animação",variable=rd_2)
    rd_animacao.place(x=15,y=210)

    rd_comedia=Checkbutton(text="Comédia",variable=rd_3)
    rd_comedia.place(x=15,y=230)

    rd_fantasia=Checkbutton(text="Fantasia",variable=rd_4)
    rd_fantasia.place(x=15,y=250)

    rd_misterio=Checkbutton(text="Mistério",variable=rd_5)
    rd_misterio.place(x=15,y=270)

    lbox_filmes=Listbox(window,width=55, height=35, selectmode="single")
    lbox_filmes.place(x=540, y= 20)
    lbox_filmes.bind("<<ListboxSelect>>", select_filme)

    window.mainloop()


#Ir para Top 1

def function17():
    page = Toplevel()
    page.geometry("1150x540")
    page.title("Avatar: The Last Airbender (2005)")
    page.resizable(0, 0)
    page.iconbitmap("imagens\Martynamru-Leather-Movie.ico")


    #Canvas para póster
    poster_space = Canvas(page, width=298, height=441, bd=2, relief="sunken")
    poster_space.place(x=20, y=20)

    #Imagem póster
    img = PhotoImage(file="avatar-tlab-poster.gif")
    poster_space.create_image(253, 375, image=img)

    #Campo de título
    titulo = Label(page, text="Avatar: The Last Airbender (2005)", fg="#5E239D", font=("Calisto MT", "16", "bold"))
    titulo.place(x=350, y=20)

    #Campo de Categorias
    cat = Label(page, text="Categorias:", fg="blue", font=("Calisto MT", "10", "bold"))
    cat.place(x=350, y=60)

    cat2 = Label(page, text="Fantasia, Animação", font=("Calisto MT", "10"))
    cat2.place(x=420, y=60)

    #Classificação
    clas = Label(page, text="Classificação:", fg="blue", font=("Calisto MT", "10", "bold"))
    clas.place(x=350, y=80)

    clas2 = Label(page, text="9.3", font=("Calisto MT", "10"))
    clas2.place(x=435, y=80)

    #Elenco
    cast = Label(page, text="Elenco:", fg="blue", font=("Calisto MT", "10", "bold"))
    cast.place(x=350, y=100)

    cast2 = Label(page, text="Zach Tyler Eisen, Dante Basco", font=("Calisto MT", "10"))
    cast2.place(x=400, y=100)

    #Campo de descrição
    desc = Text(page, height=6, width=52, font=("Calisto MT", "10", "bold"))
    desc.place(x=340, y=125)
    desc.insert(1.0, "Preso durante um século dentro de um iceberg, Aang é um menino de 12 anos que agora está livre do gelo. Ele descobre que tem um destino extraordinário: ser o Avatar. Ele é responsável por garantir o equilíbrio entre os mestres dos quarto elementos, que estão divididos em quatro civilizações: as tribos da Água, da Terra, do Fogo e do Ar. Elas estão perdidas no meio de guerras e destruições. Agora, sua missão é restaurar a ordem do universo. Mas antes ele tem que aprender a dominar todos os elementos.")
    desc.config(state="disabled")
    desc.config(wrap=WORD)

    #Campo de trailer
    trailer_space = Canvas(page, bg="gray", width=370, height=268, bd=2, relief="sunken")
    trailer_space.place(x=335, y=250)

    videoplayer = TkinterVideo(trailer_space, scaled=True, pre_load=False)
    videoplayer.load(r"avatar-tlab-trailer.mp4")

    #Buttons play/pause
    def playVideo() :
        videoplayer.play()

    def pauseVideo():
        videoplayer.pause()

    btn_play = Button(trailer_space, bg="blue", text="Play", height=1, width=8, fg="white", font=("Calisto MT", "8", "bold"))#, command = playVideo)
    btn_play.place(x=20, y=230)

    btn_pause = Button(trailer_space, bg="blue", text="Pause", height=1, width=8, fg="white", font=("Calisto MT", "8", "bold"))#, command = pauseVideo)
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
            frase = "Avatar: The Last Airbender (2005)" + "\n"
            f.write(frase)
            f.close

        elif val.get() == 1 and val1.get() == 1:
            f = open("lista_vistos.txt", "a")
            frase = "Avatar: The Last Airbender (2005)" +"\n"
            f.write(frase)
            f.close
            f = open("lista_favoritos.txt","a")
            frase = "Avatar: The Last Airbender (2005)" + "\n"
            f.write(frase)
            f.close
        elif val.get() == 0 and val1.get() == 1:
            f=open("lista_vistos.txt", "a")
            frase = "Avatar: The Last Airbender (2005)" + "\n"
            f.write(frase)
            f.close

    def comment():
        linha=txt_coment.get("1.0","end")
        ficheiro="com_avatar.txt"
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
        f = open("com_avatar.txt", "w", encoding="utf-8")
        cont = lbox_coment.size()
        for i in range(cont):
            com = lbox_coment.get(i) 
            if com.find("\n") == -1:
                com = com + "\n"
            f.write(com)
        f.close()

    def read_comment():
        f=open("com_avatar.txt", "r")
        ficheiro=f.readlines()
        f.close()
        for linha in ficheiro:
            lbox_coment.insert("end",linha)
        txt_coment.delete("1.0","end")
        txt_coment("end", "")

    def num_likes():
        f=open("like_avatar.txt", "r", encoding="utf-8")
        ficheiro=f.readlines()
        f.close()
        count=0
        for linha in ficheiro:
            count=count+1
        count_likes.set(str(count))

    def give_like():
        if rd_like.get()==True:
            f=open("like_avatar.txt","a")
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


#Ir para Top 2

def function19():
    page = Toplevel()
    page.geometry("1150x540")
    page.title("Rick and Morty")
    page.resizable(0, 0)
    page.iconbitmap("imagens\Martynamru-Leather-Movie.ico")


    #Canvas para póster
    poster_space = Canvas(page, width=298, height=441, bd=2, relief="sunken")
    poster_space.place(x=20, y=20)

    #Imagem póster
    img = PhotoImage(file="rick-and-morty-poster.gif")
    poster_space.create_image(253, 375, image=img)

    #Campo de título
    titulo = Label(page, text="Rick and Morty (2013)", fg="#5E239D", font=("Calisto MT", "16", "bold"))
    titulo.place(x=350, y=20)

    #Campo de Categorias
    cat = Label(page, text="Categorias:", fg="blue", font=("Calisto MT", "10", "bold"))
    cat.place(x=350, y=60)

    cat2 = Label(page, text="Comédia, Animação", font=("Calisto MT", "10"))
    cat2.place(x=420, y=60)

    #Classificação
    clas = Label(page, text="Classificação:", fg="blue", font=("Calisto MT", "10", "bold"))
    clas.place(x=350, y=80)

    clas2 = Label(page, text="9.2", font=("Calisto MT", "10"))
    clas2.place(x=435, y=80)

    #Elenco
    cast = Label(page, text="Elenco:", fg="blue", font=("Calisto MT", "10", "bold"))
    cast.place(x=350, y=100)

    cast2 = Label(page, text="Justin Roiland, Spencer Grammer", font=("Calisto MT", "10"))
    cast2.place(x=400, y=100)

    #Campo de descrição
    desc = Text(page, height=6, width=52, font=("Calisto MT", "10", "bold"))
    desc.place(x=340, y=125)
    desc.insert(1.0, "Rick Sanchez é um cientista genial e alcoólatra que foi morar com a família de sua filha Beth, uma cirurgiã cardíaca de equinos. Ele divide seu tempo entre desenvolver projetos altamente tecnológicos em seu laboratório (garagem da casa de Beth) e levar seu neto de 14 anos Morty em aventuras perigosas e surreais pelo Multiverso. Combinados com tensões preexistentes dentro da família, esses eventos causam ao sensível Morty muito angústia em casa e na escola.")
    desc.config(state="disabled")
    desc.config(wrap=WORD)

    #Campo de trailer
    trailer_space = Canvas(page, bg="gray", width=370, height=268, bd=2, relief="sunken")
    trailer_space.place(x=335, y=250)

    videoplayer = TkinterVideo(trailer_space, scaled=True, pre_load=False)
    videoplayer.load(r"rick-and-morty-trailer.mp4")

    #Buttons play/pause
    def playVideo() :
        videoplayer.play()

    def pauseVideo():
        videoplayer.pause()

    btn_play = Button(trailer_space, bg="blue", text="Play", height=1, width=8, fg="white", font=("Calisto MT", "8", "bold"))#, command = playVideo)
    btn_play.place(x=20, y=230)

    btn_pause = Button(trailer_space, bg="blue", text="Pause", height=1, width=8, fg="white", font=("Calisto MT", "8", "bold"))#, command = pauseVideo)
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
            frase = "Rick and Morty (2013)" + "\n"
            f.write(frase)
            f.close

        elif val.get() == 1 and val1.get() == 1:
            f = open("lista_vistos.txt", "a")
            frase = "Rick and Morty (2013)" +"\n"
            f.write(frase)
            f.close
            f = open("lista_favoritos.txt","a")
            frase = "Rick and Morty (2013)" + "\n"
            f.write(frase)
            f.close
        elif val.get() == 0 and val1.get() == 1:
            f=open("lista_vistos.txt", "a")
            frase = "Rick and Morty (2013)" + "\n"
            f.write(frase)
            f.close

    def comment():
        linha=txt_coment.get("1.0","end")
        ficheiro="com_rickmorty.txt"
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
        f = open("com_rickmorty.txt", "w", encoding="utf-8")
        cont = lbox_coment.size()
        for i in range(cont):
            com = lbox_coment.get(i) 
            if com.find("\n") == -1:
                com = com + "\n"
            f.write(com)
        f.close()

    def read_comment():
        f=open("com_rickmorty.txt", "r")
        ficheiro=f.readlines()
        f.close()
        for linha in ficheiro:
            lbox_coment.insert("end",linha)
        txt_coment.delete("1.0","end")
        txt_coment("end", "")

    def num_likes():
        f=open("like_rickmorty.txt", "r", encoding="utf-8")
        ficheiro=f.readlines()
        f.close()
        count=0
        for linha in ficheiro:
            count=count+1
        count_likes.set(str(count))

    def give_like():
        if rd_like.get()==True:
            f=open("like_rickmorty.txt","a")
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


#Ir para Top 3

def function7():
    page = Toplevel()
    page.geometry("1150x540")
    page.title("Spirited Away")
    page.resizable(0, 0)
    page.iconbitmap("imagens\Martynamru-Leather-Movie.ico")


    #Canvas para póster
    poster_space = Canvas(page, width=298, height=441, bd=2, relief="sunken")
    poster_space.place(x=20, y=20)

    #Imagem póster
    img = PhotoImage(file="spirited-away-poster.gif")
    poster_space.create_image(253, 375, image=img)

    #Campo de título
    titulo = Label(page, text="Spirited Away (2001)", fg="#5E239D", font=("Calisto MT", "16", "bold"))
    titulo.place(x=350, y=20)

    #Campo de Categorias
    cat = Label(page, text="Categorias:", fg="blue", font=("Calisto MT", "10", "bold"))
    cat.place(x=350, y=60)

    cat2 = Label(page, text="Fantasia, Animação", font=("Calisto MT", "10"))
    cat2.place(x=420, y=60)

    #Classificação
    clas = Label(page, text="Classificação:", fg="blue", font=("Calisto MT", "10", "bold"))
    clas.place(x=350, y=80)

    clas2 = Label(page, text="8.6", font=("Calisto MT", "10"))
    clas2.place(x=435, y=80)

    #Elenco
    cast = Label(page, text="Elenco:", fg="blue", font=("Calisto MT", "10", "bold"))
    cast.place(x=350, y=100)

    cast2 = Label(page, text="Rumi Hiiragi, Miyu Irino", font=("Calisto MT", "10"))
    cast2.place(x=400, y=100)

    #Campo de descrição
    desc = Text(page, height=6, width=52, font=("Calisto MT", "10", "bold"))
    desc.place(x=340, y=125)
    desc.insert(1.0, "Chihiro e seus pais estão se a mudar para uma cidade diferente. A caminho da nova casa, o pai decide ir por um um atalho. Eles se deparam com uma mesa repleta de comida, embora ninguém esteja por perto. Chihiro sente o perigo, mas seus pais começam a comer. Quando anoitece, eles se transformam em porcos. Agora, apenas Chihiro pode salvá-los.")
    desc.config(state="disabled")
    desc.config(wrap=WORD)

    #Campo de trailer
    trailer_space = Canvas(page, bg="gray", width=370, height=268, bd=2, relief="sunken")
    trailer_space.place(x=335, y=250)

    videoplayer = TkinterVideo(trailer_space, scaled=True, pre_load=False)
    videoplayer.load(r"spirited-away-trailer.mp4")

    #Buttons play/pause
    def playVideo() :
        videoplayer.play()

    def pauseVideo():
        videoplayer.pause()

    btn_play = Button(trailer_space, bg="blue", text="Play", height=1, width=8, fg="white", font=("Calisto MT", "8", "bold"))#, command = playVideo)
    btn_play.place(x=20, y=230)

    btn_pause = Button(trailer_space, bg="blue", text="Pause", height=1, width=8, fg="white", font=("Calisto MT", "8", "bold"))#, command = pauseVideo)
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
            frase = "Spirited Away (2001)" + "\n"
            f.write(frase)
            f.close

        elif val.get() == 1 and val1.get() == 1:
            f = open("lista_vistos.txt", "a")
            frase = "Spirited Away (2001)" +"\n"
            f.write(frase)
            f.close
            f = open("lista_favoritos.txt","a")
            frase = "Spirited Away (2001)" + "\n"
            f.write(frase)
            f.close
        elif val.get() == 0 and val1.get() == 1:
            f=open("lista_vistos.txt", "a")
            frase = "Spirited Away (2001)" + "\n"
            f.write(frase)
            f.close

    def comment():
        linha=txt_coment.get("1.0","end")
        ficheiro="com_spirited.txt"
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
        f = open("com_spirited.txt", "w", encoding="utf-8")
        cont = lbox_coment.size()
        for i in range(cont):
            com = lbox_coment.get(i) 
            if com.find("\n") == -1:
                com = com + "\n"
            f.write(com)
        f.close()

    def read_comment():
        f=open("com_spirited.txt", "r")
        ficheiro=f.readlines()
        f.close()
        for linha in ficheiro:
            lbox_coment.insert("end",linha)
        txt_coment.delete("1.0","end")
        txt_coment("end", "")

    def num_likes():
        f=open("like_spirited.txt", "r", encoding="utf-8")
        ficheiro=f.readlines()
        f.close()
        count=0
        for linha in ficheiro:
            count=count+1
        count_likes.set(str(count))

    def give_like():
        if rd_like.get()==True:
            f=open("like_spirited.txt","a")
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

Login = Button(mainWindow, text="Login",width=8,height=2,)
Login.place(x=680,y=25)

Registo = Button(mainWindow,text="Registo",width=8,height=2)
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

top1_label = Button(mainWindow,text="Avatar the Last Airbend - TOP OVERALL",command=lambda: function17())
top1_label.place(x=86,y=640)

#Image TOP 2

imagemRM = Image.open("Main Page//rick-morty-portal.jpg")
imgRM = imagemRM.resize((250,229), Image.ANTIALIAS)
RMResized = ImageTk.PhotoImage(imgRM)

top2_canvas = Canvas(mainWindow,width=250,height=225,bg="gray")
top2_canvas.place(x=324,y=400)
top2_canvas.create_image(127,112,image = RMResized)

#Button TOP 2

top2_label = Button(mainWindow,text="Rick and Morty - TOP SERIES",command=lambda:function19())
top2_label.place(x=372,y=640)

#Imagem TOP 3

imagemSA = Image.open("Main Page//spirited-away.jpg")
imgSA = imagemSA.resize((250,229), Image.ANTIALIAS)
SAResized = ImageTk.PhotoImage(imgSA)

top3_canvas = Canvas(mainWindow,width=250,height=225,bg="gray")
top3_canvas.place(x=584,y=400)
top3_canvas.create_image(127,112,image = SAResized)

#Button TOP 3

top3_label = Button(mainWindow,text="Spirit Away - TOP FILME",command=lambda:function7())
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
