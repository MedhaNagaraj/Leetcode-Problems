# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:23:45 2020

@author: medha
"""

# import math

class Solution:
    
    def isPowerOfFour(self, num: int) -> bool:

        #         Approach 1
        return num>0 and log(num,4).is_integer()

        # Approach 2

#         if(num > 1):
#             while(num % 4 == 0):
#                 num /= 4
        
#         return num == 1
        
#         Approach 3
#         if num > 0:
#             number = math.pow(abs(4),0.25)
#             return number - int(number) == 0
#         else:
#             return False


