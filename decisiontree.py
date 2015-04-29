import csv

class TreeNode:
    def __init__(self, examples):
        self.name = "";
        self.children = [];
        name, rule = bestAttribute(examples)
        self.name = name
        for x in rule: 
            subExamples = getSubExamples(x)
            subtree = Node(subExamples)
            self.children.append(subtree)
    
    def bestAttribute(self, examples):

        return "hehe", []

    def getSubExamples(self, examples):

    def handleAttribute(self, examples, name):

def readFile(fileName):
    # "rb" is read only
    csvReader = csv.reader(open(fileName,"rb"),delimiter=',') 
    return list(csvReader)