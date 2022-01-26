from tkinter import *
from tkVideoPlayer import TkinterVideo

window = Tk()
window.geometry("1150x540")
window.title("Spider-man: Into the Spiderverse")
window.resizable(0, 0)
window.iconbitmap("imagens\Martynamru-Leather-Movie.ico")


#Canvas para póster
poster_space = Canvas(window, width=298, height=441, bd=2, relief="sunken")
poster_space.place(x=20, y=20)

#Imagem póster
img = PhotoImage(file="spiderman-into-the-sverse-poster.gif")
poster_space.create_image(253, 375, image=img)

#Campo de título
titulo = Label(window, text="Spider-man: Into the Spiderverse (2018)", fg="#5E239D", font=("Calisto MT", "16", "bold"))
titulo.place(x=350, y=20)

#Campo de Categorias
cat = Label(window, text="Categorias:", fg="blue", font=("Calisto MT", "10", "bold"))
cat.place(x=350, y=60)

cat2 = Label(window, text="Ação, Animação", font=("Calisto MT", "10"))
cat2.place(x=420, y=60)

#Classificação
clas = Label(window, text="Classificação:", fg="blue", font=("Calisto MT", "10", "bold"))
clas.place(x=350, y=80)

clas2 = Label(window, text="8.4", font=("Calisto MT", "10"))
clas2.place(x=435, y=80)

#Elenco
cast = Label(window, text="Elenco:", fg="blue", font=("Calisto MT", "10", "bold"))
cast.place(x=350, y=100)

cast2 = Label(window, text="Shameik Moore, Jake Johnson", font=("Calisto MT", "10"))
cast2.place(x=400, y=100)

#Campo de descrição
desc = Text(window, height=4, width=50, font=("Calisto MT", "10", "bold"))
desc.place(x=340, y=120)
desc.insert(1.0, "Após ser atingido por uma teia radioativa, Miles Morales, um jovem negro do Brooklyn, torna-se no Homem-Aranha, inspirado no legado do já falecido Peter Parker. Entretanto, ao visitar o túmulo do seu ídolo numa noite chuvosa, ele é surpreendido com a presença do próprio Peter, vestindo o traje do herói por baixo de um sobretudo. A surpresa fica ainda maior quando Miles descobre que ele veio de uma dimensão paralela, assim como outras versões do Homem-Aranha.")
desc.config(state="disabled")

#Campo de trailer
trailer_space = Canvas(window, bg="gray", width=370, height=268, bd=2, relief="sunken")
trailer_space.place(x=335, y=250)

videoplayer = TkinterVideo(trailer_space, scaled=True, pre_load=False)
videoplayer.load(r"spiderman-into-the-sverse-trailer.mp4")

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

check1 = Checkbutton(window, text="Adicionar aos favoritos",variable = val)
check2 = Checkbutton(window, text="Marcar como visto", variable = val1)

check1.place(x=25, y=480)
check2.place(x=25, y=505)

def salvar_alteracoes():

    if val.get() == 1 and val1.get() == 0:
        f = open("lista_favoritos.txt","a")
        frase = "Spiderman: Into the Spiderverse (2018)" + "\n"
        f.write(frase)
        f.close

    elif val.get() == 1 and val1.get() == 1:
        f = open("lista_vistos.txt", "a")
        frase = "Spiderman: Into the Spiderverse (2018)" +"\n"
        f.write(frase)
        f.close
        f = open("lista_favoritos.txt","a")
        frase = "Spiderman: Into the Spiderverse (2018)" + "\n"
        f.write(frase)
        f.close
    elif val.get() == 0 and val1.get() == 1:
        f=open("lista_vistos.txt", "a")
        frase = "Spiderman: Into the Spiderverse (2018)" + "\n"
        f.write(frase)
        f.close
        
def comment():
    linha=txt_coment.get("1.0","end")
    ficheiro="com_spiderman.txt"
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
    f = open("com_spiderman.txt", "w", encoding="utf-8")
    cont = lbox_coment.size()
    for i in range(cont):
        com = lbox_coment.get(i) 
        if com.find("\n") == -1:
            com = com + "\n"
        f.write(com)
    f.close()

def read_comment():
    f=open("com_spiderman.txt", "r")
    ficheiro=f.readlines()
    f.close()
    for linha in ficheiro:
        lbox_coment.insert("end",linha)
    txt_coment.delete("1.0","end")
    txt_coment("end", "")

def num_likes():
    f=open("like_spiderman.txt", "r", encoding="utf-8")
    ficheiro=f.readlines()
    f.close()
    count=0
    for linha in ficheiro:
        count=count+1
    count_likes.set(str(count))

def give_like():
    if rd_like.get()==True:
        f=open("like_spiderman.txt","a")
        frase="Like"+"\n"
        f.write(frase)
        f.close
    num_likes()    

#Button salva dados do filme
favButton = Button(window, text="Salvar alterações",bg = "#FA6B6B",fg = "black",relief = "solid",bd = 2,font = "Arial 11",command=salvar_alteracoes)
favButton.place(x=200, y=490) 

#Campo likes/comentários
eval_space = Canvas(window, bg="gray", width=400, height=500, bd=2, relief="sunken")
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

window.mainloop()
