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
        maxGain = 
        
        for x in examples[0]:
            gain, rule = handleAttribute(examples, x)

        return "hehe", rule

    def getSubExamples(self, examples):
        return 

def handleAttribute(examples, name):
        return 

def readFile(fileName):
    # "rb" is read only
    csvReader = csv.reader(open(fileName,"rb"),delimiter=',') 
    return list(csvReader)