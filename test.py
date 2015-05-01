execfile("decisiontree.py")
execfile("main.py")


root = solve("bvalidate.csv",10)
print validation("bvalidate.csv", root)
print printDNF(root)
validation("bvalidate.csv", root)

