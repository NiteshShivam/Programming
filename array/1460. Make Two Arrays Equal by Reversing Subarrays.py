'''
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/
'''
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        s = {}
        for each in arr:
            if each not in s:
                s[each]=0
            s[each]+=1
        for each in target:
            if each not in s:
                return False
            else:
                if s[each]>=1:
                    s[each]-=1
                else:
                    return False
        return True
