'''
https://leetcode.com/problems/best-sightseeing-pair/solutions/1468367/code-walk-through-o-n-time-o-1-space

https://leetcode.com/problems/best-sightseeing-pair/description/
'''

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        result = 0
        maxLeft = values[0]+0
        for j in range(1,len(values)):
            result = max(result,maxLeft+values[j]-j)
            maxLeft = max(maxLeft,values[j]+j)
            
        return result
