'''
https://leetcode.com/problems/maximum-distance-in-arrays/description/
https://youtu.be/OO6i7g3it4Q
'''
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        result = 0
        t = []
        minSoFar = arrays[0][0]
        maxSoFar  = arrays[0][-1]
        for i in range(1,len(arrays)):
            result = max(result,arrays[i][-1]-minSoFar)
            result = max(result,maxSoFar-arrays[i][0])
            minSoFar = min(minSoFar,arrays[i][0])
            maxSoFar = max(maxSoFar,arrays[i][-1])
        return result
