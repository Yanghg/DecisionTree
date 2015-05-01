import math

class TreeNode:
    def __init__(self,examples,parent,minExampleNum=1):
        self.children = []
        name, splitRules = self.bestAttribute(examples)
        self.rules = splitRules
        self.labelName = name
        self.parent = parent

        #set the minimum height of an example set
        if parent:
            self.minExampleNum = parent.minExampleNum
        else:
            self.minExampleNum = minExampleNum

        if self.examples1stCheck(examples):

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
        examplesData = examples[3:]
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

    def examples1stCheck(self,examples):
        visitedList = examples[2]
        indexList = []
        for i in range(len(visitedList)):
            if visitedList[i]:
                indexList.append(i)
        if len(indexList) == 0:
            return False
        if len(examples) <= self.minExampleNum+3:
            return False
        width = len(examples[3])
        zeroNum = 0
        oneNum = 0
        for i in range(3,len(examples)):
            zeroNum += (1-examples[i][width-1])
            oneNum += examples[i][width-1]
        if zeroNum * oneNum == 0:
            return False
        return True 


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





