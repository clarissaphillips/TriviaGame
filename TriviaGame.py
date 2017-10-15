""" Clarissa Phillips                                              October 2017
    My Trivia Game.                                                         """

from graphics import *
from question import *
from data import *
import requests
import json
from urllib.request import *
from urllib.error import *

def main():

    w = 800
    h = w
    win = GraphWin("Trivia Game", w, h)
    prompt = Text(Point(w/2,h/2), "Welcome to my Trivia Game!")
    prompt.setSize(20)
    prompt.draw(win)
    win.getMouse()
    prompt.undraw()
    prompt.move(0,-375)

    # Trivia data provided by https://opentdb.com/
    url = "https://opentdb.com/api.php?amount=50&type=boolean"
    data = json.load(urlopen(url))
    data = Data(data)


    # initialize game question values
    textList = data.retTextList()
    ansList = data.retAnsList()
    diffList = data.retDiffList()

    # Create "Submit" button
    sP1 = Point(w*.65,(h*.9)-10)
    sP2 = Point((w*.65)+50, (h*.9)+10)
    submitBt = Rectangle(sP1, sP2)
    submitBt.setFill("gray")
    sBtCenter = submitBt.getCenter()
    sBtText = Text(sBtCenter,"Submit")

    # Create "difficulty" button
    diffBt = submitBt.clone()
    diffBt.move(60,0)
    dBtCenter = diffBt.getCenter()
    dBtText = Text(dBtCenter,"Diff.")

    # Create "wrong" prompt
    wrongPt = submitBt.getCenter()
    wrongPt.move(0,-25)
    wrongText = Text(wrongPt, "Wrong :(")
    wrongText.setTextColor("red")

    # Create entry object
    ePoint = Point(w*.35, h*.9)
    entryObj = Entry(ePoint, 30)

    #create score counter
    numCorrect = 0
    scorePoint = dBtCenter
    scorePoint.move(70,0)
    score = Text(scorePoint, ("Score: " + str(numCorrect)))

    prompt.draw(win)    
    diffBt.draw(win)
    dBtText.draw(win)
    entryObj.draw(win)
    submitBt.draw(win)
    sBtText.draw(win)
    score.draw(win)

    for i in range(len(textList)):
        key = str(i)
        question = Question(win, textList[key], ansList[key], diffList[key])
        prompt.setText("True or False")
        usrInput = ""
        correct = None
        while True:
            click = win.getMouse()
            if (w*.65) <= click.getX() <= ((w*.65)+50): # User hits "submit"
                if ((h*.9)-10) <= click.getY() <= ((h*.9)+10):
                    usrInput = entryObj.getText()
                    correct = question.checkInput(usrInput)
                    if correct == True:
                        prompt.setText("Correct!")
                        question.unDisplayDiff()
                        numCorrect = numCorrect + 1
                        score.setText("Score: " + str(numCorrect))
                        break
                    else:
                        wrongText.draw(win)
                        break
            elif (w*.65)+60 <= click.getX() <= ((w*.65)+110): #User hits "diff"
                if ((h*.9)-10) <= click.getY() <= ((h*.9)+10):
                    question.unDisplayDiff()
                    question.displayDiff()
                    diffBt.undraw()
                    dBtText.undraw()

        # avoid draw errors/create "next" button
        diffBt.undraw()
        dBtText.undraw()
        dBtText.setText("Next")
        diffBt.draw(win)
        dBtText.draw(win)
        while True:
            click = win.getMouse()
            if (w*.65)+60 <= click.getX() <= ((w*.65)+110):
                if ((h*.9)-10) <= click.getY() <= ((h*.9)+10):
                    dBtText.setText("Diff")
                    question.undraw()
                    entryObj.setText("")
                    wrongText.undraw()
                    break

    prompt.setText("Nice work! Click anywhere to exit.")
    win.getMouse()

main()
