'''
https://www.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1
'''


class Solution:
    def longestUniqueSubsttr(self, S):
        length = len(S)
        j = 0
        i = 0
        result = 0
        space = {}
        ans = 0
        while j<length:
            space[S[j]] = space.get(S[j],0)+1
            while i<=j and space[S[j]]!=1:
                space[S[i]]-=1
                if space[S[i]]==0:
                    del space[S[i]]
                i+=1
            ans = max(ans,j-i+1)
            j+=1
        return ans
