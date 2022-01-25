from tkinter import *

def limpar():
    lbox_favoritos.delete(0, "end")

def limpar_vistos():
    lbox_vistos.delete(0, "end")
    

def remover_favorito():
    lbox_favoritos.delete(lbox_favoritos.curselection())   
    f = open("lista_favoritos.txt", "w", encoding="utf-8")
    cont = lbox_favoritos.size()
    for i in range(cont):
        filmes = lbox_favoritos.get(i) 
        if filmes.find("\n") == -1:
            filmes = filmes + "\n"

        f.write(filmes)
    f.close()

def remover_visto():
    lbox_vistos.delete(lbox_vistos.curselection())
    f = open("lista_vistos.txt", "w", encoding="utf-8")
    cont = lbox_vistos.size()
    for i in range(cont):
        filmes = lbox_vistos.get(i)
        if filmes.find("\n") == -1:
            filmes = filmes + "\n"
    

def selecao_item(event):
    indice = lbox_favoritos.curselection()   
    texto = lbox_favoritos.get(indice)      


 


window=Tk()   
window.geometry("1150x540")
window.title('Lista de Favoritos e Vistos')
window.iconbitmap("imagens\Treetog-Junior-Folder-fav.ico")


#Panel para ListBox
panel1 = PanedWindow(width = 250, height = 300, bd = "3", relief = "sunken")
panel1.place(x=10, y=30)
panel2 = PanedWindow(width = 250, height = 300, bd = "3", relief = "sunken")
panel2.place(x=300, y=30)

#ListBox
lbox_favoritos=Listbox(panel1, width = 35, height=15, bd="3", selectmode = "single", selectbackground="orange")
lbox_favoritos.place(x=8, y= 25)
lbox_favoritos.bind("<<ListboxSelect>>", selecao_item)     
f = open("lista_favoritos.txt","r")
ficheiro = f.readlines()
f.close
for linha in ficheiro:
    lbox_favoritos.insert("end", linha)

lbox_vistos=Listbox(panel2, width=35, height=15, bd="3", selectmode = "single", selectbackground="orange")
lbox_vistos.place(x=8, y=25)
lbox_vistos.bind("<<ListboxSelect>>", selecao_item)
f=open("lista_vistos.txt", "r")
ficheiro = f.readlines()
f.close
for linha in ficheiro:
    lbox_vistos.insert("end", linha)

#Label
lbl_favoritos=Label(panel1, text="Filmes favoritados:", fg="#E34E0E", font=("Helvetica", 11))
lbl_favoritos.place(x=2, y=2)
lbl_vistos=Label(panel2, text="Filmes vistos:", fg="#E34E0E", font=("Helvetica", 11))
lbl_vistos.place(x=2, y=2)

# Buttons
btn_remove=Button(window,  text = "Remover favorito",width = 15, height = 2, fg = "black", command = remover_favorito)
btn_remove.place(x=75, y=350)
btn2_remove=Button(window, text="Remover visto", width=15, height=2, fg="black", command=remover_visto)
btn2_remove.place(x=365, y=350)

window.mainloop()   

