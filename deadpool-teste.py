from tkinter import*


deadpool = Tk()
deadpool.geometry("700x1000")
deadpool.resizable(True, True)
deadpool.title("Deadpool (2016)")
deadpool.iconbitmap("imagens\Martynamru-Leather-Movie.ico")

ctn_canvas = Canvas(deadpool, width = 375, height = 524, bd = 3,bg="black", relief = "solid")
ctn_canvas.place(x=10, y=20)


img = PhotoImage(file = "imagens\Deadpool(2016)-2.gif")
ctn_canvas.create_image(190,266, image = img)




val = IntVar()
val1 = IntVar()


check1 = Checkbutton(deadpool, text="Favorito", variable = val)
check2 = Checkbutton(deadpool, text="Visto", variable = val1)

check1.place(x= 420, y=30)
check2.place(x=420, y=60)


def lista_favoritos():

    listaFav = Tk()
    listaFav.geometry("700x1000")
    listaFav.resizable(True, True)
    listaFav.title("Lista de favoritos")
    listaFav.iconbitmap("imagens\Treetog-Junior-Folder-fav.ico")


    if val.get() == 1:
        label1 = Label(listaFav, text = "Deadpool (2016) - Teste*") 
        label1.place(x=10, y=20)


    listaFav.mainloop()


favButton = Button(deadpool, text="Lista de favoritos",bg = "#FA6B6B",fg = "black",relief = "solid",bd = 2, command=lista_favoritos)
favButton.place(x=580, y=20)



#fazer função que quando check1.get() == 1, manda o filme para lista de favoritos




deadpool.mainloop()