execfile("decisiontree.py")
execfile("main.py")
root = solve("btrain.csv",10)
#print validation("bvalidate.csv", root)