import tkinter as tk
from tkinter import *
import hex
import pyperclip #This help to copy to clipboard


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

######### G scale and G labels ###########
G_value = IntVar()
G_scale = Scale(win,orient=HORIZONTAL, to=255, length=500, showvalue=False, variable=G_value)
G_scale.place(relx=0.05, rely=0.8, anchor=W)

G_symbol = Label(text='G')
G_symbol.place(relx=0.02, rely=0.8, anchor=W)

G_value_label = Label(text=G_value.get())
G_value_label.place(relx=0.9, rely=0.8, anchor=W)

def update_G_label(a,b,c):
    G_value_label.config(text=G_value.get())
    update_Color_Window()

G_value.trace('w',update_G_label) #iniciate update_G_label when G_value cheange

######### B scale and B labels ###########
B_value = IntVar()
B_scale = Scale(win,orient=HORIZONTAL, to=255, length=500, showvalue=False, variable=B_value)
B_scale.place(relx=0.05, rely=0.9, anchor=W)

B_symbol = Label(text='B')
B_symbol.place(relx=0.02, rely=0.9, anchor=W)

B_value_label = Label(text=B_value.get())
B_value_label.place(relx=0.9, rely=0.9, anchor=W)

def update_B_label(a,b,c):
    B_value_label.config(text=B_value.get())
    update_Color_Window()

B_value.trace('w',update_B_label) #iniciate update_B_label when B_value cheange


######################################
########### Color window #############
def update_Color_Window():
    Color_Window.config(bg=hex.combine_hex(R_value.get(),G_value.get(),B_value.get()))

    if can_update_hex_entry:
        Hex_Entry_Value.set(hex.combine_hex(R_value.get(), G_value.get(), B_value.get())) #This update Hex Entry

Color_Window = Frame(win, width=100, height=100, bg='#000000')
Color_Window.place(relx=0.5, rely=0.25, anchor=CENTER)




def Copy(color):
    value = color
    pyperclip.copy(value)

Color_Copy_Button = Button(win, text='Copy', command=lambda: Copy(hex.combine_hex(R_value.get(),G_value.get(),B_value.get())))
Color_Copy_Button.place(relx=0.55, rely=0.5, anchor=CENTER)

###########################################
############# Hex Entry ###################

Hex_Entry_Value = StringVar()
Hex_Entry_Value.set("#000000")
global can_update
can_update_hex_entry = True

Hex_Entry = Entry(textvariable = Hex_Entry_Value)

Hex_Entry.place(relx=0.457, rely=0.5,width=50,anchor=CENTER)

def character_limit(entry_text):
    if len(entry_text.get()) > 7:
        entry_text.set(entry_text.get()[:-1])
    if hex.hex_validation(entry_text.get()) and len(entry_text.get()) > 6:
        global can_update_hex_entry
        can_update_hex_entry = False
        R_value.set(int(entry_text.get()[1:3], 16))
        G_value.set(int(entry_text.get()[3:5], 16))
        B_value.set(int(entry_text.get()[5:7], 16))
        can_update_hex_entry = True

Hex_Entry_Value.trace("w", lambda *args: character_limit(Hex_Entry_Value))

win.mainloop()

