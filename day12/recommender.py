import tkinter as tkt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

app = tkt.Tk()

app.title('recommendation system')
app.geometry('400x400')

cols=['user_id','movie_id','rating','ts']
df = pd.read_csv('u.data',sep = '\t',names=cols).drop('ts',axis=1)
item_cols=['movie_id','title']+[str(i) for i in range(22)]
df1=pd.read_csv('u.item',sep='|',names=item_cols,encoding = "ISO-8859-1")[['movie_id','title']]
movie = pd.merge(df,df1,on='movie_id')

result = tkt.Varaible(app)
box = tkt.Listbox(app, height=10)
for row, val in movie.iterrows():
    print(val['title'])
    box.insert(row+1, val['title'])
box.place(x=10,y=10)

def get_movie():
    pass

tkt.Button(app, text='find recommendations', font=('Arial',10), command=get_movie).place(x=200,y=50)
tkt.Label(app, textvariable=result, font=('Arial',10)).place(x=200,y=100)

app.mainloop()