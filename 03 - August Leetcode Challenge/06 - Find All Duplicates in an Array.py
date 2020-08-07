# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:42:41 2020

@author: medha
"""
"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

class Solution:
    def findDuplicates(self, nums):
        new_dict = {}
        result = []

        for n in nums:
            if n in new_dict:
                new_dict[n] += 1
            else:
                new_dict[n] = 1
        print(new_dict)

        for count in new_dict:
            if new_dict[count] > 1:
                result.append(count)
        return result
    
# Solution 2:
# class Solution(object):
#     def findDuplicates(self, nums):
#         for i in range(len(nums)):
#             while i != nums[i] - 1 and nums[i] != nums[nums[i]-1]:
# 				nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

#         return [nums[it] for it in range(len(nums)) if it != nums[it] - 1]
        