"""
Clarissa Phillips                                                 October 2017
The question class of my Trivia Game.
                                                                           """
from graphics import *

class Question(object):
    """ Class of methods for question object in my Trivia Game. """

    def __init__(self, win, question, answer, hint):
        """Constructor for question class"""

        w = win.getWidth()
        h = win.getHeight()
        question = question + "?"
        self.win = win
        qPoint = Point(w/2,h/2)
        textObj = Text(qPoint, question)
        textObj.setSize(14)
        self.question = question
        self.answer = answer
        textObj.draw(win)
        self.textObj = textObj
        hPoint = Point(w/2, h*.7)
        hintMessage = "Hint: " + hint
        hint = Text(hPoint,hintMessage)
        self.hint = hint
        return

    def checkInput(self, ans):
        """ Method to check to see if user's answer is correct.
        Returns True if correct and False if incorrect. """

        ans = ans.lower()
        if ans == self.answer:
            return True
        else:
            return False

    def displayHint(self):
        """ Method that displays the hint when prompted. """
        self.hint.draw(self.win)
        return

    def unDisplayHint(self):
        """ Method that displays the hint when prompted. """
        self.hint.undraw()
        return

    def undraw(self):
        """ Method to undraw question object from graphic window. """
        self.textObj.undraw()
        return

################################################################################

def main():

    w = 400
    h = w
    win = GraphWin("Trivia Game", w, h)
    prompt = Text(Point(w/2,25), "Welcome to my Trivia Game!")
    prompt.setSize(20)
    prompt.draw(win)
    win.getMouse()
    prompt.setText("Answer this question:")
    text = "hello"
    ans = "hey"
    hint = "Casual response..."
    question1 = Question(win, text, ans, hint)
    ePoint = Point(w*.35, h*.9)
    entryObj = Entry(ePoint, 30)
    entryObj.draw(win)

    # Create "Submit" button
    sP1 = Point(w*.65,(h*.9)-10)
    sP2 = Point((w*.65)+50, (h*.9)+10)
    submitBt = Rectangle(sP1, sP2)
    submitBt.setFill("gray")
    sBtCenter = submitBt.getCenter()
    sBtText = Text(sBtCenter,"Submit")
    submitBt.draw(win)
    sBtText.draw(win)

    # Create "Hint" button
    hintBt = submitBt.clone()
    hintBt.move(60,0)
    hBtCenter = hintBt.getCenter()
    hBtText = Text(hBtCenter,"Hint")
    hintBt.draw(win)
    hBtText.draw(win)

    usrInput = ""
    correct = None
    while True:
        click = win.getMouse()
        if (w*.65) <= click.getX() <= ((w*.65)+50):
            if ((h*.9)-10) <= click.getY() <= ((h*.9)+10):
                usrInput = entryObj.getText()
                correct = question1.checkInput(usrInput)
                if correct == True:
                    break
        elif (w*.65)+60 <= click.getX() <= ((w*.65)+110):
            if ((h*.9)-10) <= click.getY() <= ((h*.9)+10):
                question1.displayHint()
                hintBt.undraw()
                hBtText.undraw()

    win.getMouse()

#main()
