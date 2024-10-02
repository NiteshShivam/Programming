'''
https://leetcode.com/problems/rank-transform-of-an-array/description/

'''
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        tempA = sorted(arr)
        result = []
        length = len(arr)
        mp = {}
        for i in tempA:
            if i not in mp:
                mp[i]=len(mp)+1
        for i in arr:
            result.append(mp[i])
        return result
