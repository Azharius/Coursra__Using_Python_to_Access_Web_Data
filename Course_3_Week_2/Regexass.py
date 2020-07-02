import re
name = input("Enter file:")
if len(name) < 1 : name = 'Regex_sum_43.txt'
hand = open(name)
numlist=list()
sum=0
for line in hand:
    line=line.rstrip()
    #Finding all numbers in a line
    num=re.findall('[0-9]+',line)
    #if length of list returned by findall is 0 then don't take it
    if len(num)<1:continue
    #Converting nested lists to a single list
    for nums in num:
        numlist.append(nums)
#Calculating sum of all the numbers present in the list extracted before
for nos in numlist:
    sum=sum+int(nos)
#Print the list
print(numlist)
#Print the sum
print(sum)
