from tkinter import *
from lista_de_favs_e_vist import*

window = Tk()
window.resizable(True, True)
window.geometry("1300x1000")
window.title("Most Rated")

ctn_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn_canvas.place(x=10, y=20)

img = PhotoImage(file = "avatar-tlab-poster.gif")
ctn_canvas.create_image(63,77, image = img)

lbl1 = Label(window, text="Avatar:The Last Airbender", relief="sunken", bd=1)
lbl1.place(x=5, y=210)
lbl_1 = Label(window, text = "9.3", relief="sunken", bd=1)
lbl_1.place(x=65, y=230)


ctn2_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn2_canvas.place(x=165, y=20)

img2 = PhotoImage(file = "rick-and-morty-poster.gif")
ctn2_canvas.create_image(63,77, image = img2)

lbl2 = Label(window, text="Rick and Morty", relief="sunken", bd=1)
lbl2.place(x=190, y=210)
lbl_2 = Label(window, text = "9.2", relief="sunken", bd=1)
lbl_2.place(x=220, y=230)


ctn3_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn3_canvas.place(x=320, y=20)

img3 = PhotoImage(file = "over-the-garden-wall-poster.gif")
ctn3_canvas.create_image(63,77, image = img3)

lbl3 = Label(window, text="Over The Garden Wall", relief="sunken", bd=1)
lbl3.place(x=330, y=210)
lbl_3 = Label(window, text = "8.8", relief="sunken", bd=1)
lbl_3.place(x=375, y=230)


ctn4_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn4_canvas.place(x=475, y=20)

img4 = PhotoImage(file = "spirited-away-poster.gif")
ctn4_canvas.create_image(63,77, image = img4)

lbl4 = Label(window, text="Spirited Away", relief="sunken", bd=1)
lbl4.place(x=500, y=210)
lbl_4 = Label(window, text = "8.6", relief="sunken", bd=1)
lbl_4.place(x=525, y=230)


ctn5_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn5_canvas.place(x=630, y=20)

img5 = PhotoImage(file = "cobra-kai-poster.gif")
ctn5_canvas.create_image(63,77, image = img5)

lbl5 = Label(window, text="Cobra Kai", relief="sunken", bd=1)
lbl5.place(x=670, y=210)
lbl_5 = Label(window, text = "8.6", relief="sunken", bd=1)
lbl_5.place(x=690, y=230)


ctn6_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn6_canvas.place(x=785, y=20)

img6 = PhotoImage(file = "spiderman-into-the-sverse-poster.gif")
ctn6_canvas.create_image(63,77, image = img6)

lbl6 = Label(window, text="Spiderman:Into the Spiderverse", relief="sunken", bd=1)
lbl6.place(x=775, y=210)
lbl_6 = Label(window, text = "8.4", relief="sunken", bd=1)
lbl_6.place(x=840, y=230)


ctn7_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn7_canvas.place(x=940, y=20)

img7 = PhotoImage(file = "loki-poster.gif")
ctn7_canvas.create_image(63,77, image = img7)

lbl7 = Label(window, text="Loki", relief="sunken", bd=1)
lbl7.place(x=995, y=210)
lbl_7 = Label(window, text = "8.3", relief="sunken", bd=1)
lbl_7.place(x=1000, y=230)


ctn8_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn8_canvas.place(x=1095, y=20)

img8 = PhotoImage(file = "criminal-minds-poster.gif")
ctn8_canvas.create_image(63,77, image = img8)

lbl8= Label(window,text="Criminal Minds", relief="sunken", bd=1)
lbl8.place(x=1125, y=210)
lbl_8 = Label(window, text = "8.1", relief="sunken", bd=1)
lbl_8.place(x=1160, y=230)


ctn9_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn9_canvas.place(x=10, y=273)

img9 = PhotoImage(file = "castle-poster.gif")
ctn9_canvas.create_image(63,77, image = img9)

lbl9= Label(window,text="Castle", relief="sunken", bd=1)
lbl9.place(x=55, y=465)
lbl_9 = Label(window, text = "8.1", relief="sunken", bd=1)
lbl_9.place(x=60, y=485)


ctn10_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn10_canvas.place(x=165, y=273)

img10 = PhotoImage(file = "deadpool-poster.gif")
ctn10_canvas.create_image(63,77, image = img10)

lbl10= Label(window,text="Deadpool", relief="sunken", bd=1)
lbl10.place(x=210, y=465)
lbl_10 = Label(window, text = "8.0", relief="sunken", bd=1)
lbl_10.place(x=225, y=485)


ctn11_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn11_canvas.place(x=320, y=273)

img11 = PhotoImage(file = "knives-out.gif")
ctn11_canvas.create_image(63,77, image = img11)

lbl11= Label(window,text="Knives Out", relief="sunken", bd=1)
lbl11.place(x=355, y=465)
lbl_11 = Label(window, text = "7.9", relief="sunken", bd=1)
lbl_11.place(x=375, y=485)


ctn12_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn12_canvas.place(x=475, y=273)

img12 = PhotoImage(file = "shadow-and-bone-poster.gif")
ctn12_canvas.create_image(63,77, image = img12)

lbl12= Label(window,text="Shadow and Bone", relief="sunken", bd=1)
lbl12.place(x=490, y=465)
lbl_12 = Label(window, text = "7.7", relief="sunken", bd=1)
lbl_12.place(x=530, y=485)


ctn13_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn13_canvas.place(x=630, y=273)

img13 = PhotoImage(file = "luca-poster.gif")
ctn13_canvas.create_image(63,77, image = img13)

lbl13= Label(window,text="Luca", relief="sunken", bd=1)
lbl13.place(x=680, y=465)
lbl_13 = Label(window, text = "7.5", relief="sunken", bd=1)
lbl_13.place(x=685, y=485)


ctn14_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn14_canvas.place(x=785, y=273)

img14 = PhotoImage(file = "what-if-poster.gif")
ctn14_canvas.create_image(63,77, image = img14)

lbl14= Label(window,text="What if...?", relief="sunken", bd=1)
lbl14.place(x=825, y=465)
lbl_1 = Label(window, text = "7.5", relief="sunken", bd=1)
lbl_1.place(x=845, y=485)


ctn15_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn15_canvas.place(x=940, y=273)

img15 = PhotoImage(file = "the-adventures-of-tintin-poster.gif")
ctn15_canvas.create_image(63,77, image = img15)

lbl15= Label(window,text="The Adventures of Tintin", relief="sunken", bd=1)
lbl15.place(x=940, y=465)
lbl_15 = Label(window, text = "7.3", relief="sunken", bd=1)
lbl_15.place(x=995, y=485)


ctn16_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn16_canvas.place(x=1095, y=273)

img16 = PhotoImage(file = "aquaman-poster.gif")
ctn16_canvas.create_image(63,77, image = img16)

lbl16= Label(window,text="Aquaman", relief="sunken", bd=1)
lbl16.place(x=1135, y=465)
lbl_16 = Label(window, text = "6.9", relief="sunken", bd=1)
lbl_16.place(x=1155, y=485)


ctn17_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn17_canvas.place(x=10, y=528)

img17 = PhotoImage(file = "mary-poppins-retuns-poster.gif")
ctn17_canvas.create_image(63,77, image = img17)

lbl17= Label(window,text="Mary Poppins Returns", relief="sunken", bd=1)
lbl17.place(x=15, y=715)
lbl_17 = Label(window, text = "6.7", relief="sunken", bd=1)
lbl_17.place(x=65, y=735)


ctn18_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn18_canvas.place(x=165, y=528)

img18 = PhotoImage(file = "lady-in-the-water-poster.gif")
ctn18_canvas.create_image(63,77, image = img18)

lbl18= Label(window,text="Lady in the Water", relief="sunken", bd=1)
lbl18.place(x=185, y=715)
lbl_18 = Label(window, text = "5.5", relief="sunken", bd=1)
lbl_18.place(x=220, y=735)


ctn19_canvas = Canvas(window, width = 125, height = 153, bd = 3,bg="black", relief = "solid")
ctn19_canvas.place(x=320, y=528)

img19 = PhotoImage(file = "white-wall-poster.gif")
ctn19_canvas.create_image(63,77, image = img19)

lbl19= Label(window,text="White Wall", relief="sunken", bd=1)
lbl19.place(x=355, y=715)
lbl_19 = Label(window, text = "4.2", relief="sunken", bd=1)
lbl_19.place(x=375, y=735)



window.mainloop()




