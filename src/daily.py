from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from tkinter import *
from datetime import date
import json

# Add sleep times
labels_S = []
entries_S = []
text_G = []
text_F = []
planningContent = []

todaysDate = date.today()
todaysDateFormatted = todaysDate.strftime("%B %d, %Y")

root=Tk()
default_font = "Verdana"
root.option_add("*Font", default_font)
root.geometry("1400x1000")
root.option_add("*Button.Background", "ghost white")
root.option_add("*Button.Foreground", "grey7")
root.option_add("*Text.Background", "ghost white")
root.option_add("*Text.Foreground", "black")
root.tk_setPalette(background='grey7', foreground="ghost white", activeBackground='ghost white')
# , foreground='black', activeBackground='black', activeForeground='grey7')

planningF = Frame(root)
planningF.pack()

feelingsF=Frame(root)
feelingsF.pack()

middle=Frame(root)
middle.pack()

top=Frame(root)
top.pack()

intro=Frame(top)
intro.pack(side=LEFT)
introTop=Frame(intro)
introTop.pack(side=TOP)
introText=Frame(intro)
introText.pack()

streaks_F=Frame(top)
streaks_F.pack(side=RIGHT)
streaksText=Frame(streaks_F)
streaksText.pack(side=TOP)
streaksList = Frame(streaks_F)
streaksList.pack()


bottom=Frame(root)
bottom.pack()


def main():
    root.title("Daily Practice - " + todaysDateFormatted)

    planning()


    introduction()
    streaks()

    gratitude()
    feelings()

    B = Button(bottom, text ="Save", command = update)
    B.pack()
    C = Button(bottom, text ="Generate PDF", command = test_template)
    C.pack()
    # Width, height in pixels
    mainloop()

def planning():
    with open("C:/Users/Wouter Kok/Documents/self-improj/data/planning.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        planningLabel = Label(planningF, width=40, text="LIST OF TODOS & LEARNINGS", font=(default_font, 16))
        planningLabel.pack()
        planningText = Text(planningF, width=100, height=8)

        planningText.config(padx = 15, pady = 15)

        planningText.insert(INSERT, data['planning'])
        planningContent.insert(0, planningText)
        planningText.pack()


def introduction():
    greeting = Label(introTop, width=40, text="ROUTINE", font=(default_font, 16))
    greeting.pack()

    strin =  """SLEEP SCHEDULE : 6:00 OUT - 21:30 IN
                INTERMITTEND FASTING: BETWEEN 19:00 and 11:00
                ...
                ..."""
    moreInfo = Label(introText, text=strin, font = (default_font, 12))
    moreInfo.pack()


def streaks():
    greeting = Label(streaksText, width=40, text="STREAKS", font=(default_font, 16))
    greeting.pack(side=RIGHT)
    readStreaks()

def readStreaks():
    with open("C:/Users/Wouter Kok/Documents/self-improj/data/streaks.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        i = 0
        for k,v in data.items():
            labels_S.append(Label(streaksList, text=k, font=(default_font,12)))
            labels_S[i].grid(row = i)
            entries_S.append(Entry(streaksList, justify='center'))
            entries_S[i].grid(row=i, column=1)
            entries_S[i].insert(0, v)

            i = i + 1

def feelings():
    Label(feelingsF, text="FEELINGS", font=(default_font, 16)).grid(row = 0)
    feelingsText = Text(feelingsF, width=100, height=1.5)
    feelingsText.config(padx = 15, pady = 15)
    text_F.append(feelingsText)
    text_F[0].grid(row = 1)


def gratitude():
    Label(middle, text="GRATITUDE & ACCEPTANCE", font=(default_font, 16)).grid(row = 0)
    for i in range(3):
        newText = Text(middle, width=100, height=1.5)
        newText.config(padx = 15, pady = 15)
        text_G.append(newText)
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

    data['planning'] = planningContent[0].get(1.0, END)

    with open("../data/planning.json", "w") as jsonFile:
        json.dump(data, jsonFile)

def test_template():
    pdfName = '../results/' + todaysDateFormatted + '.pdf'
    my_doc = SimpleDocTemplate(pdfName)
    sample_style_sheet = getSampleStyleSheet()
    flowables = []

    spaces = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
    paragraph_1_text = '```Day 2: The day of ' + todaysDateFormatted + '```<br />'
    paragraph_1 = Paragraph(spaces + paragraph_1_text.upper(), sample_style_sheet['Heading1'])

    paragraph_2 = Paragraph("\n\n**List of Todos & Learnings**", sample_style_sheet['Heading2'])

    paragraph_3_text = planningContent[0].get(1.0, END).replace(' ', '&nbsp;')
    paragraph_3_text = paragraph_3_text.replace('\n','<br />\n')
    paragraph_3 = Paragraph(paragraph_3_text, sample_style_sheet['BodyText'])

    paragraph_8 = Paragraph("\n\n**Feelings**", sample_style_sheet['Heading2'])
    paragraph_9 = Paragraph(text_F[0].get(1.0, END))


    paragraph_4 = Paragraph("**Gratitude & Acceptance**", sample_style_sheet['Heading2'])

    temp = ""
    for i in range(3):
        temp = temp + " - " + text_G[i].get(1.0, END) + "\n"

    paragraph_5 = Paragraph(temp.replace('\n','<br />\n'), sample_style_sheet['BodyText'])

    paragraph_6 = Paragraph("**Streaks**", sample_style_sheet['Heading2'])

    temp = ""

    for i in range(len(entries_S)):
        temp = temp + labels_S[i]['text'] + ":  " + entries_S[i].get() + "\n"

    paragraph_7 = Paragraph(temp.replace('\n','<br />\n'), sample_style_sheet['BodyText'])

    flowables.extend([paragraph_1, paragraph_2, paragraph_3, paragraph_8, paragraph_9, paragraph_4, paragraph_5, paragraph_6, paragraph_7])
    my_doc.build(flowables)


main()