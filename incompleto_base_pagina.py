from tkinter import *
#from tkVideoPlayer import TkinterVideo

window = Tk()
window.geometry("1700x900")
window.title("Item-Title")
window.resizable(0, 0)


#Canvas para póster
poster_space = Canvas(window, width=507, height=750, bd=2, relief="sunken")
poster_space.place(x=20, y=20)

#Imagem póster
#img = PhotoImage(file="peee.gif")
#poster_space.create_image(253, 375, image=img)

#Campo de título
titulo = Label(window, text="The Peepee Poopoo Man", fg="#5E239D", font=("Calisto MT", "24", "bold"))
titulo.place(x=560, y=20)

#Campo de Categorias
cat = Label(window, text="Categorias:", fg="blue", font=("Calisto MT", "10", "bold"))
cat.place(x=560, y=70)

cat2 = Label(window, text="CategoriaA, CategoriaB", font=("Calisto MT", "10"))
cat2.place(x=630, y=70)

#Classificação
clas = Label(window, text="Classificação:", fg="blue", font=("Calisto MT", "10", "bold"))
clas.place(x=560, y=90)

clas2 = Label(window, text="num", font=("Calisto MT", "10"))
clas2.place(x=645, y=90)

#Campo de descrição
desc = Label(window, text="Descrição:", fg="blue", font=("Calisto MT", "10", "bold"))
desc.place(x=560, y=110)

desc2 = Label(window, text="coiso faz coisa", font=("Calisto MT", "10"))
desc2.place(x=625, y=110)

#Campo de trailer
trailer_space = Canvas(window, width=600, height=522, bd=2, relief="sunken")
trailer_space.place(x=560, y=250)

#Buttons play/pause
btn_play = Button(trailer_space, text="Play", height=1, width=10, fg="blue", font=("Calisto MT", "10", "bold"))
btn_play.place(x=30, y=470)

btn_pause = Button(trailer_space, text="Pause", height=1, width=10, fg="blue", font=("Calisto MT", "10", "bold"))
btn_pause.place(x=150, y=470)

#Button marcar como visto
btn_seen = Button(window, text="Marcar como Visto", height=1, width=20, fg="red", font=("Calisto MT", "10", "bold"))
btn_seen.place(x=20, y=800)

#Button adicionar aos favoritos
btn_fav = Button(window, text="Adicionar aos Favoritos", height=1, width=20, fg="red", font=("Calisto MT", "10", "bold"))
btn_fav.place(x=200, y=800)

#Campo de likes


#Campo de comentários



window.mainloop()