# MITx: 6.00.1x Problem Set 1 Problem 3
# Purpose: Display the longest substring of a given lowercase string in which the letters occur in alphabetical order

# Define variables
s = 'azcbobobegghakl'
substringA = s[0]
substringB = 'a'

for i in range(0,len(s)-1,1):  # increment for loop through each character in string s
    a = i
    b = i+1
    substringB = s[a]
    while b < len(s) and s[a] <= s[b]:  # run while loop as long as lower bound /= last char & letters are alphabetical
        substringB += s[b]
        a = b
        b += 1
    if len(substringA) < len(substringB):  # if the current substring len > previous one, replace the previous substring
        substringA = substringB
print('Longest substring in alphabetical order is: ' + substringA)  # print the alphabetical longest substring
