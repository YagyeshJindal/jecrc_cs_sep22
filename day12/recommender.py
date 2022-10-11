import tkinter as tkt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import os
print('location is :', os.getcwd(),'\n\n\n')

app = tkt.Tk()

app.title('recommendation system')
app.geometry('400x400')

cols=['user_id','movie_id','rating','ts']
df = pd.read_csv('u.data',sep = '\t',names=cols).drop('ts',axis=1)
item_cols=['movie_id','title']+[str(i) for i in range(22)]
df1=pd.read_csv('u.item',sep='|',names=item_cols,encoding = "ISO-8859-1")[['movie_id','title']]
movie = pd.merge(df,df1,on='movie_id')

result = tkt.Variable(app)

frame = tkt.Frame(app)
frame.place(x=10,y=10)

box = tkt.Listbox(app, height=10)
for title in movie['title'].unique():
    box.insert(tkt.END, title)
box.pack(side='left',fill='y')
# box.place(x=10,y=10)

scroll = tkt.Scrollbar(frame, orient=tkt.VERTICAL)
scroll.config(command= box.yview)
box.config(yscrollcommand=scroll.set)
scroll.pack(side='right',fill='y')

def get_movie():
    movie_selected = box.get(box.curselection())
    print('movie selected :', movie_selected)

movie_pivot = movie.pivot_table(index = 'user_id',columns = 'title',values = 'rating')
    
# find the similarity for selected movie
corrs = movie_pivot.corrwith(movie_pivot[movie_selected])
corrs_df = pd.DataFrame(corrs , columns = ['Correlation'])
corrs_df['rating'] = movie.groupy('title')['rating'].mean()
corrs_df['count'] = movie['title'].value_counts()
    
top_recom = list(corrs_df[corrs_df['count']>50].sort_values(by = 'Correlation',ascending = False).head(20).index)

if movie_selected in top_recom:
    top_recom.remove(movie_selected)
print('recommendation:',top_recom)    

if top_recom:
    result.set(top_recom[0])
else:
    result.set('sorry no recommendations found')    

tkt.Button(app, text='find recommendations', font=('Arial',10), command=get_movie).place(x=200,y=50)
tkt.Label(app, textvariable=result, font=('Arial',10)).place(x=10,y=300)

app.mainloop()