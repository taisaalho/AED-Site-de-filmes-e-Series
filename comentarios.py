from cgitb import text
from tkinter import *
import os
ficheiro="coment.txt"

def comment():
    linha=txt_coment.get("1.0","end")
    ficheiro="coment.txt"
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
    f = open("tarefas.txt", "w", encoding="utf-8")
    cont = lbox_coment.size()
    for i in range(cont):
        com = lbox_coment.get(i) 
        if com.find("\n") == -1:
            com = com + "\n"
        f.write(com)
    f.close()

def read_comment():
    f=open("coment.txt", "r")
    ficheiro=f.readlines()
    f.close()
    for linha in ficheiro:
        lbox_coment.insert("end",linha)
    txt_coment.delete("1.0","end")
    txt_coment("end", "")

window=Tk()
window.geometry("700x400")
window.title("Comentários")

coment = StringVar()

#Button
btn_guardar=Button(window, text="Comentar", width=20, height=2 , fg="blue", command=comment)
btn_guardar.place(x=20, y=30)

btn_limpar=Button(window, text="Apagar", width=20, height=2, fg="blue", command=remover)
btn_limpar.place(x=220, y=30)

btn_ler=Button(window, text="Ver comentarios", width=20, height=2, fg="blue", command=read_comment)
btn_ler.place(x=420, y=30)

#Label
lbl_dcom=Label(window, text="Deixe aqui o seu comentario:", bd=2)
lbl_dcom.place(x=20,y=80)

#text
txt_coment=Text(window, width=40, height=3, relief="sunken", bd=3)
txt_coment.place(x=20, y=100)

#Label
lbl_com=Label(window, text="Comentários", bd=2)
lbl_com.place(x=20,y=157)

#listbox
lbox_coment=Listbox(window, width=60, height=10, bd="3", selectmode = "single", selectbackground="blue")
lbox_coment.place(x=20, y= 180)
lbox_coment.bind("<<ListboxSelect>>", selecao_item)

window.mainloop()