import math

class TreeNode:
    def __init__(self,examples,parent,minExampleNum=1):
        self.children = []
        self.rules = []
        self.name = ""
        self.parent = parent

        #set the minimum height of an example set
        if parent:
            self.minExampleNum = parent.minExampleNum
        else:
            self.minExampleNum = minExampleNum

        #first check the examples using rule 1,2 and 3
        if self.examples1stCheck(examples):
            self.name, self.rules = self.bestAttribute(examples)
            if self.name!="Good" or self.name!="Bad":
                for rule in self.rules: 
                    subExample = self.getSubExample(rule,examples)
                    child = TreeNode(subExample,this)
                    self.children.append(child)
    
    def bestAttribute(self, examples):
        #information gain always larger than 0, set boundary to be 0
        maxGain = 0
        bestRule = []
        bestName = "" 
        attributes = examples[0][:-1]

        #calculate outcome gain
        classEntropy = self.calculateEntropy(examples[3:])
    
        #get attribute with largest information gain
        for at in range(len(attributes)):
            if examples[2][at] != True:
                gain, rule = self.handleAttribute(examples, at, classEntropy)
                if gain == -10:
                    return self.name, []
                if gain > maxGain:
                    maxGain = gain
                    bestRule = rule
                    bestName = attributes[at]
        return bestName, bestRule

    def handleAttribute(self, examples, atIndex, classEntropy):
        attributesType = examples[1]
        used = examples[2]
        splitSet = {}
        splitRules = []
        examplesData = examples[3:]
        numTotal = len(examplesData)
        conditionalEnt = 0

        #if unused norminal attribute       
        if attributesType[atIndex] == True: 
            examples[2][atIndex] = True
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
            splitList = []
            #get attribute value range
            minVal = float("inf")
            maxVal = float("-inf") 
            for x in examplesData:
                current = x[atIndex]
                minVal = min(current, minVal)
                maxVal = max(current, maxVal)

            if minVal == maxVal:
                self.setNameByResult(examples)
                return -10, splitRules

            #partition and get gain
            else:
                partition = minVal
                increment = (maxVal - minVal)/11.0
                for i in range(10):
                    partition += increment
                    splitList.append(partition)
                informationGain = 0

                for splitPoint in splitList:
                    tempSet = {}
                    tempRules = []
                    tempSet["belowPoint"] = []
                    tempSet["abovePoint"] = []
                    tempRules.append("<" + str(splitPoint))
                    tempRules.append(">" + str(splitPoint))
                    tempConditionalEnt = 0
                    #build dictionary for different attribute value
                    for x in examplesData:
                        current = x[atIndex]
                        if current < splitPoint:
                            tempSet["belowPoint"].append(x)
                        else:
                            tempSet["abovePoint"].append(x)
                    #calculate conditional entropy
                    for key in tempSet: 
                        prob = float(len(tempSet[key])/numTotal)
                        tempConditionalEnt += prob * self.calculateEntropy(tempSet[key])
                    #calculate information gain
                    tempGain = classEntropy - tempConditionalEnt
                    if tempGain > informationGain:
                        informationGain = tempGain
                        splitRules = tempRules
        return infomationGain, splitRules


    def getSubExample(self, rule, examples):
        subExampleSet = []
        attributeIndex = examples[0].index(self.name)
        subExample = []
        subExample.append(examples[0])
        subExample.append(examples[1])
        subExample.append((examples[2])[:]) 
        sign = rule[0]
        if sign == '=':
            value = int(rule[1:])
            for dataRow in examples[3:]:
                if dataRow[attributeIndex] == value:
                    subExample.append(dataRow)
        else:
            value = float(rule[1:])
            for dataRow in examples[3:]:
                if sign == '>':
                    if dataRow[attributeIndex] >= value:
                        subExample.append(dataRow)
                else:
                    if dataRow[attributeIndex] < value:
                        subExample.append(dataRow)
        return subExample

    def examples1stCheck(self,examples):
        visitedList = examples[2]
        indexList = []
        for i in range(len(visitedList)):
            if visitedList[i]:
                indexList.append(i)
        if len(indexList) == 0:
            self.setNameByResult(examples)
            return False
        if len(examples) <= self.minExampleNum+3:
            self.setNameByResult(examples)
            return False
        width = len(examples[3])
        zeroNum = 0
        oneNum = 0
        for i in range(3,len(examples)):
            zeroNum += (1-examples[i][width-1])
            oneNum += examples[i][width-1]
        if zeroNum * oneNum == 0:
            self.setNameByResult(examples)
            return False
        return True 


    def setNameByResult(self,examples):
        oneNum = 0
        width = len(examples[3])
        for dataRow in examples[3:]:
            oneNum += dataRow[width-1]
        accuracy = float(oneNum)/(len(examples)-3)
        if accuracy>0.5:
            self.name = "Good"
        elif accuracy<0.5:
            self.name = "Bad"
        else:
            self.name = random.choice(["Good","Bad"])

    def validate(self,examples,stat):
        count=0
        if self.name=='Good':
            for i in range(0,len(examples)-3):
                if examples[i+3][-1]!=1:
                    count+=1
            stat.append(count)
        elif self.name=='bad':
            for i in range(0,len(examples)-3):
                if examples[i+3][-1]!=0:
                    count+=1
            stat.append(count)
        else:
            for i in range(0,len(self.rule)):
                sub=getSubExample(self.rule[i],examples)
                self.child[i].validate(sub,stat)





    #helper functions for TreeNode class #consider 0
    def calculateEntropy(self, dataSet):
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





