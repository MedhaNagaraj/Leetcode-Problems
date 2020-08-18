# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 23:33:41 2020

@author: medha
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

    
        if n > 0 :
            if (n & (n-1)):
                return False
            else:
                return True
            
            
        # Method 2
        # return (n > 0) and not(n & n-1) 
        
        # Method 3            
        # original_decimal = (math.floor(math.log(n,2) * 10000000000) / 10000000000)
        # nearest_decimal = (math.floor(math.log(n,2) * 10000000000) / 10000000000)  + 0.0000000001
        
        # if n > 0 and original_decimal.is_integer():
        #     return True
        # elif n > 0 and nearest_decimal.is_integer():
        #     return True     
        # else:
        #     return False