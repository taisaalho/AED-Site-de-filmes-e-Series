from tkinter import *
import tkinter as tk 
from tkinter import filedialog   # filedialog boxes
from PIL import ImageTk
from tkVideoPlayer import TkinterVideo


window = Toplevel()
window.geometry("1150x540")
window.title("Deadpool")
window.resizable(0, 0)


#Canvas para póster
poster_space = Canvas(window, width=298, height=441, bd=2, relief="sunken")
poster_space.place(x=20, y=20)

#Imagem póster
img = PhotoImage(file="deadpool-poster.gif")
poster_space.create_image(253, 375, image=img)

#Campo de título
titulo = Label(window, text="Deadpool (2016)", fg="#5E239D", font=("Calisto MT", "16", "bold"))
titulo.place(x=350, y=20)

#Campo de Categorias
cat = Label(window, text="Categorias:", fg="blue", font=("Calisto MT", "10", "bold"))
cat.place(x=350, y=60)

cat2 = Label(window, text="Ação, Comédia", font=("Calisto MT", "10"))
cat2.place(x=420, y=60)

#Classificação
clas = Label(window, text="Classificação:", fg="blue", font=("Calisto MT", "10", "bold"))
clas.place(x=350, y=80)

clas2 = Label(window, text="8.0", font=("Calisto MT", "10"))
clas2.place(x=435, y=80)

#Elenco
cast = Label(window, text="Elenco:", fg="blue", font=("Calisto MT", "10", "bold"))
cast.place(x=350, y=100)

cast2 = Label(window, text="Ryan Reynolds, Morena Baccarin", font=("Calisto MT", "10"))
cast2.place(x=400, y=100)

#Campo de descrição
desc = Text(window, height=4, width=50, font=("Calisto MT", "10", "bold"))
desc.place(x=340, y=120)
desc.insert(1.0, "Wade Wilson é um ex-agente especial que passou a trabalhar como mercenário. Seu mundo é destruído quando um cientista maligno o tortura e o desfigura completamente. O experimento brutal transforma Wade em Deadpool, que ganha poderes especiais de cura e uma força aprimorada. Com a ajuda de aliados poderosos e um senso de humor mais desbocado e cínico do que nunca, o irreverente anti-herói usa habilidades e métodos violentos para se vingar do homem que quase acabou com a sua vida.")
desc.config(state="disabled")

#Campo de trailer
trailer_space = Canvas(window, bg="gray", width=370, height=268, bd=2, relief="sunken")
trailer_space.place(x=335, y=250)

videoplayer = TkinterVideo(trailer_space, scaled=True, pre_load=False)
videoplayer.load(r"deadpool-trailer.mp4")

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

check1.place(x=20, y=490)
check2.place(x=180, y=490)

def lista_favoritos():

    listaFav = Tk()
    listaFav.geometry("1150x540")
    listaFav.resizable(True, True)
    listaFav.title("Lista de favoritos")
    listaFav.iconbitmap("imagens\Treetog-Junior-Folder-fav.ico")
    


    if val.get() == 1 and val1.get() == 0:
        btn1 = Button(listaFav, text = "Filme xxx", font = "Arial 12 bold", relief = "solid", bd = 2)
        btn1.place(x=50, y=50)
        

    elif val.get() == 1 and val1.get() == 1:
        btn2 = Button(listaFav, text = "Filme xxx - Visto", font = "Arial 12 bold", relief = "solid", bd = 2)
        btn2.place(x=50, y=50)
        

    listaFav.mainloop()

#Button lista de favoritos
favButton = Button(window, text="Lista de favoritos",bg = "#FA6B6B",fg = "black",relief = "solid",bd = 2,font = "Arial 12 bold",command=lista_favoritos)
favButton.place(x=565, y=203) 

#Campo likes/comentários
eval_space = Canvas(window, bg="gray", width=400, height=500, bd=2, relief="sunken")
eval_space.place(x=720, y=20)

#Campo de likes
like_space = LabelFrame(eval_space, text="Likes", width=380, height=60, bd=2, relief="raised", fg="red", font=("Calisto MT", "10", "bold"))
like_space.place(x=15, y=15)

#Campo de comentários
com_space = LabelFrame(eval_space, text="Comentários", width=380, height=410, bd=2, relief="raised", fg="red", font=("Calisto MT", "10", "bold"))
com_space.place(x=15, y=85)

window.mainloop()