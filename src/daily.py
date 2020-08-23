from tkinter import *
from datetime import date
import json

# Add sleep times
labels_S = []
entries_S = []

today = date.today()

root=Tk()

topText=Frame(root)
topText.pack()

top=Frame(root, pady=3)
top.pack()
middle=Frame(root, pady=3)
middle.pack()
bottom=Frame(root, pady=3)
bottom.pack()


def main():
    root.title("Daily Practice - " + today.strftime("%B %d, %Y"))
    
    streaks()
    gratitude()

    B = Button(bottom, text ="Save", command = updateStreaks)
    B.pack()
    # Width, height in pixels
    mainloop()

def streaks():
    greeting = Label(topText, text="Streaks", font=("Arial", 16))
    greeting.pack()
    readStreaks()

def readStreaks():
    with open("../streaks/streaks.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        
        i = 0
        for k,v in data.items():
            labels_S.append(Label(top, text=k, font=("Arial",12)))
            labels_S[i].grid(row = i)

            entries_S.append(Entry(top))
            entries_S[i].grid(row=i, column=1)
            entries_S[i].insert(0, v)
            
            i = i + 1

def gratitude():
    greeting2 = Label(middle, text="Gratitude", font=("Arial", 16)).grid(row = 0)
    text_box1 = Text(middle, height=5).grid(row = 1)
    text_box2 = Text(middle).grid(row = 2)
    text_box3 = Text(middle).grid(row = 3)

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