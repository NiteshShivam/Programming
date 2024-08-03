'''
https://www.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency-1587115621/1
'''
class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,a,n):
        store = {}
        for each in a:
            if each not in store:
                store[each]=0
            store[each]+=1
        result = []
        
        y = sorted(store.items(),key = lambda x:(-x[1],x[0]))
        for each in y:
            for i in range(each[1]):
                result.append(each[0])
        return result
        
