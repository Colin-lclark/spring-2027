# Get the number of trees in this csv file by reading the number of rows
def treeInstances():
    numlines = 0
    with open('/Users/Colin/spring-2026/Tree Database/Tree_Records.csv') as rows:
        for line in rows:
            numlines += 1
    return numlines

print(treeInstances())