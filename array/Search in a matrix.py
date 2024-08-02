'''
https://www.geeksforgeeks.org/problems/search-in-a-matrix17201720/1
'''
class Solution:
	def matSearch(self,mat, N, M, X):
		i=0
		j=M-1
		while i<N and j>=0:
		    if mat[i][j]==X:
		        return 1
		    elif mat[i][j]<X:
		        i+=1
		    else:
		        j-=1
		return 0
