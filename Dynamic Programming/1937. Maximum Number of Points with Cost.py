'''
https://leetcode.com/problems/maximum-number-of-points-with-cost/description/
https://www.youtube.com/watch?v=0AlKD9rZfm4ff
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        row = len(points)
        col = len(points[0])
        prev = points[0]

        for i in range(1,row):
            left = [0]*col
            right = [0]*col
            left[0]= prev[0]

            for j in range(1,col):
                left[j] = max(left[j-1]-1,prev[j])
            right[col-1]=prev[col-1]
            for j in range(col-2,-1,-1):
                right[j] = max(right[j+1]-1,prev[j])
            for j in range(col):
                prev[j] = max(left[j],right[j])+points[i][j]
        return max(prev)
