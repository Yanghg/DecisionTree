import csv

class TreeNode:
    def __init__(self, examples):
        self.name = ""
        self.children = []
        name, splitRules = bestAttribute(examples)
        self.name = name
        for x in splitRules: 
            subExamples = getSubExamples(x)
            subtree = Node(subExamples)
            self.children.append(subtree)
    
    def bestAttribute(self, examples):
        for examples
        return "hehe", []

    def getSubExamples(self, examples):
        return 
    def handleAttribute(self, examples, name):
        return 

def readFile(fileName):
    # "rb" is read only
    csvReader = csv.reader(open(fileName,"rb"),delimiter=',') 
    return list(csvReader)