# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 23:47:16 2020

@author: medha
"""

"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if (n < 1):
            return False

        while (n % 3 == 0):
            n /= 3;

        return n == 1;