from reportlab.pdfgen.canvas import Canvas
from tkinter import *
from datetime import date
import json

# Add sleep times
labels_S = []
entries_S = []
text_G = []
planningContent = []

today = date.today()

root=Tk()

STARTFRAME = Frame(root)
STARTFRAME.pack()
planningF = Frame(root)
planningF.pack()

ENDFRAME = Frame(root)
ENDFRAME.pack()
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
    
    #START OF DAY
    START = Label(STARTFRAME, width=40, text="START OF DAY", font=("Arial", 22))
    START.pack()
    planning()

    #END OF DAY
    END = Label(ENDFRAME, width=40, text="END OF DAY", font=("Arial", 22))
    END.pack()
    introduction()
    streaks()
    
    gratitude()

    B = Button(bottom, text ="Save", command = update)
    B.pack()
    C = Button(bottom, text ="Generate PDF", command = test_template)
    C.pack()
    # Width, height in pixels
    mainloop()

def planning():
    with open("C:/Users/Wouter Kok/Documents/self-improj/data/planning.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        planningLabel = Label(planningF, width=40, text="PLANNING", font=("Arial", 16))
        planningLabel.pack()
        planningText = Text(planningF, width=100, height=4)
        

        planningText.insert(INSERT, data['planning'])
        planningContent.insert(0, planningText)
        planningText.pack()


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
    with open("C:/Users/Wouter Kok/Documents/self-improj/data/streaks.json", "r+") as jsonFile:
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
        text_G.append(Text(middle, width=100, height=3))
        text_G[i].grid(row = i + 1)

    
def update():
    updateStreaks()
    updatePlanning()
    createTxt()

def createTxt():
    print("aa")

def updateStreaks():
    with open("../data/streaks.json", "r+") as jsonFile:
        data = json.load(jsonFile)

    i = 0

    for k,v in data.items():
        data[k] = entries_S[i].get()
        i = i + 1

    with open("../data/streaks.json", "w") as jsonFile:
        json.dump(data, jsonFile)

def updatePlanning():
    with open("../data/planning.json", "r+") as jsonFile:
        data = json.load(jsonFile)

    print(planningContent[0].get(1.0,END))
    data['planning'] = planningContent[0].get(1.0, END)

    with open("../data/planning.json", "w") as jsonFile:
        json.dump(data, jsonFile)

def test_template():
    writer = PdfWriter()

    writer.write('../results/2.pdf')

main()