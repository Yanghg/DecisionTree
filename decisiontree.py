class TreeNode:
    def __init__(self,examples,parent):
        self.children = []
        name, splitRules = bestAttribute(examples)
        self.rules = splitRules
        self.name = name
        self.parent = parent

        for x in splitRules: 
            subExamples = getSubExamples(x,examples)
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