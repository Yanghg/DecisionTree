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
        attributes = examples[0][:-1]

        #calculate outcome gain
        classEntropy = self.calculateEntropy(examples[3:])
        if classEntropy == 0:
            # over

        #get attribute with largest information gain
        for at in range(len(attributes)):
            gain, rule = self.handleAttribute(examples, at, classEntropy)
            if gain > maxGain:
                maxGain = gain
                bestRule = rule
                bestName = attributes(at)
        return bestName, bestRule

    def handleAttribute(self, examples, atIndex, classEntropy):
        attributesType = examples[1]
        used = examples[2]
        splitSet = {}
        splitRules = []
        examplesData = examples[3:]
        numTotal = len(examplesData)
        #if unused norminal attribute
        conditionalEnt = 0;
        if attributesType[atIndex] == True and used[atIndex] == False: 
            used[atIndex] = True
            #build dictionary for different attribute value
            for x in examplesData:
                    current = x[atIndex]
                    if not splitSet.has_key(current):
                        splitSet[current] = []
                        splitRules.append("=" + str(current))
                    splitSet[current].append(x)
            #calculate conditional entropy
            for key in splitSet: 
                prob = float(len(splitSet[key])/numTotal)
                conditionalEnt += prob * self.calculateEntropy(splitSet[key])
            #calculate information gain
            infomationGain = classEntropy - conditionalEnt

        #if numeric attribute
        elif attributesType[atIndex] == False:


        return infomationGain, splitRules


    def getSubExamples(self, examples):
        return subExamples


    #helper functions for TreeNode class #consider 0
    def calculateEntropy(dataSet):
        num = len(dataSet)
        freq={}
        entropy = 0.0

        for target in dataSet:
            current = target[-1]
         
            if not freq.has_key(current):
                freq[current] = 0       
            freq[current] += 1
      
        for key in freq:
            prob = float(freq[key])/num
            if prob != 0:                   
                entropy -= prob*math.log(prob,2)
        return entropy





