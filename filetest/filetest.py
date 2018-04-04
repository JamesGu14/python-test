import os
import csv
testFileName = os.getcwd() + '/test.txt'
csvFilePath = os.getcwd() + '/celebrities.csv'

# Read file line by line
'''
with open(testFileName) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
for line in content:
    print(line.strip())
'''

# Read CSV files
'''
totalLine = 0

with open(csvFilePath, newline='') as csvFile:
    spamReader = csv.reader(csvFile, delimiter=',')
    for row in spamReader:
        totalLine += 1

print(totalLine)
'''

# Loop directory
directoryPath = os.getcwd() + '/img/'
directory = os.fsencode(directoryPath)
validFileType = ["jpg", "jpeg", "png", "gif"]

for file in os.listdir(directory):
    fileName = os.fsdecode(file)
    if fileName =