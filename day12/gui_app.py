# gui - graphical user interface
#libraries :-
#1. tkinter
#2. PyQT
#3. Turtle

import tkinter as tkt

app = tkt.Tk()

app.title('my app')
app.geometry('600x400')

msg = tkt.Variable(app)
print(msg.get())
msg.set('empty')
print(msg.get())

tkt.Label(app, text = 'a simple text label').place(x=10,y=10)
tkt.Label(app , textvariable=msg).place(x=10,y=30)

def abc():
    print('wow')
    msg.set('jo tea ra man kre')

tkt.Label(app, text = 'yagyesh jindal').place(x=10,y=50)
tkt.Button(app, text = 'isko click kr', command = abc).place(x=10,y=70)
tkt.Button(app, text ='y wala bhi h', command = lambda:msg.set('pta nhi')).place(x=10,y=90)

f1 = tkt.Variable(app)
f1.set('0')
f2 = tkt.Variable(app)
f2.set('0')
result = tkt.Variable(app)

tkt.Entry(app, textvariable=f1, font=('Arial',10)).place(x=10,y=110)
tkt.Entry(app, textvariable=f2, font=('Arial',10)).place(x=10,y=130)
tkt.Label(app, text='result').place(x=100,y=130)
tkt.Label(app, textvariable=result, font=('Arial',10)).place(x=200,y=130)

def calc(op):
    print('i will calc')
    result.set(eval(f1.get()+op+f2.get()))

tkt.Button(app, text='+', command=lambda:calc('+') , font=('Arial',10)).place(x=10,y=150)
tkt.Button(app, text='-', command=lambda:calc('-') , font=('Arial',10)).place(x=30,y=150)
tkt.Button(app, text='*', command=lambda:calc('*') , font=('Arial',10)).place(x=50,y=150)
tkt.Button(app, text='/', command=lambda:calc('/') , font=('Arial',10)).place(x=70,y=150)

app.mainloop() 