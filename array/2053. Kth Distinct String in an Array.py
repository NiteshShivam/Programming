'''
https://leetcode.com/problems/kth-distinct-string-in-an-array/
'''
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        space = {}
        for each in arr:
            if each not in space:
                space[each]=0
            space[each]+=1
        for each in arr:
            if space[each]==1:
                if k==1:
                    return each
                else:
                    k-=1
        return ""
