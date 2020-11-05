
import tkinter as tk
from tkinter import *
import tkinter.font as tf
import mysql.connector
import matplotlib.pyplot as plt
from PIL import ImageTk,Image
def graph_page():
   
    
    root = Toplevel()
    root.geometry("1920x1080+0+0")
    root.attributes("-fullscreen", True)
    root.title('Graph Page')
    root.configure(bg="#161A1D")
    
    
    newList = []
    def list_date_filtering():
        length_list = len(date_list)
        
        for i in range(0,length_list,1):
            temp = date_list[i]
            temp =str(temp).strip('[]')
            temp =str(temp).strip('datetime.date')
            temp =str(temp).strip('()')
            temp =str(temp).replace(', ','-')
            newList.append(temp)
        
    

    mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , 
                               password = 'aniket123', database = 'stock')
    mycursor = mydb.cursor()
    
    #Fetching Date
    mycursor.execute("select Date from gold")
    date = mycursor.fetchall()
    date_list = list(map(list, date))
    list_date_filtering()
    
    
    #Fetching price
    mycursor.execute("select price from gold")
    price = mycursor.fetchall()
    price_list = list(sum(price,()))
    
    
    graph_date = newList[-8:]
    graph_price = price_list[-8:]
    
    mainframe= Frame(root,bg="#161A1D")
    table_frame = Frame(mainframe , bd = 5)
    diff_frame =  Frame(mainframe ,bg="#161A1D")
    
    def difference():
        price_last = graph_price[-1]
        price_nd_lst = graph_price[-2]
        
        difference = price_last - price_nd_lst
        
        if difference >= 0 :
            diff = str(difference) + '↑'
            diff_label =  Label(diff_frame ,text = diff , font = ('Arial',20,'bold') , anchor = NW , fg = '#8bc34a',bg = '#161A1D')
            diff_label.pack(padx = 267 , side = TOP)
        else:
            diff = str(difference) + '↓'
            diff_label =  Label(diff_frame ,text = diff , font = ('Arial',20,'bold') , anchor = NW , fg = '#fe3636',bg = '#161A1D')
            #FOr predato,HP padx=267
            diff_label.pack(padx = 267 , side = TOP)

    class Table: 
      
        def __init__(self,root): 
              
            # code for creating table 
            color_text = ''
            color_background = ''
            self.e = Label(table_frame, width=13, fg='white', 
                                   font=('Arial',16,'bold'),
                                   text = 'Date',
                                   bd = 15 ,
                                   bg = 'black')
            self.e.grid(row=0 , column=0)
        
            self.e = Label(table_frame, width=13, fg='white', 
                                   font=('Arial',16,'bold'),
                                   text = 'Price',
                                   bd = 15 ,
                                   bg = 'black')
            self.e.grid(row=0 , column=1)
        
            for i in range(1,total_rows): 
                for j in range(total_columns): 
                    if i%2 == 1:
                        color_text = 'black'
                        color_background = 'white'
                    else:
                        color_text = 'white'
                        color_background = 'black'
                    
                    self.e = Label(table_frame, width=13, fg=color_text, 
                                   font=('Arial',16,'bold'),
                                   text = lst[i-1][j],
                                   bd = 15 ,
                                   bg = color_background) 
                    
                    self.e.grid(row=i, column=j) 



    difference()
    diff_frame.pack(anchor = NW , side = BOTTOM , padx = (80,0), pady = (0,50))   
    table_frame.pack(padx=(80,0),side=LEFT , pady = 0)
       
             


    test_list = []

    for i in range (0,8,1):
        test_array = []
        test_array.append(graph_date[i])
        test_array.append(graph_price[i])
        temp = tuple(test_array)
        test_list.append(temp)


# take the data 
    lst = test_list 

# find total number of rows and 
# columns in list 
    total_rows = 9
    total_columns = 2
   
# create root window 
    t = Table(root)


#Graph Plotting
    fig = plt.figure(figsize=(13,10))
#fig.patch.set_facecolor('#e9ecef')
    plt.xlabel('Date')
    plt.ylabel('Gold Rate')
    plt.plot(graph_date,graph_price,color="#e9ecef")
    ax=plt.gca()
    ax.set_facecolor('#161a1d')

    plt.xticks(rotation = 'vertical')
#plt.show()
    fig.savefig('Graph.png')


#Show Graph
    C = Canvas(mainframe, width=936, height=720)
    filename = ImageTk.PhotoImage(file = 'Graph.png')
    graph_label = Label(C , image=filename)
    graph_label.config(width=936, height=720)
    graph_label.pack()
#For Predator,HP pady=7
    C.pack(anchor=CENTER,pady=7)

    mainframe.pack(fill=X, expand=TRUE)
    root.bind("<Escape>", lambda event: root.destroy())
    mainloop()
    
def call_function():
    graph_page()