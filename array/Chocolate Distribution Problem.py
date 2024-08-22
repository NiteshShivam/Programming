'''
https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1

solution:
https://discuss.geeksforgeeks.org/comment/2cf8486841cf4b75932562b71295c2e2/practice
'''
class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        #print(A)
        result = A[-1]
        for i in range(N-M+1):
            result = min(result,A[i+M-1]-A[i])
        return result
