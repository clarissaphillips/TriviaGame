"""
    Clarissa Phillips                                              October 2017
    My Trivia Game.
                                                                            """
from graphics import *
from question import *

def main():

    w = 400
    h = w
    win = GraphWin("Trivia Game", w, h)
    prompt = Text(Point(w/2,25), "Welcome to my Trivia Game!")
    prompt.setSize(20)
    prompt.draw(win)
    win.getMouse()

    # initialize game question values
    textList = ["What color is the sun", "What programing language is this",
                "What college is in Swarthmore, PA, USA"]
    ansList = ["yellow", "python", "swarthmore college"]
    hintList = ["Lemons are also...", "Its an OO language!", "Also called Swat!"]

    # Create "Submit" button
    sP1 = Point(w*.65,(h*.9)-10)
    sP2 = Point((w*.65)+50, (h*.9)+10)
    submitBt = Rectangle(sP1, sP2)
    submitBt.setFill("gray")
    sBtCenter = submitBt.getCenter()
    sBtText = Text(sBtCenter,"Submit")

    # Create "Hint" button
    hintBt = submitBt.clone()
    hintBt.move(60,0)
    hBtCenter = hintBt.getCenter()
    hBtText = Text(hBtCenter,"Hint")

    # Create "wrong" prompt
    wrongPt = submitBt.getCenter()
    wrongPt.move(0,-25)
    wrongText = Text(wrongPt, "Wrong :(")
    wrongText.setTextColor("red")

    # Create entry object
    ePoint = Point(w*.35, h*.9)
    entryObj = Entry(ePoint, 30)

    hintBt.draw(win)
    hBtText.draw(win)
    entryObj.draw(win)
    submitBt.draw(win)
    sBtText.draw(win)

    for i in range(len(textList)):
        question = Question(win, textList[i], ansList[i], hintList[i])
        prompt.setText("Answer this question:")
        usrInput = ""
        correct = None
        while True:
            click = win.getMouse()
            wrongText.undraw()
            if (w*.65) <= click.getX() <= ((w*.65)+50): # User hits "submit"
                if ((h*.9)-10) <= click.getY() <= ((h*.9)+10):
                    usrInput = entryObj.getText()
                    correct = question.checkInput(usrInput)
                    if correct == True:
                        prompt.setText("Correct!")
                        question.unDisplayHint()
                        break
                    else:
                        wrongText.draw(win)
            elif (w*.65)+60 <= click.getX() <= ((w*.65)+110): #User hits "hint"
                if ((h*.9)-10) <= click.getY() <= ((h*.9)+10):
                    question.unDisplayHint()
                    question.displayHint()
                    hintBt.undraw()
                    hBtText.undraw()

        # avoid draw errors/create "next" button
        hintBt.undraw()
        hBtText.undraw()
        hBtText.setText("Next")
        hintBt.draw(win)
        hBtText.draw(win)
        while True:
            click = win.getMouse()
            if (w*.65)+60 <= click.getX() <= ((w*.65)+110):
                if ((h*.9)-10) <= click.getY() <= ((h*.9)+10):
                    hBtText.setText("Hint")
                    question.undraw()
                    entryObj.setText("")
                    break

    prompt.setText("Nice work! Click anywhere to exit.")
    win.getMouse()

main()
