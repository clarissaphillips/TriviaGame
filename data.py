"""
Clarissa Phillips                                                  October 2017
The data class of my Trivia Game.
                                                                            """
import requests
import json
from urllib.request import *
from urllib.error import *

class Data(object):
    """ Class of methods for data dictionary in my Trivia Game. """

    def __init__(self, data):
        """Constructor for data dictionary"""

        data = data['results']
        textList = {}
        ansList = {}
        diffList = {}
        for i in range(len(data)):
            key = str(i)
            if "&" in data[i]['question']:
                pass
            else:
                textList[key] = data[i]['question']
                ansList[key] = data[i]['correct_answer'].lower()
                diffList[key] = data[i]['difficulty']

        self.textList = textList
        self.ansList = ansList
        self.diffList = diffList
        self.data = data
        return

    def Data(self):
        return self.data

    def retTextList(self):
        return self.textList

    def retAnsList(self):
        return self.ansList

    def retDiffList(self):
        return self.diffList

################################################################################

def main():

    url = "https://opentdb.com/api.php?amount=25&type=boolean"
    data = json.load(urlopen(url))
    data = data['results']
    textList = {}
    ansList = {}
    diffList = {}
    print(data[0]['category'])
    for i in range(len(data)):
        key = str(i)
        textList[key] = data[i]['question']
        ansList[key] = data[i]['correct_answer']
        diffList[key] = data[i]['difficulty']
    print(textList)
    print(ansList)
    print(diffList)



#main()
