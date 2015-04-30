import math

class TreeNode:
    def __init__(self,examples,parent):
        self.children = []
        name, splitRules = self.bestAttribute(examples)
        self.rules = splitRules
        self.labelName = name
        self.parent = parent

        for x in splitRules: 
            subExamples = self.getSubExamples(x,examples)
            child = TreeNode(subExamples)
            self.children.append(child)
    
    def bestAttribute(self, examples):
        #information gain always larger than 0, set boundary to be 0
        maxGain = 0
        bestRule = []
        bestName = "" 
        attributes = examples[0]

        #calculate outcome gain
        examplesData = examples[2:]
        classEntropy = calculateEntropy(examplesData)

        #get attribute with largest information gain
        for at in attributes:
            gain, rule = self.handleAttribute(examples, at, classEntropy)
            if gain > maxGain:
                maxGain = gain
                bestRule = rule
                bestName = at
        return bestName, bestRule

    def handleAttribute(self, examples, attribute, classEntropy):
        
        return gain, rule

    def getSubExamples(self, examples):
        return subExamples

#helper functions for TreeNode class
def calculateEntropy(data):
    num = len(data)
    freq={}
    entropy = 0.0

    for target in dataSet:
        current = target[-1]
     
        if not freq.has_key(current):
            freq[current] = 0       
        freq[current] += 1
  
    for key in freq:
        prob = float(freq[key])/num       
        entropy -= prob*math.log(prob,2)

    return entropy







