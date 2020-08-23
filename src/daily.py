from tkinter import *
from datetime import date
import json

# Add sleep times
labels_S = []
entries_S = []
text_G = []

today = date.today()

root=Tk()


top=Frame(root)
top.pack()

intro=Frame(top, pady=3)
intro.pack(side=LEFT)
introTop=Frame(intro)
introTop.pack(side=TOP)
introText=Frame(intro)
introText.pack()

streaks_F=Frame(top, pady=3)
streaks_F.pack(side=RIGHT)
streaksText=Frame(streaks_F)
streaksText.pack(side=TOP)
streaksList = Frame(streaks_F)
streaksList.pack()


middle=Frame(root, pady=3)
middle.pack()
bottom=Frame(root, pady=3)
bottom.pack()


def main():
    root.title("Daily Practice - " + today.strftime("%B %d, %Y"))
    
    introduction()
    streaks()
    
    gratitude()

    B = Button(bottom, text ="Save", command = update)
    B.pack()
    # Width, height in pixels
    mainloop()

def introduction():
    greeting = Label(introTop, width=40, text="EXTRA INFO", font=("Arial", 16))
    greeting.pack()
    
    strin =  """-- SLEEP SCHEDULE : 6:00 OUT - 21:30 IN -- 
                ...
                ...
                ..."""  
    moreInfo = Label(introText, text=strin, font = ("Arial", 12))
    moreInfo.pack()


def streaks():
    greeting = Label(streaksText, width=40, text="STREAKS", font=("Arial", 16))
    greeting.pack(side=RIGHT)
    readStreaks()

def readStreaks():
    with open("C:/Users/Wouter Kok/Documents/self-improj/streaks/streaks.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        
        i = 0
        for k,v in data.items():
            labels_S.append(Label(streaksList, text=k, font=("Arial",12)))
            labels_S[i].grid(row = i)

            entries_S.append(Entry(streaksList))
            entries_S[i].grid(row=i, column=1)
            entries_S[i].insert(0, v)
            
            i = i + 1

def gratitude():
    Label(middle, text="GRATITUDE & ACCEPTANCE", font=("Arial", 16)).grid(row = 0)
    for i in range(3):
        text_G.append(Text(middle, width=100, height=2))
        text_G[i].grid(row = i + 1)

    
def update():
    updateStreaks()
    createTxt()

def createTxt():
    print("aa")

def updateStreaks():
    with open("../streaks/streaks.json", "r+") as jsonFile:
        data = json.load(jsonFile)

    i = 0

    for k,v in data.items():
        data[k] = entries_S[i].get()
        i = i + 1

    with open("../streaks/streaks.json", "w") as jsonFile:
        json.dump(data, jsonFile)

main()