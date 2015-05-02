# DecisionTree

#how to build and run code:

1. To run the code, you need first run following command on your terminal:

    $ execfile("decisiontree.py")
    $ execfile("main.py")

2. To train and get the unpruned decision tree, run the following function:

    $ root = solve("btrain.csv")

    "btrain.csv" can be replaced by your own file name for training, root is the root node you generated

3. To prune your decision tree, you need to run 

    $ pruningAll("bvalidate.csv",root)

    Then 'root' will be the root node of the pruned tree

4. Output tree

    $ generateXMLFile(root)

5. Generate outcomes for test set.

    $ generateTest("btest.csv", root)

    'root' is the root node of your decision tree

6. print DNF format of your tree
    
    $ printDNF(root)

7. helper function

    $ validation("bvalidate.csv",root)

    Calculate the accuarcy of your decision tree with a certain set

    $ calcNodeNum(root)

    Calculate the nodes in your decision tree





