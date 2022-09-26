import tkinter as tk
import random

win = tk.Tk()
canvas = tk.Canvas(win, width=400, height=450, bg="#bfbfbf")
canvas.pack()
voda = []
zem = []
piczem = tk.PhotoImage(file="images/ostrov0.png")
picvoda = tk.PhotoImage(file="images/ostrov3.png")
obrazky = [tk.PhotoImage(file="images/ostrov_kruh0.png"),tk.PhotoImage(file="images/ostrov_kruh1.png")]
mosty = [tk.PhotoImage(file="images/ostrov1.png"),tk.PhotoImage(file="images/ostrov2.png")]
sirobr = 50
vysobr = 50
prepinac = 0
money = 0

def click_switch(e):
    global prepinac
    if canvas.itemcget("switcher", "image") == "pyimage3":
        canvas.itemconfig("switcher", image=obrazky[1])
        prepinac = 1
    elif canvas.itemcget("switcher", "image") == "pyimage4":
        canvas.itemconfig("switcher", image = obrazky[0])
        prepinac = 0
    print(prepinac)

def trier(e):
    global prepinac, money, text
    if prepinac == 0:
        x = (e.x//50)*50
        y = (e.y//50)*50
        idecko = canvas.find_withtag("current")[0]
        canvas.delete(idecko)
        canvas.create_image(x, y, image = mosty[0], anchor = "nw", tags="bridge")
        money += 10
    elif prepinac == 1:
        x = (e.x//50)*50
        y = (e.y//50)*50
        idecko = canvas.find_withtag("current")[0]
        canvas.delete(idecko)
        canvas.create_image(x, y, image = piczem, anchor = "nw")
        money += 50
    text.config(text = money)


def counter(e):
    global money
    text.config(text=money)

def rotator(e):
    global prepinac
    if prepinac == 0:
        if canvas.itemcget("current", "image") == "pyimage5":
            canvas.itemconfig("current", image=mosty[1])
        elif canvas.itemcget("current", "image") == "pyimage6":
            canvas.itemconfig("current", image = mosty[0])

def create_screen():
    global zem, money, text
    m = random.randint(4,6)
    n = random.randint(3,9)
    for stlpec in range(n):
        for riadok in range(m):
            ran = random.randint(0,5)
            if ran == 1:
                temp = canvas.create_image(riadok * sirobr, stlpec * vysobr, image = piczem, anchor = "nw")
                zem.append(temp)
            else:
                temp = canvas.create_image(riadok * sirobr, stlpec * vysobr, image = picvoda,anchor = "nw", tags = "water")
                voda.append(temp)
    canvas.create_image(400, 10, anchor = "ne", image = obrazky[0], tags = "switcher")
    text = tk.Label(text=money, bg="#bfbfbf", width=0, height=0)
    text.place(x=310, y=vysobr/2-10)
    text.config(font=('Helvatical bold', 20))

create_screen()
canvas.tag_bind("switcher", "<Button-1>", click_switch)
canvas.tag_bind("water", "<Button-1>", trier)
canvas.tag_bind("bridge", "<Button-1>", rotator)
canvas.bind("<Button-1>", counter)
win.mainloop()