import math

def calculateEntropy(dataSet):
    num = len(dataSet)
    freq={}
    entropy = 0.0

    for target in dataSet:
        current = target[-1]
     
        if not freq.has_key(current):
            freq[current]=0       
        freq[current]+=1
  
    for key in freq:
        prob = float(freq[key])/num       
        entropy -= prob*math.log(prob,2)

    return entropy