import csv
from decisiontree import TreeNode

#examples = [["aa","bb","cc"],[True,False,True],[1 2 3],[4 5 6]....[7 8 9]]


def handleAttribute(examples, name):
    return gain, rule

def readFile(fileName):
    # "rb" is read only
    csvReader = csv.reader(open(fileName,"rb"),delimiter=',') 
    return list(csvReader)

def printTree(root):
    return 

def solve(fileName):
    examples = readFile(fileName)
    root = TreeNode(examples,None)
    return root
