'''
https://www.youtube.com/watch?v=9dKdLNlmxco
https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description/
'''
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row = len(rowSum)
        col  = len(colSum)
        matrix = [[0]*col for _ in range(row)]
        i =0
        j=0
        while i<row and j<col:
            temp = min(rowSum[i],colSum[j])
            matrix[i][j]=temp
            rowSum[i]-=temp
            if rowSum[i]==0:
                i+=1
            colSum[j]-=temp
            if colSum[j]==0:
                j+=1
        return matrix
