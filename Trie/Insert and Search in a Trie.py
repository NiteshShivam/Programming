'''

https://youtu.be/YXefcFMpemo
https://www.geeksforgeeks.org/problems/trie-insert-and-search0651/1
'''
"""
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""

class Solution:
    #Function to insert string into TRIE.
    def insert(self, root, key):
        temp = root
        for each in key:
            place = ord(each)-ord('a')
            if temp.children[place] == None:
                temp.children[place]=TrieNode()
            temp = temp.children[place]
        temp.isEndOfWord = True
    
    #Function to use TRIE data structure and search the given string.
    def search(self, root, key):
        temp = root
        for each in key:
            place = ord(each)-ord('a')
            if temp.children[place] == None:
                return False
            temp =temp.children[place]
        return temp.isEndOfWord
