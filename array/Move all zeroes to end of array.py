'''
https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1
'''
class Solution:
	def pushZerosToEnd(self,arr, n):
        i = -1
        j = 0
        while j<n:
            if arr[j]!=0:
                i+=1
                arr[i]=arr[j]
            j+=1
        i+=1
        while i<n:
            arr[i]=0
            i+=1
