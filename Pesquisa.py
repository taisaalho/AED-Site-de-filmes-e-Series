from tkinter import *

window=Tk()   
window.title('Pesquisa')

global screenHeight
global screenWidth
global appHeight, appWidth
global x,y
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 700                             
appHeight = 600
x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))

l_filmes=["Aquaman", "Luca", "Mary Poppins Returns", "Lady in water", "Knives Out"]

l_series=["Cobra Kai", "Ricky and Morty", "Castle", "Shadow and Bone", "Criminal minds"]

l_f_categorias=["Ação", "Animação", "Comédia", "Fantasia", "Mistério"]

l_s_categorias=["Ação", "Animação", "Comédia", "Fantasia", "Mistério"]

def pes_categoria():
    if rd_1==True:
        pes_ação()
    elif rd_2==True:
        pes_animacao()
    elif rd_3==True:
        pes_comedia()
    elif rd_4==True:
        pes_fantasia()
    elif rd_5==True:
        pes_misterio()

def selecao_item(event):
    indice = lbox_tarefas.curselection()   # Índice da linha selecionada
    texto = lbox_tarefas.get(indice)       # Obter conteudo da Listbox, linha selecionada 
    tarefa.set(texto)

def pes_ação():
    conWindow = Toplevel()
    conWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    conWindow.title("Filmes e series de Ação")
    conWindow.focus_force()
    conWindow.grab_set()

    pos=l_f_categorias.index("Ação")
    f_açao=l_filmes[pos]
    pos_1=l_s_categorias.index("Ação")
    s_açao=l_series[pos_1]
    print(f_açao)

    frame_açao=

    #ListBox
    lbox_tarefas=Listbox( width = 35, height=15, bd="3", selectmode = "single", selectbackground="orange")
    lbox_tarefas.place(x=8, y= 25)
    lbox_tarefas.bind("<<ListboxSelect>>", selecao_item)      # Evento ao selecionar item da Listbox #########

def pes_animacao():
    conWindow = Toplevel()
    conWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    conWindow.title("Filmes e series de Animação")
    conWindow.focus_force()
    conWindow.grab_set()

    pos=l_f_categorias.index("Animação")
    f_animacao=l_filmes[pos]
    pos_1=l_s_categorias.index("Animação")
    s_animacao=l_series[pos_1]
    return f_animacao, s_animacao

def pes_comedia():
    conWindow = Toplevel()
    conWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    conWindow.title("Filmes e series de Comédia")
    conWindow.focus_force()
    conWindow.grab_set()

    pos=l_f_categorias.index("Animação")
    f_comedia=l_filmes[pos]
    pos_1=l_s_categorias.index("Animação")
    s_comedia=l_series[pos_1]
    return f_comedia, s_comedia

def pes_fantasia():
    conWindow = Toplevel()
    conWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    conWindow.title("Filmes e series de Fantasia")
    conWindow.focus_force()
    conWindow.grab_set()

    pos=l_f_categorias.index("Fantasia")
    f_fantasia=l_filmes[pos]
    pos_1=l_s_categorias.index("Fantasia")
    s_fantasia=l_series[pos_1]
    return f_fantasia, s_fantasia

def pes_misterio():
    conWindow = Toplevel()
    conWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    conWindow.title("Filmes e series de Mistério")
    conWindow.focus_force()
    conWindow.grab_set()

    pos=l_f_categorias.index("Mistério")
    f_misterio=l_filmes[pos]
    pos_1=l_s_categorias.index("Mistério")
    s_misterio=l_series[pos_1]
    return f_misterio, s_misterio

#Menu Window principal
barra_Menu=Menu(window)

simuladores_Menu=Menu(barra_Menu)
barra_Menu.add_command(label="Pesquisa")
barra_Menu.add_command(label="Sair", command=window.quit)

window.configure(menu=barra_Menu)

tarefa=StringVar()
rd_1=IntVar()
rd_2=IntVar()
rd_3=IntVar()
rd_4=IntVar()
rd_5=IntVar()

#Texto Window principal
txt_pes=Text(window, width=50, height=1, relief="sunken", bd=3)
txt_pes.place(x=10, y=20)

#Botão pesquisa por nome 
button_name=Button(window, text="Pesquisar", width=10, height=1, fg="black") #command=pes_nome)
button_name.place(x=430, y=20)

#Painel de filmes e series
frame_tipo=LabelFrame(window, text="Tipo", width=140, height=90, relief="sunken", bd="3", fg="black")
frame_tipo.place(x=10,y=60)

rd_filme=Checkbutton(text="Filme") #,command=)
rd_filme.place(x=15,y=80)

rd_serie=Checkbutton(text="Serie") #, command=)
rd_serie.place(x=15,y=110)

#Painel das categorias
frame_categoria=LabelFrame(window, text="Categoria", width=200, height=250, relief="sunken", bd="3", fg="black")
frame_categoria.place(x=10, y=170)

#Botão das categorias
#button_categorias=Button(window, text="Pesquisar por Categorias", width=20, height=2, fg="black", relief="raised", command=pes_categoria)
#button_categorias.place(x=230, y=210)

#Seleção das categorias
rd_açao=Checkbutton(text="Ação",variable=rd_1, command=pes_ação)
rd_açao.place(x=15,y=190)

rd_animacao=Checkbutton(text="Animação",variable=rd_2, command=pes_animacao)
rd_animacao.place(x=15,y=210)

rd_comedia=Checkbutton(text="Comédia",variable=rd_3, command=pes_comedia)
rd_comedia.place(x=15,y=230)

rd_fantasia=Checkbutton(text="Fantasia",variable=rd_4, command=pes_fantasia)
rd_fantasia.place(x=15,y=250)

rd_misterio=Checkbutton(text="Mistério",variable=rd_5, command=pes_misterio)
rd_misterio.place(x=15,y=270)

window.mainloop()