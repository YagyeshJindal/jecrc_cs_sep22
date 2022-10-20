import tkinter as tkt
import pandas as pd

model = pd.read_pickle('SurvivalPredictionRF.pickle')

app = tkt.Tk()
app.geometry('300x200')
app.title('Titanic Survival Prediction')

cols = ['Sex_male','Fare','Age']

tkt.Label(app, text = 'Choose gender', padx = 20, pady = 20).grid(row = 0, column=0)
genders = {
    'Male': 1,
    'Female':0
}
genderVar = tkt.Variable(app)
genderVar.set(genders['Male'])
frame = tkt.Frame(app)
frame.grid(row=0, column =1)
for gender , genderValue in genders.items():
    tkt.Radiobutton(frame, text = gender , variable=genderVar, value=genderValue).pack(side=tkt.LEFT)

# Fare
tkt.Label(app, text='Enter Fare', padx=20, pady=5).grid(row=1, column=0) 
fareVar= tkt.DoubleVar(app)
fareVar.set(0.0)
tkt.Spinbox(app, from_=0, to = 10000, textvariable=fareVar, width=10).grid(row=1, column=1)

# Age
tkt.Label(app , text='Enter Age', padx=20, pady=10).grid(row=2, column=0)
ageVar= tkt.IntVar(app)
ageVar.set(0)
tkt.Spinbox(app, from_=0, to = 10000, textvariable=ageVar, width=10).grid(row=2, column=1)
# tkt.Entry(app, textvariable= fareVar).grid(row=1, column=1)

# Prediciton Button
def find_survival():
    global model
    query_df= pd.DataFrame({'Sex_male':[genderVar.get()], 'Fare':[fareVar.get()], 'Age':[ageVar.get()]})

    pred = model.predict(query_df)
    if pred[0]==1:
        resultVar.set('Might Survive')
    else:
        resultVar.set('Might Not Survive')    
    return

tkt.Button(app, text='Check', command= find_survival, padx=20, pady= 2).grid(row=3, column=0, columnspan=2)    

# Result
resultVar= tkt.Variable(app)
tkt.Label(app, textvariable=resultVar, font=('Times New Roman',20)).grid(row=4,column=0,columnspan=2)


app.mainloop()    