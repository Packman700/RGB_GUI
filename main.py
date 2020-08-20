import tkinter as tk
from tkinter import *
import hex
import pyperclip  # This help to copy to clipboard
import rgb_hls

win = Tk()

win.geometry('600x300')

  # This update all labels and windows



def update(a, b, c):

    R_value_label.config(text=R_value.get())
    G_value_label.config(text=G_value.get())
    B_value_label.config(text=B_value.get())


    # Bright_value.set(
    #     round(max([R_value.get(), G_value.get(), B_value.get()]) / (255 / 100)))  # Snap to max RGB value
    # Bright_value_label.config(text=(Bright_value.get()))

    Color1.set(rgb_hls.hue_change(R_value.get(), G_value.get(), B_value.get(), number=1, type=Palette_mode.get()))
    Color2.set(rgb_hls.hue_change(R_value.get(), G_value.get(), B_value.get(), number=2, type=Palette_mode.get()))
    Color4.set(rgb_hls.hue_change(R_value.get(), G_value.get(), B_value.get(), number=4, type=Palette_mode.get()))
    Color5.set(rgb_hls.hue_change(R_value.get(), G_value.get(), B_value.get(), number=5, type=Palette_mode.get()))

    update_Color_Window(Color_Window3,hex.combine_hex(R_value.get(),G_value.get(),B_value.get()))  # center color window
    update_Color_Window(Color_Window1,Color1.get())
    update_Color_Window(Color_Window2,Color2.get())
    update_Color_Window(Color_Window4,Color4.get())
    update_Color_Window(Color_Window5,Color5.get())

    if can_update_hex_entry: # This allows to enter color
        Hex_Entry_Value.set(hex.combine_hex(R_value.get(), G_value.get(), B_value.get()))  # This update Hex Entry

############## Menu Button ###############
Palette_Menu = Menubutton(text='Pallets',relief=RAISED)
Palette_Menu.place(relx=0.85, rely=0.85)

Palette_Menu.menu = Menu(Palette_Menu, tearoff=0)
Palette_Menu['menu'] = Palette_Menu.menu

Palette_mode = StringVar()
Palette_mode.set('Triad')

Palette_Menu.menu.add_radiobutton(label='Triad',variable=Palette_mode,value='Triad')
Palette_Menu.menu.add_radiobutton(label='Complementary',variable=Palette_mode,value='Complementary')
Palette_Menu.menu.add_radiobutton(label='Split-complementary',variable=Palette_mode,value='Split-complementary')
Palette_Menu.menu.add_radiobutton(label='Monochromatic',variable=Palette_mode,value='Monochromatic')
Palette_Menu.menu.add_radiobutton(label='Quadrangle',variable=Palette_mode,value='Quadrangle')
Palette_Menu.menu.add_radiobutton(label='Tetradic',variable=Palette_mode,value='Tetradic')
Palette_Menu.menu.add_radiobutton(label='Analog',variable=Palette_mode,value='Analog')



######### R scale and R labels ###########
R_value = IntVar()
R_scale = Scale(win,orient=HORIZONTAL, to=255, length=450, showvalue=False, variable=R_value)
R_scale.place(relx=0.05, rely=0.65, anchor=W)

R_symbol = Label(text='R')
R_symbol.place(relx=0.02, rely=0.65, anchor=W)

R_value_label = Label(text=R_value.get())
R_value_label.place(relx=0.82, rely=0.65, anchor=W)

R_value.trace('w', update)  # iniciate update_R_label when R_value cheange

######### G scale and G labels ###########
G_value = IntVar()
G_scale = Scale(win,orient=HORIZONTAL, to=255, length=450, showvalue=False, variable=G_value)
G_scale.place(relx=0.05, rely=0.75, anchor=W)

G_symbol = Label(text='G')
G_symbol.place(relx=0.02, rely=0.75, anchor=W)

G_value_label = Label(text=G_value.get())
G_value_label.place(relx=0.82, rely=0.75, anchor=W)

G_value.trace('w', update)  # iniciate update_G_label when G_value cheange

######### B scale and B labels ###########
B_value = IntVar()
B_scale = Scale(win, orient=HORIZONTAL, to=255, length=450, showvalue=False, variable=B_value)
B_scale.place(relx=0.05, rely=0.85, anchor=W)

B_symbol = Label(text='B')
B_symbol.place(relx=0.02, rely=0.85, anchor=W)

B_value_label = Label(text=B_value.get())
B_value_label.place(relx=0.82, rely=0.85, anchor=W)

B_value.trace('w', update)  # iniciate update_B_label when B_value cheange

# ########## Light scale and labels##########
# Bright_value = IntVar()
# Bright_scale = Scale(win, orient=HORIZONTAL, to=100, length=500, showvalue=False, variable=Bright_value)
#                      # ,command=lambda *args: update('a','b','c',Bright_move=True))
# # Bright_scale.bind("<ButtonRelease-1>",lambda *args: update('a','b','c',Bright_move=True))
#
# Bright_scale.place(relx=0.05, rely=0.95, anchor=W)
#
# Bright_symbol = Label(text=u'\u2600')
# Bright_symbol.place(relx=0.02, rely=0.95, anchor=W)
#
# Bright_value_label = Label(text=Bright_value.get())
#
# Bright_value_label.place(relx=0.9, rely=0.95, anchor=W)
#
# Bright_value.trace('w', update)  # iniciate update Bright_value_label when Bright_value cheange

######################################
########### Color window #############
def update_Color_Window(window_name,color):
    window_name.config(bg=color)

def Copy(color):
    value = color
    pyperclip.copy(value)

################## 1 ######################
Color1 = StringVar()
Color_Window1 = Frame(win, width=100, height=100, bg='#000000')
Color_Window1.place(relx=0.12, rely=0.25, anchor=CENTER)

Color_Copy_Button1 = Button(win, text='Copy', command=lambda: Copy(Color1.get()))
Color_Copy_Button1.place(relx=0.12, rely=0.5, anchor=CENTER)

################## 2 ######################
Color2 = StringVar()

Color_Window2 = Frame(win, width=100, height=100, bg='#000000')
Color_Window2.place(relx=0.31, rely=0.25, anchor=CENTER)

Color_Copy_Button2 = Button(win, text='Copy', command=lambda: Copy(Color2.get()))
Color_Copy_Button2.place(relx=0.31, rely=0.5, anchor=CENTER)

############## 3 Main ################
Color_Window3 = Frame(win, width=100, height=100, bg='#000000')
Color_Window3.place(relx=0.5, rely=0.25, anchor=CENTER)

Color_Copy_Button = Button(win, text='Copy', command=lambda: Copy(hex.combine_hex(R_value.get(),G_value.get(),B_value.get())))
Color_Copy_Button.place(relx=0.55, rely=0.5, anchor=CENTER)

################## 4 ######################
Color4 = StringVar()
Color_Window4 = Frame(win, width=100, height=100, bg='#000000')
Color_Window4.place(relx=0.69, rely=0.25, anchor=CENTER)

Color_Copy_Button4 = Button(win, text='Copy', command=lambda: Copy(Color4.get()))
Color_Copy_Button4.place(relx=0.69, rely=0.5, anchor=CENTER)

################## 5 ######################
Color5 = StringVar()
Color_Window5 = Frame(win, width=100, height=100, bg='#000000')
Color_Window5.place(relx=0.88, rely=0.25, anchor=CENTER)

Color_Copy_Button5 = Button(win, text='Copy', command=lambda: Copy(Color5.get()))
Color_Copy_Button5.place(relx=0.88, rely=0.5, anchor=CENTER)

###########################################
############# Hex Entry ###################
Hex_Entry_Value = StringVar()
Hex_Entry_Value.set("#000000")
global can_update
can_update_hex_entry = True

Hex_Entry = Entry(textvariable=Hex_Entry_Value)
Hex_Entry.place(relx=0.457, rely=0.5, width=50, anchor=CENTER)

def character_limit_enter_color(entry_text):
    if len(entry_text.get()) > 7:  # character limit
        entry_text.set(entry_text.get()[:-1])
    if hex.hex_validation(entry_text.get()) and len(entry_text.get()) > 6:  # enter color
        global can_update_hex_entry
        can_update_hex_entry = False
        R_value.set(int(entry_text.get()[1:3], 16))
        G_value.set(int(entry_text.get()[3:5], 16))
        B_value.set(int(entry_text.get()[5:7], 16))
        can_update_hex_entry = True

Hex_Entry_Value.trace("w", lambda *args: character_limit_enter_color(Hex_Entry_Value))




win.mainloop()

