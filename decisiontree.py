import csv

class TreeNode:
    def __init__(self, examples):
        self.name = ""
        self.children = []
        self.rules = []
        name, splitRules = bestAttribute(examples)
        self.rules = splitRules
        self.name = name
        for x in splitRules: 
            subExamples = getSubExamples(x)
            child = Node(subExamples)
            self.children.append(child)
    
    def bestAttribute(self, examples):
        maxGain = 0
        maxRule = ""
        name = ""
        for x in examples[0]:
            gain, rule = handleAttribute(examples, x)
            if gain > maxGain:
                maxGain = gain
                maxRule = rule
                name = x
        return x, rule

    def getSubExamples(self, examples):
        return subExamples

def handleAttribute(examples, name):
        return gain, rule

def readFile(fileName):
    # "rb" is read only
    csvReader = csv.reader(open(fileName,"rb"),delimiter=',') 
    return list(csvReader)