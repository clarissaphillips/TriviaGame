"""
Clarissa Phillips                                                  October 2017
The question class of my Trivia Game.
                                                                            """
from graphics import *

class Question(object):
    """ Class of methods for question object in my Trivia Game. """

    def __init__(self, win, question, answer, diff):
        """Constructor for question class"""

        w = win.getWidth()
        h = win.getHeight()
        self.win = win
        qPoint = Point(w/2,h/2)
        textObj = Text(qPoint, question)
        textObj.setSize(14)
        self.question = question
        self.answer = answer
        textObj.draw(win)
        self.textObj = textObj
        dPoint = Point(w/2, h*.7)
        diff = Text(dPoint, diff)
        self.diff = diff
        return

    def checkInput(self, ans):
        """ Method to check to see if user's answer is correct.
        Returns True if correct and False if incorrect. """

        ans = ans.lower()
        if ans == self.answer:
            return True
        else:
            return False

    def displayDiff(self):
        """ Method that displays the hint when prompted. """
        self.diff.draw(self.win)
        return

    def unDisplayDiff(self):
        """ Method that displays the hint when prompted. """
        self.diff.undraw()
        return

    def undraw(self):
        """ Method to undraw question object from graphic window. """
        self.textObj.undraw()
        return
