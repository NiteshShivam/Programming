'''

https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1
https://www.youtube.com/watch?v=DzfmJoFq1pc
'''
class Solution:
	def shortest_distance(self, matrix):
		length = len(matrix)
		row = length
		col = len(matrix[0])
		
		for i in range(row):
		    for j in range(col):
		        if matrix[i][j]==-1:
		            matrix[i][j]=float('inf')
		
		
		
		
		for via in range(length):
		    for i in range(row):
		        for j in range(col):
		            matrix[i][j] = min(matrix[i][j],matrix[i][via]+matrix[via][j])
        
        
        
        
        for i in range(row):
		    for j in range(col):
		        if matrix[i][j]==float('inf'):
		            matrix[i][j]=-1
        return matrix
