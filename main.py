import tkinter as tk
from tkinter import *
import hex


win = Tk()

win.geometry('600x300')
######### R scale and R labels ###########
R_value = IntVar()
R_scale = Scale(win,orient=HORIZONTAL, to=255, length=500, showvalue=False, variable=R_value)
R_scale.place(relx=0.05, rely=0.7, anchor=W)

R_symbol = Label(text='R')
R_symbol.place(relx=0.02, rely=0.7, anchor=W)

R_value_label = Label(text=R_value.get())
R_value_label.place(relx=0.9, rely=0.7, anchor=W)

def update_R_label(a,b,c):
    R_value_label.config(text=R_value.get())
    update_Color_Window()

R_value.trace('w',update_R_label) #iniciate update_R_label when R_value cheange

def take_R_value():
    var = R_value.get()
    return var

######### G scale and G labels ###########
G_value = IntVar()
G_scale = Scale(win,orient=HORIZONTAL, to=255, length=500, showvalue=False, variable=G_value)
G_scale.place(relx=0.05, rely=0.8, anchor=W)

B_symbol = Label(text='B')
B_symbol.place(relx=0.02, rely=0.8, anchor=W)

G_value_label = Label(text=G_value.get())
G_value_label.place(relx=0.9, rely=0.8, anchor=W)

def update_G_label(a,b,c):
    G_value_label.config(text=G_value.get())
    update_Color_Window()

G_value.trace('w',update_G_label) #iniciate update_G_label when G_value cheange

def take_G_value():
    var = G_value.get()
    return var

######### B scale and B labels ###########
B_value = IntVar()
B_scale = Scale(win,orient=HORIZONTAL, to=255, length=500, showvalue=False, variable=B_value)
B_scale.place(relx=0.05, rely=0.9, anchor=W)

G_symbol = Label(text='G')
G_symbol.place(relx=0.02, rely=0.9, anchor=W)

B_value_label = Label(text=B_value.get())
B_value_label.place(relx=0.9, rely=0.9, anchor=W)

def update_B_label(a,b,c):
    B_value_label.config(text=B_value.get())
    update_Color_Window()

B_value.trace('w',update_B_label) #iniciate update_B_label when B_value cheange

def take_B_value():
    var = B_value.get()
    return var

######################################
########### Color window #############
def update_Color_Window():
    Color_Window.config(bg=hex.combine_hex(take_R_value(),take_G_value(),take_B_value()))

Color_Window = Frame(win,width=100,height=100,bg='#000000')
Color_Window.place(relx=0.5, rely=0.3)

win.mainloop()

