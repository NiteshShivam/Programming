'''

https://www.geeksforgeeks.org/problems/shortest-unique-prefix-for-every-word/1
'''
class TrieNode():
    def __init__(self):
        self.child = {}
        self.freq = 0

class Solution:
    def __init__(self):
        self.root= TrieNode()
    def insert(self,word):
        temp = self.root
        for each in word:
            if each not in temp.child:
                temp.child[each] = TrieNode()
            temp.child[each].freq+=1
            temp  = temp.child[each]
        
    def uniquePath(self,word):
        temp = self.root
        result = ""
        for each in word:
            if temp.freq==1:
                break
            result = result+each
            temp = temp.child[each]
            
        return result
    def findPrefixes(self, arr, N):
        for each in arr:
            self.insert(each)
        result = []
        for i in range(N):
            result.append(self.uniquePath(arr[i]))
        return result
