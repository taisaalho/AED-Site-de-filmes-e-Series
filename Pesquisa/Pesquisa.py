from tkinter import *
from tkinter import messagebox

window=Tk()   
window.title('Pesquisa')

global screenHeight
global screenWidth
global appHeight, appWidth
global x,y
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 900                             
appHeight = 700
x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))

ficheiro="lista_f_s.txt"

def pes_categoria():
    if rd_1.get()==True:
        pes_ação()
    if rd_2.get()==True:
        pes_animacao()
    if rd_3.get()==True:
        pes_comedia()
    if rd_4.get()==True:
        pes_fantasia()
    if rd_5.get()==True:
        pes_misterio()
    if rd_a.get()==True:
        pes_filme()
    if rd_b.get()==True:
        pes_serie()

def w_pesquisados():
    conWindow = Toplevel()
    conWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    conWindow.title("Pesquisa")
    conWindow.focus_force()
    lbox_filmes=Listbox(conWindow,width=90, height=20, selectmode="single")
    lbox_filmes.place(x=8, y= 25)
    lbox_filmes.bind("<<ListboxSelect>>", )
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
        if campos[1]==txt_pes.get():
            if campos[1] not in "pesquisados.txt":
                f=open("pesquisados.txt","a")
                frase=campos[1]+"\n"
                f.write(frase)
                f.close
    w_pesquisados()

def pes_filme():
    f=open("lista_f_s.txt", "r", encoding="utf-8")
    ficheiro=f.readlines()
    f.close()
    for linha in ficheiro:
        campos=linha.split(";")
        #print(campos[2],campos[3])
        if campos[0]=="Filme":
            if campos[1] not in "pesquisados.txt":
                f=open("pesquisados.txt","a")
                frase=campos[1]+"\n"
                f.write(frase)
                f.close
    w_pesquisados()

def pes_serie():
    f=open("lista_f_s.txt", "r", encoding="utf-8")
    ficheiro=f.readlines()
    f.close()
    for linha in ficheiro:
        campos=linha.split(";")
        #print(campos[2],campos[3])
        if campos[0]=="Série":
            if campos[1] not in "pesquisados.txt":
                f=open("pesquisados.txt","a")
                frase=campos[1]+"\n"
                f.write(frase)
                f.close
    w_pesquisados()


def pes_ação():
    f=open("lista_f_s.txt", "r", encoding="utf-8")
    ficheiro=f.readlines()
    f.close()
    for linha in ficheiro:
        campos=linha.split(";")
        #print(campos[2],campos[3])
        if campos[2]=="Ação" or campos[3]=="Ação":
            if campos[1] not in "pesquisados.txt":
                f=open("pesquisados.txt","a")
                frase=campos[1]+"\n"
                f.write(frase)
                f.close
    w_pesquisados()

def pes_animacao():
    f=open("lista_f_s.txt", "r", encoding="utf-8")
    ficheiro=f.readlines()
    f.close()
    for linha in ficheiro:
        campos=linha.split(";")
        #print(campos[2],campos[3])
        if campos[2]=="Animação" or campos[3]=="Animação":
            if campos[1] not in "pesquisados.txt":
                f=open("pesquisados.txt","a")
                frase=campos[1]+"\n"
                f.write(frase)
                f.close
    w_pesquisados()

def pes_comedia():
    f=open("lista_f_s.txt", "r", encoding="utf-8")
    ficheiro=f.readlines()
    f.close()
    for linha in ficheiro:
        campos=linha.split(";")
        #print(campos[2],campos[3])
        if campos[2]=="Comédia" or campos[3]=="Comédia":
            if campos[1] not in "pesquisados.txt":
                f=open("pesquisados.txt","a")
                frase=campos[1]+"\n"
                f.write(frase)
                f.close
    w_pesquisados()

def pes_fantasia():
    f=open("lista_f_s.txt", "r", encoding="utf-8")
    ficheiro=f.readlines()
    f.close()
    for linha in ficheiro:
        campos=linha.split(";")
        #print(campos[2],campos[3])
        if campos[2]=="Fantasia" or campos[3]=="Fantasia":
            if campos[1] not in "pesquisados.txt":
                f=open("pesquisados.txt","a")
                frase=campos[1]+"\n"
                f.write(frase)
                f.close
    w_pesquisados()
    
def pes_misterio():
    f=open("lista_f_s.txt", "r", encoding="utf-8")
    ficheiro=f.readlines()
    f.close()
    for linha in ficheiro:
        campos=linha.split(";")
        #print(campos[2],campos[3])
        if campos[2]=="Mistério" or campos[3]=="Mistério":
            if campos[1] not in "pesquisados.txt":
                f=open("pesquisados.txt","a")
                frase=campos[1]+"\n"
                f.write(frase)
                f.close
    w_pesquisados()

#Menu Window principal
barra_Menu=Menu(window)

sim_Menu=Menu(barra_Menu)
barra_Menu.add_command(label="Pesquisa")
barra_Menu.add_command(label="Sair", command=window.quit)

window.configure(menu=barra_Menu)

rd_a=IntVar()
rd_b=IntVar()
rd_1=IntVar()
rd_2=IntVar()
rd_3=IntVar()
rd_4=IntVar()
rd_5=IntVar()

#Texto Window principal
txt_pes=Text(window, width=50, height=1, relief="sunken", bd=3)
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
button_categorias=Button(window, text="Pesquisar por Categorias", width=20, height=2, fg="black", relief="raised", command=pes_categoria)
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

window.mainloop()
