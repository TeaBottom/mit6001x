# MITx: 6.00.1x Problem Set 1 Problem 2
# Purpose: display the number of times the string 'bob' occurs in a given lower case string

s = 'azcbobobegghakl'
numBob = 0

for i in range(0,len(s),1):
    a = i
    b = i+3
    if s[a:b] == 'bob':
        numBob += 1
print('Number of times bob occurs is: ' + str(numBob))