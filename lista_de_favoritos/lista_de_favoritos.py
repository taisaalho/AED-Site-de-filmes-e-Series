# Biblioteca Tkinter: UI
from tkinter import *



def limpar():
    lbox_favoritos.delete(0, "end")
    

def remover():
    # Remove o item selecionado da Listbox
    lbox_favoritos.delete(lbox_favoritos.curselection())   # indice do item selecionado
    filme.set("")
    f = open("lista_favoritos.txt", "w", encoding="utf-8")
    cont = lbox_favoritos.size()
    for i in range(cont):
        atividade = lbox_favoritos.get(i) 
        if atividade.find("\n") == -1:
            atividade = atividade + "\n"

        f.write(atividade)
    f.close()
    

def selecao_item(event):
    indice = lbox_favoritos.curselection()   # Índice da linha selecionada
    texto = lbox_favoritos.get(indice)       # Obter conteudo da Listbox, linha selecionada 
    filme.set(texto)

 


window=Tk()   # invoca classe tk , cria a "main window"
window.geometry("1150x540")
window.title('Lista de Favoritos')
window.iconbitmap("imagens\Treetog-Junior-Folder-fav.ico")


#Panel para ListBox
panel1 = PanedWindow(width = 250, height = 300, bd = "3", relief = "sunken")
panel1.place(x=10, y=30)

#ListBox
lbox_favoritos=Listbox(panel1, width = 35, height=15, bd="3", selectmode = "single", selectbackground="orange")
lbox_favoritos.place(x=8, y= 25)
lbox_favoritos.bind("<<ListboxSelect>>", selecao_item)      # Evento ao selecionar item da Listbox #########
f = open("lista_favoritos.txt","r")
ficheiro = f.readlines()
f.close
for linha in ficheiro:
    lbox_favoritos.insert("end", linha)

# Panel filme
panel2 = PanedWindow(width = 350, height = 100, bd = "3", relief = "sunken")
panel2.place(x=300, y=30)
#Label
lbl_filme=Label(panel2, text="Selecionado:", fg="blue", font=("Helvetica", 9))
lbl_filme.place(x=2, y=30)
#Entry
filme = StringVar()
txt_filme=Entry(panel2, width = 35, textvariable= filme)
txt_filme.place(x=80, y=30)

# Buttons


btn_remove=Button(window,  text = "Remove",width = 12, height = 2, fg = "black", command = remover )
btn_remove.place(x=400, y=200)


window.mainloop()   # event listening loop by calling the mainloop()





#download = salvar alterações