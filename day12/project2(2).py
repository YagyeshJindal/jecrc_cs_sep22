import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tkt

data = pd.read_csv('treadmil-users.csv')

app = tkt.Tk()
app.geometry('600x300')
app.title('Treadmill Users Analysis')

graphs = tkt.Variable(app)
values = {
    'Pair Plot':"sns.pairplot(data=data)",
    'Joint Plot': "sns.jointplot(data=data, x='{col1}', y='{col2}')",
    'Bar Plot' : "sns.barplot(data=data, x='{col1}', y='{col2}')"
}
graphs.set(values['Pair Plot'])
y=10
for key,value in values.items():
    tkt.Radiobutton(app, text = key, variable=graphs , value=value).place(x=10,y=y)
    y += 20

# option menu 1
col1 = tkt.Variable(app)
values = ['Select','Product','Age','Gender']
col1.set(values[0])
tkt.Label(app, text='Column 1').place(x=100,y=10)
tkt.OptionMenu(app, col1, *values).place(x=100,y=40)    

# option menu 2
col2 = tkt.Variable(app)
col2.set(values[0])
tkt.Label(app, text='Column 2').place(x=100,y=80)
tkt.OptionMenu(app, col2, *values).place(x=100,y=110)    

# option menu 3
col3 = tkt.Variable(app)
col3.set(values[0])
tkt.Label(app, text='Column 3').place(x=100,y=150)
tkt.OptionMenu(app, col3, *values).place(x=100,y=180)

def show():
    column1 = col1.get()
    column2 = col2.get()
    column3 = col3.get()
    fig = plt.figure(figsize=(5,2))
    eval(graphs.get().format(col1 = column1 , col2 = column2 , col3 = column3))
    # print(col1.get(), col2.get(), col3.get())
    g= graphs.get()
    plt.show()

tkt.Button(app, text='Show', command=show).place(x=400, y = 10)

app.mainloop()