'''
https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1
'''
class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def search(self,matrix, n, m, X): 
    	j = m-1
    	i = 0
    	while i<n and j>=0:
    	    if matrix[i][j]==X:
    	        return 1
    	    elif matrix[i][j]<X:
    	        i+=1
    	    else:
    	        j-=1
    	return 0
