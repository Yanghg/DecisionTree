execfile("decisiontree.py")
execfile("main.py")

'''
# Default solve should set the third parameter(portion) as 1.
for i in range(1,11):
    root = solve("btrain.csv",10, 11-i)
    print validation("bvalidate.csv", root)
'''


root = solve("btrain.csv",10,1)


#print validation("bvalidate.csv", root)
print printDNF(root)


