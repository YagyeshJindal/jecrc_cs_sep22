import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tkt

app = tkt.Tk()
app.geometry('600x300')
app.title('Treadmill Users Analysis')

rb1 = tkt.Variable(app)
values = {'data 1': '1','data 2': '2'}
for key,value in values.items():
    tkt.Radiobutton(app, text = key, variable=rb1 , value=value).pack()

def show():
    print(rb1.get())

tkt.Button(app, text='Show', command=show).place(x=400, y = 10)

app.mainloop()