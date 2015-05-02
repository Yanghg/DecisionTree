#-*- coding: UTF-8 -*-
import sys
import csv
from xml.etree import ElementTree
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment
import xml.etree.cElementTree as ET
from decisiontree import TreeNode

#examples = [["aa","bb","cc"],[True,False,True],[False,True,False],[1 2 3],[4 5 6]....[7 8 9]]

#This function is to read data set from file
def readFile(fileName,type,portion):  #portions means how much we want to devide the set. type zero means training set or validation set. type one means testing set.
    # "rb" is read only
    csvReader = csv.reader(open(fileName,"rb"),delimiter=',') 
    data = list(csvReader)
    tlength=len(data)
    dlength= len(data[0])
    plength= int(tlength*portion)
    data = data[:tlength]
    examples=[]
    if type==0:
        Dis_Cons = []
        alignpos =[] 
        serialpos=[]# continuous variable
        mostcfW= [] #Common num for win
        mostcfL= [] #Common num for win
        ave4W= []
        ave4L= []
        mostSfW=[] #continous num average
        mostSfL=[] #continous num average
        mapsW=[]#dict for win side
        mapsL=[]#dict for lose side
        delation=[]
        # find value type: discrete or continuous
        examples.append([])
        for i in range(0,dlength):
            if i ==0:
                examples[0].append(data[0][0][:])
            else:
                examples[0].append(data[0][i][1:])
            temp=data[1][i]
            mapsL.append({})
            mapsW.append({})
            mostcfW.append([-1])
            mostcfL.append([-1])
            ave4W.append([])
            ave4L.append([])
            mostSfW.append(0) 
            mostSfL.append(0)
            if temp!= '?':
                if temp.find('.')!=-1:
                    Dis_Cons.append(False)
                else:
                    Dis_Cons.append(True)
            else:
                temp=data[2][i]
                if temp!= '?':
                    if temp.find('.')!=-1:
                        Dis_Cons.append(False)
                    else:
                        Dis_Cons.append(True)
        examples.append(Dis_Cons[:])
        del examples[1][dlength-1]
        examples.append([])
        for i in range(0,dlength-1):
            examples[2].append(False)
        # Turn str to int or float
        for i in range(1,plength):
            examples.append([])
            for j in range(0,dlength):
                if data[i][j]!='?':
                    if Dis_Cons[j]==True:
                        examples[i+2].append(int(data[i][j]))
                        if data[i][dlength-1].find('1')!=-1:
                            if mapsW[j].has_key(examples[i+2][j])==True:
                                mapsW[j][examples[i+2][j]]+=1
                            else:
                                mapsW[j][examples[i+2][j]]=1
                            if mostcfW[j][0]<mapsW[j][examples[i+2][j]] :
                                if len(mostcfW[j])==1:
                                    mostcfW[j].append(examples[i+2][j])
                                else:
                                    mostcfW[j][0]=mapsW[j][examples[i+2][j]]
                                    mostcfW[j][1]=examples[i+2][j]
                        else:
                            if mapsL[j].has_key(examples[i+2][j])==True:
                                mapsL[j][examples[i+2][j]]+=1
                            else:
                                mapsL[j][examples[i+2][j]]=1
                            if mostcfL[j][0]<mapsL[j][examples[i+2][j]] :
                                if len(mostcfL[j])==1:
                                    mostcfL[j].append(examples[i+2][j])
                                else:
                                    mostcfL[j][0]=mapsL[j][examples[i+2][j]]
                                    mostcfL[j][1]=examples[i+2][j]
                    else:
                        examples[i+2].append(float(data[i][j]))
                        if data[i][dlength-1].find('1')!=-1:
                            ave4W[j].append(examples[i+2][j])
                            mostSfW[j]=(mostSfW[j]*(len(ave4W[j])-1)+ave4W[j][-1])/len(ave4W[j])
        
                        else:

                            ave4L[j].append(examples[i+2][j])
                            mostSfL[j]=(mostSfL[j]*(len(ave4L[j])-1)+ave4L[j][-1])/len(ave4L[j])

                else:
                    if j==dlength-1:
                        delation.append(i+2)
                    else:
                        if Dis_Cons[j]==True:
                            alignpos.append([i,j])
                            examples[i+2].append(-50)
                        else:
                            serialpos.append([i,j])
                            examples[i+2].append(-50.0)
        # Switch ? to the most common data
        for cc in range(0,len(alignpos)):
            a=alignpos[cc][0]
            b=alignpos[cc][1]
            if data[a][dlength-1].find('1')!=-1:
                examples[a+2][b]=mostcfW[b][1]
            else:
                examples[a+2][b]=mostcfL[b][1]
        for cc in range(0,len(serialpos)):
            a=serialpos[cc][0]
            b=serialpos[cc][1]
            if data[a][dlength-1].find('1')!=-1:
                examples[a+2][b]=mostSfW[b]
            else:
                examples[a+2][b]=mostSfL[b]
        counterz=0
        for i in range(0,len(delation)):
            del examples[delation[i]-counterz]
            counterz+=1
    else:
        Dis_Cons = []
        delation = []
        examples.append([])
        for i in range(0,dlength):
            temp=data[1][i]
            if i ==0:
                examples[0].append(data[0][0][:])
            else:
                examples[0].append(data[0][i][1:])
            if temp!= '?':
                if temp.find('.')!=-1:
                    Dis_Cons.append(False)
                else:
                    Dis_Cons.append(True)
            else:
                temp=data[2][i]
                if temp!= '?':
                    if temp.find('.')!=-1:
                        Dis_Cons.append(False)
                    else:
                        Dis_Cons.append(True)
        examples.append(Dis_Cons[:])
        # del examples[1][dlength]
        examples.append([])
        for i in range(0,dlength-1):
            examples[2].append(False)
        for i in range(1,plength):
            examples.append([])
            for j in range(0,dlength-1):
                if data[i][j]!='?':
                    if Dis_Cons[j]==True:
                        examples[i+2].append(int(data[i][j]))
                    else:
                        examples[i+2].append(float(data[i][j]))
                else:
                    examples[i+2].append(-50)
                    if not i+2 in delation:
                        delation.append(i+2)
        counterz=0
        for i in range(0,len(delation)):
            del examples[delation[i]-counterz]
            counterz+=1
        if len(examples[-1])==0:
            del examples[-1]
    return examples

def prettify(elem):
    #Return a pretty-printed XML string for the Element.
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def generateXMLLoop(root,topTag):
    for child in root.children:
        childTag = SubElement(topTag, child.name)
        if child.parentRule[0] == "=":
            syntax = "equal"
        elif child.parentRule[0] == ">":
            syntax = "above"
        else: 
            syntax = "below"
        childTag.text = root.name + " " + syntax + " " + child.parentRule[1:] + " " + str(child.imprValue)
        generateXMLLoop(child,childTag)

#This function is to print the tree out in console window
#A corresponding XML file is also generated as "results.xml"
def generateXMLFile(root):
    rootTag = Element(root.name)
    generateXMLLoop(root,rootTag)
    print prettify(rootTag)
    tree = ET.ElementTree(rootTag)
    tree.write("results.xml")

def output(examples):
    csvfile = open('labeled.csv', 'w')
    writer = csv.writer(csvfile,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #writer = csv.writer(sys.stdout)
    for item in examples:
        writer.writerow(item)

<<<<<<< HEAD
#This function create a decision tree from a training set "fileName", 
#gapNum is a parameter for selecting continuous attributes  
#portion is used to decide how much of the training set we use
def solve(fileName,gapNum = 10,portion = 1):
    examples = readFile(fileName, 0,portion) 
=======

def solve(fileName,gapNum,portion):
    examples = readFile(fileName, 0, portion) 
>>>>>>> origin/master
    root = TreeNode(examples,None,"",max((len(examples)-3)*0.001,1),gapNum)
    return root


#This function returns the accuracy of decision tree 'root' on a certain validation file 'fileName'
def validation(fileName,root):
    testdata = readFile(fileName, 0,1) #do not forget to add portion as 1.
    stat =[]
    missum=0#total wrong.
    root.validate(testdata,stat)
    for i in range(0,len(stat)):
        missum+=stat[i]
    #print len(stat)
    accuracy=float(missum)/float(len(testdata)-3)
    accuracy=1-accuracy
    return accuracy


def generateTest(fileName, root):
    examples = readFile(fileName, 1, 1)
    print len(examples)
    for dataIndex in range(3, len(examples)):
        outcome = root.generateOutcome(examples[dataIndex], examples)
        examples[dataIndex].append(outcome)
    #del examples[1]
    #del examples[1]
    output(examples)

#This function will prune the tree 'root'
def pruningAll(fileName,root):
    validation(fileName,root)
    root.calcImprGloValue()
    print str(pruning(root)) + " subtrees pruned!!"

def pruning(root):
    if root.name != "Good" and root.name != "Bad":
        if (root.imprValue > 0) and (root.imprValue >= root.imprGloValue):
            root.children = []
            root.rule = []
            #print "a node is pruned"
            if root.isGood:
                root.name = "Good"
            else:
                root.name = "Bad"
            return 1
        else:
            sum = 0
            for child in root.children:
                sum += pruning(child) 
            return sum
    return 0


#This function returns the node (including leaf) number of a tree
def calcNodeNum(root):
    sum = 1
    for child in root.children:
        sum += calcNodeNum(child)
    return sum


def printDNF(root):
    count = []
    res = root.getDNF(count)
    if res[-4:] == " or ":
        res = res[:-4]
    return res

