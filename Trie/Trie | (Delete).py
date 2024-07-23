'''

https://www.geeksforgeeks.org/problems/trie-delete/1?page=1
'''
class Solution():
    def deleteKey(self, root, key):
        #your code goes here
        temp = root
        for each in key:
            index = ord(each)-ord('a')
            if temp.children[index]!=None:
                temp = temp.children[index]
            else:
                return
        temp.isEndOfWord = False
