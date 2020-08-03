"""
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        reversed_word = []

        for char in s.lower():
            if char.isalpha()or char.isdigit():
                #print(char)
                arr.append(char)
        reversed_word = arr[::-1]
        
        print(arr)
        print(reversed_word)
        return arr == reversed_word