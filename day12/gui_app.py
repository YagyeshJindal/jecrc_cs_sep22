# gui - graphical user interface
#libraries :-
#1. tkinter
#2. PyQT
#3. Turtle

import tkinter as tkt

app = tkt.Tk()

app.title('my app')
app.geometry('600x400')
tkt.Label(app, text = 'a simple text label').place(x=50,y=50)
tkt.Label(app,text = 'yagyesh jindal').place(x=100,y=100)

app.mainloop() 