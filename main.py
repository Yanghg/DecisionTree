#-*- coding: UTF-8 -*-
import csv
from decisiontree import TreeNode

#examples = [["aa","bb","cc"],[True,False,True],[False,True,False],[1 2 3],[4 5 6]....[7 8 9]]


def handleAttribute(examples, name):
    return gain, rule

def readFile(fileName):
    # "rb" is read only
    csvReader = csv.reader(open(fileName,"rb"),delimiter=',') 
    data = list(csvReader)
    tlength=len(data)
    dlength= len(data[0])
    examples=[]
    Dis_Cons = []
    alignpos =[] 
    mostcfW= [] #Common num for win
    mostcfL= [] #Common num for win
    mapsW=[]#dict for win side
    mapsL=[]#dict for lose side
    delation=[]
    # find value type: discrete or continuous
    for i in range(0,dlength):
        temp=data[1][i]
        mapsL.append({})
        mapsW.append({})
        mostcfW.append([-1])
        mostcfL.append([-1])
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
    examples.append(data[0][:])
    examples.append(Dis_Cons[:])
    del examples[1][dlength-1]
    examples.append([])
    for i in range(0,dlength-1):
        examples[2].append(False)
    # Turn str to int or float
    for i in range(1,tlength):
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
                if j==dlength-1:
                    delation.append(i+2)
                else:
                    alignpos.append([i,j])
                    examples[i+2].append(-50)
    # Switch ? to the most common data
    for cc in range(0,len(alignpos)):
        a=alignpos[cc][0]
        b=alignpos[cc][1]
        if data[a][dlength-1].find('1')!=-1:
            examples[a+2][b]=mostcfW[b][1]
        else:
            examples[a+2][b]=mostcfL[b][1]
    counterz=0
    for i in range(0,len(delation)):
        del examples[delation[i]-counterz]
        counterz+=1
    return examples

def printTree(root):
    return

def solve(fileName,percentage):
    examples = readFile(fileName)
    root = TreeNode(examples,None)
    return root

def validation(fileName,root):
    testdata= readFile(fileName)
    stat=[]
    missum=0#total wrong.
    root.validate(testdata,stat)
    for i in range(0,len(stat)):
        missum+=stat[i]
    accuracy=float(missum)/float(len(testdata)-3)
    return accuracy
