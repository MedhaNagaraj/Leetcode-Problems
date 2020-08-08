# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 23:44:03 2020

@author: medha
"""

# import math

class Solution:
    
    def isPowerOfFour(self, num: int) -> bool:

        return num>0 and log(num,4).is_integer()

        # Approach 1

#         if(num > 1):
#             while(num % 4 == 0):
#                 num /= 4
        
#         return num == 1
        
#         Approach 2
#         if num > 0:
#             number = math.pow(abs(4),0.25)
#             return number - int(number) == 0
#         else:
#             return False

#         Approach 3
#         import math

# num = 268435455
# print(math.log(num,2))

# closest_decimal = (math.floor(math.log(num,2) * 10000) / 10000)
# nearest_decimal = (math.floor(math.log(num,2) * 10000) / 10000)  + 0.0001
# print(nearest_decimal)
# if num > 0 and closest_decimal.is_integer():
#     print(True)
# elif num > 0 and nearest_decimal.is_integer():
#     print(True)     
# else:
#     print(False)


#
#number = 16**(1/4)
#print(number)
#number = 5
#print(abs(num))
#
#if number > 0:
#    print("number is greater than 0")
#    num = math.pow(abs(4),)
#    print(number,"is a 4th power of", num)
#    
#    if (num - int(num) == 0):
#        print(num, True)
#    else:
#        print(False)
#
#else:
#    print("number is negative")

#num = 4
#
#if num > 1:
#    while (num % 4 == 0) :
#        num /= 4
#if num == 1:
#    print(True)
#else:
#    print(False)
