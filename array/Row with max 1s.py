'''

https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1
'''

 # O(n+m)

class Solution:

	def rowWithMax1s(self,arr):
	    row = len(arr)
	    col = len(arr[0])
	    j = col-1
	    result = -1
	    for i in range(row):
	        while arr[i][j]==1 and j>=0:
	            result = i
	            j-=1
	    return result



============================================================================
class Solution:

	def rowWithMax1s(self,arr):
	    row = len(arr)
	    col = len(arr[0])
	    prevjS = col+1
	    prevR = -1
	    for i in range(row):
	        left = 0
	        right = col-1
	        prevj = -1
	        while left<=right:
	            mid = left+(right-left)//2
	            if arr[i][mid]==0:
	                left = mid+1
	            elif arr[i][mid]==1:
	                prevj=mid
	                right = mid-1
	           
	        if prevj !=-1:
	            if prevjS>prevj:
	                prevjS=prevj
	                prevR = i
	        
	    return prevR





=====================================
#User function Template for python3
class Solution:

    def rowWithMax1s(self,arr):
        col = len(arr[0])
        row = len(arr)
        for i in range(col):
            for j in range(row):
                if arr[j][i]==1:
                    return j
        return -1
	    
