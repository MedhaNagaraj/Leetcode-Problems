# -*- coding: utf-8 -*-
"""
@author: medha
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        for i in range(len(s)):
            t = s[:i] + s[i+1:]
            if t == t[::-1]: 
                return True
        
        if s == s[::-1]:
            return True
        