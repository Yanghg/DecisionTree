import csv

class TreeNode:
    def __init__(self, examples, name="NULL", children=[]):
        self.name = name
        self.children = children


def readFile(fileName):
    # "rb" is read only
    csvReader = csv.reader(open(fileName,"rb"),delimiter=',') 
    return list(csvReader)