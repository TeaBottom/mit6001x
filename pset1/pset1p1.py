# MITx: 6.00.1x Problem Set 1 Problem 1
# Purpose: Display the number of vowels in a given string

s = "azcbobobegghakl"
numVowels = 0

for i in range(0, len(s)):
    if s[i] in "aeiou":
        numVowels += 1
print(numVowels)

