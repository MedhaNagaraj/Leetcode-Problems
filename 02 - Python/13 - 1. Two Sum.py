# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 00:12:01 2020

@author: medha
"""
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
#nums = [2, 7, 11, 15]
#target = 9
#
#print(nums)

def twosum(nums, target):
    
    prevMap = {} # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return
#    result = {}
#    for i, n in enumerate(nums):
#        print(i,n)
#        diff = target - n
#        if diff in result:
#            return[result[diff],i]
#        result[i] = n
#    return


twosum([2, 7, 11, 15], 9)

