import csv
outputFile = open("b.txt", "w")

result = []
with open('a.csv','r') as inputFile:
    header = inputFile.readline()
    for line in inputFile:
        tempNum = int(line.rstrip('\n'))
        result.append((3*tempNum+6).__str__())

with open('b.csv', 'w') as outFile:
    outFile.write("y")
    for i in range(0,1000):
        outFile.write('\n')
        outFile.write(result[i])

inputFile.close()
outputFile.close()