from tkinter import *
from turtle import bgcolor, color
from tkinter import messagebox
#from tkVideoPlayer import TkinterVideo

window = Tk()
window.geometry("1150x540")
window.title("Item-Title")
window.resizable(0, 0)
window.iconbitmap("imagens\Martynamru-Leather-Movie.ico")


#Canvas para póster
poster_space = Canvas(window, width=298, height=441, bd=2, relief="solid")
poster_space.place(x=20, y=20)

#Imagem póster
#img = PhotoImage(file="peee.gif")
#poster_space.create_image(253, 375, image=img)

#Campo de título
titulo = Label(window, text="The Peepee Poopoo Man", fg="#5E239D", font=("Calisto MT", "16", "bold"))
titulo.place(x=350, y=20)

#Campo de Categorias
cat = Label(window, text="Categorias:", fg="blue", font=("Calisto MT", "10", "bold"))
cat.place(x=350, y=60)

cat2 = Label(window, text="CategoriaA, CategoriaB", font=("Calisto MT", "10"))
cat2.place(x=420, y=60)

#Classificação
clas = Label(window, text="Classificação:", fg="blue", font=("Calisto MT", "10", "bold"))
clas.place(x=350, y=80)

clas2 = Label(window, text="num", font=("Calisto MT", "10"))
clas2.place(x=435, y=80)

#Elenco
cast = Label(window, text="Elenco:", fg="blue", font=("Calisto MT", "10", "bold"))
cast.place(x=350, y=100)

cast2 = Label(window, text="aaaaaaaaaaaaa", font=("Calisto MT", "10"))
cast2.place(x=400, y=100)

#Campo de descrição
desc = Label(window, text="Descrição:", fg="blue", font=("Calisto MT", "10", "bold"))
desc.place(x=350, y=120)

desc2 = Label(window, text="coiso faz coisa", font=("Calisto MT", "10"))
desc2.place(x=415, y=120)

#Campo de trailer
trailer_space = Canvas(window, bg="gray", width=370, height=268, bd=2, relief="solid")
trailer_space.place(x=335, y=250)

#Buttons play/pause
btn_play = Button(trailer_space, bg="blue", text="Play", height=1, width=8, fg="white", font=("Calisto MT", "8", "bold"))
btn_play.place(x=20, y=230)

btn_pause = Button(trailer_space, bg="blue", text="Pause", height=1, width=8, fg="white", font=("Calisto MT", "8", "bold"))
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
        frase = "Filme xxx" + "\n"
        f.write(frase)
        f.close

    elif val.get() == 1 and val1.get() == 1:
        f = open("lista_vistos.txt", "a")
        frase = "Filme xxx" +"\n"
        f.write(frase)
        f.close
        f = open("lista_favoritos.txt","a")
        frase = "Filme xxx" + "\n"
        f.write(frase)
        f.close
    elif val.get() == 0 and val1.get() == 1:
        f=open("lista_vistos.txt", "a")
        frase = "Filme xxx" + "\n"
        f.write(frase)
        f.close
        
    


#Button salva dados do filme
favButton = Button(window, text="Salvar alterações",bg = "#FA6B6B",fg = "black",relief = "solid",bd = 2,font = "Arial 11",command=salvar_alteracoes)
favButton.place(x=200, y=490) 



#Campo likes/comentários
eval_space = Canvas(window, bg="gray", width=400, height=500, bd=2, relief="solid")
eval_space.place(x=720, y=20)

#Campo de likes
like_space = LabelFrame(eval_space, text="Likes", width=380, height=60, bd=2, relief="raised", fg="red", font=("Calisto MT", "10", "bold"))
like_space.place(x=15, y=15)

#Campo de comentários
com_space = LabelFrame(eval_space, text="Comentários", width=380, height=410, bd=2, relief="raised", fg="red", font=("Calisto MT", "10", "bold"))
com_space.place(x=15, y=85)




window.mainloop()
