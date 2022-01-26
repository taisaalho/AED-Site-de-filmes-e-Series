from tkinter import *
from tkinter import messagebox

def num_likes():
    f=open("likes.txt", "r", encoding="utf-8")
    ficheiro=f.readlines()
    f.close()
    count=0
    for linha in ficheiro:
        count=count+1
    count_likes.set(str(count))

def give_like():
    if rd_like.get()==True:
        f=open("likes.txt","a")
        frase="Like"+"\n"
        f.write(frase)
        f.close
    num_likes()

window=Tk()
window.geometry("700x400")
window.title("Comentários")

rd_like=IntVar()

rd_like=Checkbutton(text="Like",font=("Helvetica", 9) ,variable=rd_like, command=give_like)
rd_like.place(x=15,y=10)

lbl_count_likes=Label(window, text="Nº de Likes:", font=("Helvetica", 9))
lbl_count_likes.place(x=70, y=10)

count_likes = StringVar()
txt_count_likes=Entry(window, width = 5, textvariable= count_likes)
txt_count_likes.place(x=140, y=10)

window.mainloop()