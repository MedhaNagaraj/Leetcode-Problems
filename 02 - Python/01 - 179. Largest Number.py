#Given a list of non negative integers, arrange them such that they form the largest number.
#Example 1:
#Input: [10,2] Output: "210"
#
#Example 2:
#Input: [3,30,34,5,9] Output: "9534330"
#
#Note: The result may be very large, so you need to return a string instead of an integer.

from itertools import permutations 
perm = []
xlist = []
lst = [3,34,5,30,9]

perm = permutations(lst) 

x = ''

for i in perm:
    for j in i:
        x = x + str(j)
#        print(x)
    xlist.append(int(x))
    x = ''
#    print(xlist)

result = max(xlist)
print(result)

