# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 20:40:21 2020

@author: medha
"""
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for s in word:
            if s not in node.child:
                node.child[s] = TrieNode()
            node = node.child[s]
        node.val = word
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def match(word, depth, node):
            if depth == len(word): return not (node.val=='')
            if word[depth] != '.':
                return word[depth] in node.child and match(word, depth + 1, node.child[word[depth]])
            else:
                for c in node.child:
                    if match(word, depth+1, node.child[c]):
                        return True
            return False
        return match(word, 0, self.root)
        

class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.val = ""
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)