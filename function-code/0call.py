from tkinter import *
#------------------Funções das páginas------------------
from aquamanFunction import function
from deadpoolFunction import function2
from whiteWallFunction import function3
from spidermanItsvFunction import function4
from maryPoppinsReturnsFunction import function5
from ladyInTheWaterFunction import function6
from spiritedAwayFunction import function7
from knivesOutFunction import function8
from lucaFunction import function9
from theAdventuresofTintinFunction import function10
from lokiFunction import function11
from cobraKaiFunction import function12
from criminalMindsFunction import function13
from whatIfFunction import function14
from goodOmensFunction import function15
from shadowAndBoneFunction import function16
from avatarTlabFunction import function17
from castleFunction import function18 
from rickAndMortyFunction import function19
from overTheGardenWallFunction import function20
#-------------------------------------------------------


window = Tk()
window.geometry("500x500")
window.title("Function Call")

btn_call_1 = Button(window, text="Aquaman", height=1, width=20, command=function)
btn_call_1.place(x=20, y=20)

btn_call_2 = Button(window, text="Deadpool", height=1, width=20, command=function2)
btn_call_2.place(x=20, y=50)

btn_call_3 = Button(window, text="White Wall", height=1, width=20, command=function3)
btn_call_3.place(x=20, y=80)

btn_call_4 = Button(window, text="Spiderman: Into the Spiderverse", height=1, width=20, command=function4)
btn_call_4.place(x=20, y=110)

btn_call_5 = Button(window, text="Mary Poppins Returns", height=1, width=20, command=function5)
btn_call_5.place(x=20, y=140)

btn_call_6 = Button(window, text="Lady in the Water", height=1, width=20, command=function6)
btn_call_6.place(x=20, y=170)

btn_call_7 = Button(window, text="Spirited Away", height=1, width=20, command=function7)
btn_call_7.place(x=20, y=200)

btn_call_8 = Button(window, text="Knives Out", height=1, width=20, command=function8)
btn_call_8.place(x=20, y=230)

btn_call_9 = Button(window, text="Luca", height=1, width=20, command=function9)
btn_call_9.place(x=20, y=260)

btn_call_10 = Button(window, text="The Adventures of Tintin", height=1, width=20, command=function10)
btn_call_10.place(x=20, y=290)

btn_call_11 = Button(window, text="Loki", height=1, width=20, command=function11)
btn_call_11.place(x=200, y=20)

btn_call_12 = Button(window, text="Cobra Kai", height=1, width=20, command=function12)
btn_call_12.place(x=200, y=50)

btn_call_13 = Button(window, text="Criminal Minds", height=1, width=20, command=function13)
btn_call_13.place(x=200, y=80)

btn_call_14 = Button(window, text="What if...?", height=1, width=20, command=function14)
btn_call_14.place(x=200, y=110)

btn_call_15 = Button(window, text="Good Omens", height=1, width=20, command=function15)
btn_call_15.place(x=200, y=140)

btn_call_16 = Button(window, text="Shadow and Bone", height=1, width=20, command=function16)
btn_call_16.place(x=200, y=170)

btn_call_17 = Button(window, text="Avatar TLAB", height=1, width=20, command=function17)
btn_call_17.place(x=200, y=200)

btn_call_18 = Button(window, text="Castle", height=1, width=20, command=function18)
btn_call_18.place(x=200, y=230)

btn_call_19 = Button(window, text="Rick and Morty", height=1, width=20, command=function19)
btn_call_19.place(x=200, y=260)

btn_call_20 = Button(window, text="Over the Garden Wall", height=1, width=20, command=function20)
btn_call_20.place(x=200, y=290)

window.mainloop()