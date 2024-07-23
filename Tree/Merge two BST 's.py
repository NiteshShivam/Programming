'''

https://www.geeksforgeeks.org/problems/merge-two-bst-s/1
'''
class Solution:
    def inorder(self,root,result):
        if not root:
            return
        self.inorder(root.left,result)
        result.append(root.data)
        self.inorder(root.right,result)
    def merge(self, root1, root2):
        result1 = []
        result2 = []
        self.inorder(root1,result1)
        self.inorder(root2,result2)
        m = len(result1)
        n = len(result2)
        #print(result1)
        #print(result2)
        final = []
        i = 0
        j=0
        while i<m and j<n:
            if result1[i]<=result2[j]:
                final.append(result1[i])
                i+=1
            else:
                final.append(result2[j])
                j+=1
        while i<m:
            final.append(result1[i])
            i+=1
        while j<n:
            final.append(result2[j])
            j+=1
        return final
        
