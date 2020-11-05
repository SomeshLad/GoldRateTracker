import Graph_Page as GP
import tkinter as tk
from tkinter import *
import tkinter.font as tf
import mysql.connector
from datetime import datetime
import runpy
 
#SQL DATA
query1 = "INSERT INTO gold VALUES(%s, %s)"
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , 
password = 'aniket123', database = 'stock')
 
mycursor = mydb.cursor()
date= datetime.now()
######

root = Tk()
root.geometry("1390x1080+0+0")
root.attributes("-fullscreen", True)
# add widgets here
 
root.title('Stock')
hed = Label(root, text = "Gold Rate Tracker", bg = "#403d39",fg="#e9ecef",font="Times 50 underline bold")
hed.pack(fill=X)
 
instruction = Label(root, text = "Instructions:",bg = "#343a40",fg="#ced4da",font="Times 25 bold" , anchor = NW, padx=15, pady=10)
instruction.pack(pady=(20,8),padx=100, fill=X) 
 
fontstyle=tf.Font(family="Times",size= 20, weight= "bold")
 
instruction_Message = Label(root, 
text = """  1. Enter the current value of gold in the given input box.\n  2. After entering the gold rate, click on "Generate Button".\n  3. We recommend not to enter multiple values on a single day.\n  4. Once you click the "Generate Button" you will be taken to the "Graph Page".\n  5. Press "Escape(Esc)" Key to Exit.""",bg = "#333333",fg="#e9ecef",
font=fontstyle, justify = LEFT , anchor = NW, padx=30,pady=10) 
instruction_Message.pack(pady = 0 ,padx=100,fill = X)
 
 
#Testing 
baseFrame = Frame(root,bg="#343a40",highlightbackground="#343a40",
highlightthickness =10)
baseFrame.pack(pady=10)
 
 
#########
 
frame = Frame(baseFrame,
bg="#343a40")
frame.pack(pady = 20)
 
buttonFrame = Frame(baseFrame)
buttonFrame.pack()
 
price = Label(frame , text = "Enter Current Gold Rate: " ,
bg="#343a40",
fg = "#cccccc", 
font = "Times 25 bold", 
anchor = NW,
pady=10,
# padx=30
)
price.pack(padx=10, pady = 20,side=LEFT)
 
def delete_text(e):
    entry.delete(0,5)
    
 
entry = Entry(frame,font ='Times 18',width = 10,bg='#cccccc',fg='#333333')
entry.insert(0,'Price')
entry.bind("<Button-1>", delete_text)
entry.pack(padx=(0,10) ,pady = 20,side=LEFT)
 
 
 
# price.config(justify = LEFT)
 
#Button functions 
 
def on_enter(e):
    generate['background'] = '#e9ecef',
    generate['foreground'] = '#333333'
 
def on_leave(e):
    generate['background'] = '#333333',
    generate['foreground'] = '#e9ecef'
 
def fetch_value(e):
    val=int(entry.get())
    print(val)
    delete_text(e)
    data = (date,val)
    mycursor.execute(query1,data)
    mydb.commit()
#    runpy.run_path('GraphPage.py')
 
 
 
#Button Properties
generate = Button(buttonFrame,
bg = "#333333",
fg="#e9ecef",
text = 'Generate',
anchor = CENTER,
font = 'Times 20 bold',
justify = CENTER,
activebackground ="#323739",
activeforeground ="#f8f9fa",
highlightcolor = "#cccccc",
command = GP.call_function
)
generate.pack(side = BOTTOM)

#on Call functions 
generate.bind("<Enter>", on_enter)
generate.bind("<Leave>", on_leave)
generate.bind("<Button-1>", fetch_value)
root.bind("<Escape>", lambda event: root.destroy())
 
root.configure(bg="#161A1D")

mainloop()
 
