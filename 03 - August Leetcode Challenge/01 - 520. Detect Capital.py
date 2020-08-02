"""
520. Detect Capital 

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True
 

Example 2:
Input: "FlaG"
Output: False

"""

#Approach 1
def detectCapitalUse(self, word: str) -> bool:
    if len(word) == 1:
        return True
    if word.islower():
        return(word.islower())
        #print('Everything is lower')
    elif word.isupper():
        return(word.isupper())
        #print('Everything is upper')
    elif word[0].isupper() and word[1:].islower():
        return True
        #print('Only first word is upper')
    else:
        return False
        
#Approach 2
import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)

"""
Complexity Analysis
Time complexity: Basically O(n)O(n), but depends on implementation.
Space complexity : O(1)O(1). We only need constant spaces to store our pattern.
"""


#Approach 3
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        if len(word) == 1:
            return True

        # case 1: All capital
        if word[0].isupper() and word[1].isupper():
            for i in range(2, n):
                if not word[i].isupper():
                    return False
        # case 2 and case 3
        else:
            for i in range(1, n):
                if word[i].isupper():
                    return False

        # if pass one of the cases
        return True
    
"""
Complexity Analysis
Time complexity: O(n)O(n), where n is the length of the word. We only need to check each char at most constant times.
Space complexity : O(1)O(1). We only need constant spaces to store our variables.
"""