'''
https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1
'''
class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        #print(A)
        result = A[-1]
        for i in range(N-M+1):
            result = min(result,A[i+M-1]-A[i])
        return result
