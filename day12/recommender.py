import tkinter as tkt

app = tkt.Tk()

app.title('recommendation system')
app.geometry('400x400')

result = tkt.Varaible(app)
box = tkt.Listbox(app, height=10)
box.place(x=10,y=10)

def get_movie():
    pass

tkt.Button(app, text='find recommendations', font=('Arial',10), command=get_movie).place(x=200,y=50)
tkt.Label(app, textvariable=result, font=('Arial',10)).place(x=200,y=100)

app.mainloop()