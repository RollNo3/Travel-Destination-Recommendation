from experta import *
import zipfile, io, re, csv, sys
import tkinter as tk
from tkinter import *
from value_interpretor import *
from show import *
from csv_reader import *

result=[]
type1=0

class TourismSuggestion(Fact):
    budget= Field(float,mandatory=True)
    placeType= Field(str,mandatory=True)
    namep = Field(str,mandatory=True)
    country = Field(str,mandatory=True)

class TourismSuggestionActivation(Fact):
    budget= Field(float,mandatory=True)
    placeType= Field(str,mandatory=True)


class LiveSuggestion(Fact):
    climate= Field(str,mandatory=True)
    government= Field(str,mandatory=True)
    religion= Field(str,mandatory=True)
    country= Field(str,mandatory=True)

class LiveSuggestionActivation(Fact):
    climate= Field(str,mandatory=True)
    government= Field(str,mandatory=True)
    religion= Field(str,mandatory=True)


class BussSuggestion(Fact):
    importexport= Field(str,mandatory=False)
    worktype= Field(str,mandatory=True)
    country= Field(str,mandatory=True)

class BussSuggestionActivation(Fact):
    importexport= Field(str,mandatory=False)
    worktype= Field(str,mandatory=True)

class JobSuggestion(Fact):
    worktype= Field(str,mandatory=True)
    country= Field(str,mandatory=True)

class JobSuggestionActivation(Fact):
    worktype= Field(str,mandatory=True)

class WorkType(Fact):
    pass

class TourismType(Fact):
    pass

class Engine(KnowledgeEngine):

    @DefFacts()
    def set_tourism_facts(self):
        for item in tourism:
            yield TourismSuggestion(budget=float(tourism[item]["budget"]),placeType=tourism[item]["type of place"].lower(),namep=item,country=tourism[item]["country"])


    @DefFacts()
    def set_livejob_facts(self):
        for item in countryDetails:
            yield BussSuggestion(importexport=countryDetails[item]["trade type"].lower(),worktype=countryDetails[item]["field domain"].lower(),country=item)
            yield JobSuggestion(worktype=countryDetails[item]["field domain"].lower(),country=item)
            yield LiveSuggestion(climate=countryDetails[item]["average weather"].lower(),government=countryDetails[item]["type of government"].lower(),religion=countryDetails[item]["major religion"].lower(),country=item)

    @Rule()
    def start_up(self):

        
        root = Tk()
        root.withdraw()

        top=tk.Toplevel(root)
        top.geometry("1200x488")
        res = IntVar()

        res.set(1)


        label=Label(top,text="Choose the question you want to ask:", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.pack(anchor=W, fill=BOTH, expand=True)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)


        Radiobutton(top,text="I want to migrate to another country. Please help me decide which country will be best suitable for me to live in.",variable=res,value=1,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="I want to work in a country where I can earn most money. Where should I go?",variable=res,value=2,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="I want to travel to exotic places in the world. Can you suggest me some?",variable=res,value=3,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        button1 = Button(top,text='Next', font=70, padx=10, pady=10, command=  root.destroy , fg='red', bg='#fac370')
        button1.pack(anchor=W, fill=BOTH, expand=True)

        root.mainloop()
        self.declare(TourismType(res.get()))



    @Rule(TourismType(3))
    def tourism_suggestion(self):

        root = Tk()
        root.withdraw()

        top=tk.Toplevel(root)
        top.geometry("1200x488")
        res = IntVar()
        res.set(1)

        label=Label(top,text="What is your total budget (per person)", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.pack(anchor=W, fill=BOTH, expand=True)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)


        Radiobutton(top,text="Under lankh INR",variable=res,value=1,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="Between 1 lakh and 2 lakh",variable=res,value=2,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="Above 2 lakhs INR",variable=res,value=3,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)


        pl = IntVar()
        pl.set(1)

        label=Label(top,text="What type of place do you wanna go?", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.pack(anchor=W, fill=BOTH, expand=True)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)


        Radiobutton(top,text="1. Historical Place",variable=pl,value=1,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="2. Hill Station",variable=pl,value=2,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="3. Desert Safari",variable=pl,value=3,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="4. Beaches",variable=pl,value=4,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        button1 = Button(top,text='NEXT', font=70, padx=10, pady=10, command=  root.destroy , fg='red', bg='#fac370')
        button1.pack(anchor=W, fill=BOTH, expand=True)



        root.mainloop()

        c= getBudget(res.get())
        p= getPlaceType(pl.get())

        self.declare(TourismSuggestionActivation(budget=c,placeType=p))

        

    @Rule(TourismType(1))
    def live_suggestion(self):
        global type1
        type1=1
        root = Tk()
        root.withdraw()

        top=tk.Toplevel(root)
        top.geometry("1200x1488")


        c= IntVar()
        c.set(1)

        g= IntVar()
        g.set(1)

        r= IntVar()
        r.set(1)

        pl =IntVar()
        pl.set(1)

        label=Label(top,text="What kind of Population Desnity do you prefer?", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.pack(anchor=W, fill=BOTH, expand=True)


        Radiobutton(top,text="High",variable=pl,value=1,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)

        Radiobutton(top,text="Low",variable=pl,value=2,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        label=Label(top,text="What kind of Climate do you prefer?", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.pack(anchor=W, fill=BOTH, expand=True)


        Radiobutton(top,text="Cold",variable=c,value=1,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)

        Radiobutton(top,text="Moderate",variable=c,value=2,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)

        Radiobutton(top,text="Hot",variable=c,value=3,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)

        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        label=Label(top,text="What kind of Government do you prefer?", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.pack(anchor=W, fill=BOTH, expand=True)


        Radiobutton(top,text="Democracy",variable=g,value=1,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)

        Radiobutton(top,text="Communist",variable=g,value=2,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)

        Radiobutton(top,text="Monarchy",variable=g,value=3,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)

        Radiobutton(top,text="Republic",variable=g,value=4,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)

        Radiobutton(top,text="Federal",variable=g,value=5,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)



        label=Label(top,text="What is your religion?", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="Christianity",variable=r,value=1,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)

        Radiobutton(top,text="Buddhism",variable=r,value=2,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)

        Radiobutton(top,text="Hinduism",variable=r,value=3,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)

        Radiobutton(top,text="Islam",variable=r,value=4,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)

        Radiobutton(top,text="Atheist",variable=r,value=5,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        button1 = Button(top,text='NEXT', font=70, padx=10, pady=10, command=  root.destroy , fg='red', bg='#fac370')
        button1.pack(anchor=W, fill=BOTH, expand=True)


        root.mainloop()

        self.declare(LiveSuggestionActivation(climate=getClimate(c.get()),government=getGov(g.get()),religion=getReligion(r.get())))

    @Rule(TourismType(2))
    def work_suggestion(self):
        
        root = Tk()
        root.withdraw()

        top=tk.Toplevel(root)
        top.geometry("1200x488")
        res = IntVar()
        res.set(1)


        label=Label(top,text="What is your work preference?", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.pack(anchor=W, fill=BOTH, expand=True)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)


        Radiobutton(top,text="Bussiness",variable=res,value=1,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="Job",variable=res,value=2,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        button1 = Button(top,text='NEXT', font=70, padx=10, pady=10, command=  root.destroy , fg='red', bg='#fac370')
        button1.pack(anchor=W, fill=BOTH, expand=True)

        root.mainloop()
        x = getWorkType(res.get())
        self.declare(WorkType(x))

    @Rule(WorkType("bussiness"))
    def bussiness_suggestion(self):
        type1=2
        root = Tk()
        root.withdraw()

        top=tk.Toplevel(root)
        top.geometry("1200x488")
        res = IntVar()
        res.set(1)

        f = IntVar()
        f.set(1)


        label=Label(top,text="Choose the type of trade:", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.pack(anchor=W, fill=BOTH, expand=True)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)


        Radiobutton(top,text="Import",variable=res,value=1,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="Export",variable=res,value=2,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        label=Label(top,text="Your field:", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.pack(anchor=W, fill=BOTH, expand=True)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)


        Radiobutton(top,text="Technology",variable=f,value=1,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="Manufacturing",variable=f,value=2,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="Tourism",variable=f,value=3,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="Infrastructure",variable=f,value=4,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)


        button1 = Button(top,text='NEXT', font=70, padx=10, pady=10, command=  root.destroy , fg='red', bg='#fac370')
        button1.pack(anchor=W, fill=BOTH, expand=True)

        root.mainloop()

        xa = getImpExp(res.get())
        self.declare(BussSuggestionActivation(importexport=xa,worktype=getField(f.get())))


    @Rule(WorkType("job"))
    def job_suggestion(self):
        type1=3
        root = Tk()
        root.withdraw()

        top=tk.Toplevel(root)
        top.geometry("1200x488")
        f = IntVar()
        f.set(1)

        label=Label(top,text="Your field:", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.pack(anchor=W, fill=BOTH, expand=True)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)


        Radiobutton(top,text="Technology",variable=f,value=1,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="Manufacturing",variable=f,value=2,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="Tourism",variable=f,value=3,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

        Radiobutton(top,text="Infrastructure",variable=f,value=4,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)




        button1 = Button(top,text='NEXT', font=70, padx=10, pady=10, command=  root.destroy , fg='red', bg='#fac370')
        button1.pack(anchor=W, fill=BOTH, expand=True)

        root.mainloop()
        self.declare(JobSuggestionActivation(worktype=getField(f.get())))


    @Rule(
        TourismSuggestionActivation(
            budget=MATCH.b,
            placeType=MATCH.p),
        TourismSuggestion(
            budget=MATCH.b,
            placeType=MATCH.p,
            namep=MATCH.n,
            country=MATCH.c))
    def print_res(self,b,p,n,c):
        global result,type1
        result.append(n)
        type1=0
        

    @Rule(
        LiveSuggestionActivation(
            climate=MATCH.cl,
            government=MATCH.g,
            religion=MATCH.r),
        LiveSuggestion(
            climate=MATCH.cl,
            government=MATCH.g,
            religion=MATCH.r,
            country=MATCH.c))
    def print_res2(self,cl,g,r,c):
        global result,type1
        result.append(c)
        type1=1

    @Rule(
        BussSuggestionActivation(
            importexport=MATCH.i,
            worktype=MATCH.w),
        BussSuggestion(
            importexport=MATCH.i,
            worktype=MATCH.w,
            country=MATCH.c))
    def print_res3(self,i,w,c):
        global result, type1
        result.append(c)
        type1=2

    @Rule(
        JobSuggestionActivation(
            worktype=MATCH.w),
        JobSuggestion(
            worktype=MATCH.w,
            country=MATCH.c))
    def print_res4(self,w,c):
        global result, type1
        result.append(c)
        type1=3 



if __name__ == '__main__':


    tourism = getTourism()
    countryDetails = getCountryDetails()
    engine=Engine()
    engine.reset()

    engine.run()
    if type1 == 0:
        showResultForTourism(result,tourism)
    elif type1 == 1:
        showResultForLive(result,countryDetails)
    elif type1 ==2 :
        showResultForBuss(result,countryDetails)
    else:
        showResultForJob(result,countryDetails)
    print(result)



