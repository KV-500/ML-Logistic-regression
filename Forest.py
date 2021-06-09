import pandas  as pd
import numpy as np
import tkinter as tk
import cv2,os
import csv
from PIL import Image
import datetime
import time
from tkinter import messagebox
from tkinter import *


window =tk.Tk()
window.title("FOREST")
window.configure(background='yellow')

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

x_cord = 75;
y_cord = 20;
checker=0;


lbl = tk.Label(window, text="Probability of fire occuring",width=20  ,height=1  ,fg="black"  ,bg="yellow" ,font=('Times New Roman', 25, ' bold ') ) 
lbl.place(x=450-x_cord, y=500-y_cord)

message3 = tk.Label(window, text="" ,bg="white"  ,fg="blue"  ,width=5  ,height=1, activebackground = "white" ,font=('Times New Roman', 25, ' bold ')) 
message3.place(x=850-x_cord, y=500-y_cord)


message2 = tk.Label(window, text="" ,bg="white"  ,fg="blue"  ,width=50  ,height=1, activebackground = "white" ,font=('Times New Roman', 15, ' bold ')) 
message2.place(x=500-x_cord, y=550-y_cord)



message = tk.Label(window, text="Forest Fire Prevention" ,bg="yellow"  ,fg="black"  ,width=40  ,height=1,font=('Times New Roman', 35, 'bold underline')) 
message.place(x=200, y=20)

message = tk.Label(window, text="Predict the probability of Forest-Fire Occurence" ,bg="yellow"  ,fg="black"  ,width=40  ,height=1,font=('Times New Roman', 12, 'bold')) 
message.place(x=575, y=80)



lbl = tk.Label(window, text="Temperature",width=20  ,height=2  ,fg="black"  ,bg="yellow" ,font=('Times New Roman', 25, ' bold ') ) 
lbl.place(x=200-x_cord, y=200-y_cord)


txt = tk.Entry(window,width=30,bg="white" ,fg="blue",font=('Times New Roman', 15, ' bold '))
txt.place(x=250-x_cord, y=300-y_cord)

lbl2 = tk.Label(window, text="Oxygen",width=20  ,fg="black"  ,bg="yellow"    ,height=2 ,font=('Times New Roman', 25, ' bold ')) 
lbl2.place(x=600-x_cord, y=200-y_cord)



txt2 = tk.Entry(window,width=30  ,bg="white"  ,fg="blue",font=('Times New Roman', 15, ' bold ')  )
txt2.place(x=650-x_cord, y=300-y_cord)

lbl3 = tk.Label(window, text="Humidity",width=20  ,fg="black"  ,bg="yellow"  ,height=2 ,font=('Times New Roman', 25, ' bold ')) 
lbl3.place(x=1000-x_cord, y=200-y_cord)

txt3 = tk.Entry(window,width=30  ,bg="white"  ,fg="blue",font=('Times New Roman', 15, ' bold ')  )
txt3.place(x=1060-x_cord, y=300-y_cord)


def Train():
       dataset=pd.read_csv('Forest_fire.csv')
       #print(dataset)
       dataset.drop(['Area'],axis=1,inplace=True)#print(dataset)
       X=dataset.iloc[:,:-1].values
       #print(X)
       Y=dataset.iloc[:,3].values
       #print(Y)
       from sklearn.model_selection import train_test_split
       X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20,random_state=0)
       from sklearn.linear_model import LogisticRegression
       log=LogisticRegression()
       log.fit(X_train,Y_train)
       #print(X_train)
       pred=log.predict(X_test)
       #print(pred)
       New_tem=float(txt.get())
       New_oxy=float(txt2.get())
       New_hum=float(txt3.get())

       
       pred1=log.predict([[New_tem,New_oxy,New_hum]])
       #print(pred1)
       res1 = pred1 
       if(pred1>=0.5):
          res = "The Forest is Danger" 
       else:
          res = "The Forest is safe"
       message2.configure(text= res)
       message3.configure(text= res1)
       
def quit_window():
   MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
   if MsgBox == 'yes':
       tk.messagebox.showinfo("Greetings", "Thank You very much for using our software. Have a nice day ahead!!")
       window.destroy()



trainImg = tk.Button(window, text="PREDICT", command=Train  ,fg="white"  ,bg="blue"  ,width=25  ,height=2, activebackground = "blue" ,font=('Times New Roman', 15, ' bold '))
trainImg.place(x=645-x_cord, y=425-y_cord)

quitWindow = tk.Button(window, text="QUIT", command=quit_window  ,fg="white"  ,bg="blue"  ,width=10  ,height=2, activebackground = "pink" ,font=('Times New Roman', 15, ' bold '))
quitWindow.place(x=1000, y=735-y_cord)

window.mainloop()

