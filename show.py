import tkinter as tk
from tkinter import *


def showResultForTourism(result,tourism):
    root = Tk()
    root.withdraw()

    top=tk.Toplevel(root)

    top.geometry("940x520")
    top.configure(background='#bfbf9d')
    if len(result)==0:
        label=Label(top,text="Sorry, No place found in database which fulfilling your requirement :-(", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.grid(row=0,column=0,columnspan=5, ipadx=200)
    else:
        label=Label(top,text="Best suited places as per your requirements are following:", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.grid(row=0,column=0,columnspan=5, ipadx=190)
        label1=Label(top,text="", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
        label1.grid(row=1,column=0,columnspan=5, ipadx=100)
        
        name=Label(top,text="Name of place", font=200, fg='red', padx=10, pady=10, bg='white')
        name.grid(row=2,column=0)
        name1=Label(top,text="Country", font=200, fg='red', padx=10, pady=10, bg='white')
        name1.grid(row=2,column=1)
        rating=Label(top,text="Budget", font=200, fg='red', padx=10, pady=10, bg='white')
        rating.grid(row=2,column=2)
        price=Label(top,text="Type of Place", font=200, fg='red', padx=10, pady=10, bg='white')
        price.grid(row=2,column=3)

        cnt=1
        j=3
        for item in result:
            if cnt==0:
                break
            name=Label(top,text=item, font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            name.grid(row=j,column=0)
            name1=Label(top,text=tourism[item]["country"], font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            name1.grid(row=j,column=1)
            rating=Label(top,text=tourism[item]["budget"], font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            rating.grid(row=j,column=2)
            price=Label(top,text=str(tourism[item]["type of place"]), font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            price.grid(row=j,column=3)

            cnt+=1
            j+=1
        button1 = Button(top,text='Exit', font=70, padx=10, pady=10, command=  root.destroy , fg='red', bg='#fac370')
        button1.grid(row = j,column=2)

        root.mainloop()


def showResultForLive(result,countryDetails):
    root = Tk()
    root.withdraw()

    top=tk.Toplevel(root)
    j=3

    top.geometry("940x520")
    top.configure(background='#bfbf9d')
    if len(result)==0:
        print("i was here")
        label=Label(top,text="Sorry, No country found in database which fulfilling your requirement :-(", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.grid(row=0,column=0,columnspan=5, ipadx=200)
    else:
        label=Label(top,text="Best suited countries as per your requirements are following:", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.grid(row=0,column=0,columnspan=5, ipadx=190)
        label1=Label(top,text="", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
        label1.grid(row=1,column=0,columnspan=5, ipadx=100)
        
        name=Label(top,text="Country", font=200, fg='red', padx=10, pady=10, bg='white')
        name.grid(row=2,column=0)
        name1=Label(top,text="Average Weather", font=200, fg='red', padx=10, pady=10, bg='white')
        name1.grid(row=2,column=1)
        rating=Label(top,text="Type of Government", font=200, fg='red', padx=10, pady=10, bg='white')
        rating.grid(row=2,column=2)
        price=Label(top,text="Major Religion", font=200, fg='red', padx=10, pady=10, bg='white')
        price.grid(row=2,column=3)

        cnt=1
        
        for item in result:
            if cnt==0:
                break
            name=Label(top,text=item, font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            name.grid(row=j,column=0)
            name1=Label(top,text=countryDetails[item]["average weather"], font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            name1.grid(row=j,column=1)
            rating=Label(top,text=countryDetails[item]["type of government"], font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            rating.grid(row=j,column=2)
            price=Label(top,text=countryDetails[item]["major religion"], font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            price.grid(row=j,column=3)

            cnt+=1
            j+=1
    button1 = Button(top,text='Exit', font=70, padx=10, pady=10, command=  root.destroy , fg='red', bg='#fac370')
    button1.grid(row = j,column=2)

    root.mainloop()


def showResultForBuss(result,countryDetails):
    root = Tk()
    root.withdraw()
    j=3
    top=tk.Toplevel(root)

    top.geometry("940x520")
    top.configure(background='#bfbf9d')
    if len(result)==0:
        label=Label(top,text="Sorry, No country found in database which fulfilling your requirement :-(", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.grid(row=0,column=0,columnspan=5, ipadx=200)
    else:
        label=Label(top,text="Best countries places as per your requirements are following:", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.grid(row=0,column=0,columnspan=5, ipadx=190)
        label1=Label(top,text="", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
        label1.grid(row=1,column=0,columnspan=5, ipadx=100)
        
        name=Label(top,text="Country", font=200, fg='red', padx=10, pady=10, bg='white')
        name.grid(row=2,column=0)
        name1=Label(top,text="Import/Export", font=200, fg='red', padx=10, pady=10, bg='white')
        name1.grid(row=2,column=1)
        rating=Label(top,text="Value of Import/Export", font=200, fg='red', padx=10, pady=10, bg='white')
        rating.grid(row=2,column=2)
        price=Label(top,text="Field", font=200, fg='red', padx=10, pady=10, bg='white')
        price.grid(row=2,column=3)

        cnt=1
        j=3
        for item in result:
            if cnt==0:
                break
            name=Label(top,text=item, font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            name.grid(row=j,column=0)
            name1=Label(top,text=countryDetails[item]["trade type"], font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            name1.grid(row=j,column=1)
            rating=Label(top,text=countryDetails[item][countryDetails[item]["trade type"]], font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            rating.grid(row=j,column=2)
            price=Label(top,text=countryDetails[item]["field domain"], font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            price.grid(row=j,column=3)

            cnt+=1
            j+=1
    button1 = Button(top,text='Exit', font=70, padx=10, pady=10, command=  root.destroy , fg='red', bg='#fac370')
    button1.grid(row = j,column=2)

    root.mainloop()


def showResultForJob(result,countryDetails):
    root = Tk()
    root.withdraw()
    j=3
    top=tk.Toplevel(root)

    top.geometry("940x520")
    top.configure(background='#bfbf9d')
    if len(result)==0:
        label=Label(top,text="Sorry, No country found in database which fulfilling your requirement :-(", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.grid(row=0,column=0,columnspan=5, ipadx=200)
    else:
        label=Label(top,text="Best countries places as per your requirements are following:", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.grid(row=0,column=0,columnspan=5, ipadx=190)
        label1=Label(top,text="", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
        label1.grid(row=1,column=0,columnspan=5, ipadx=100)
        
        name=Label(top,text="Country", font=200, fg='red', padx=10, pady=10, bg='white')
        name.grid(row=2,column=0)
        price=Label(top,text="Field", font=200, fg='red', padx=10, pady=10, bg='white')
        price.grid(row=2,column=3)

        cnt=1
        j=3
        for item in result:
            if cnt==0:
                break
            name=Label(top,text=item, font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            name.grid(row=j,column=0)

            price=Label(top,text=countryDetails[item]["field domain"], font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            price.grid(row=j,column=3)

            cnt+=1
            j+=1
    button1 = Button(top,text='Exit', font=70, padx=10, pady=10, command=  root.destroy , fg='red', bg='#fac370')
    button1.grid(row = j,column=2)

    root.mainloop()
