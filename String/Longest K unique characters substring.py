'''
https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
Solution : https://discuss.geeksforgeeks.org/comment/da93d7e385177f966d09674a2d380826/practice
'''

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        ans = -1
        i = 0
        length = len(s)
        freq = {}
        for j in range(length):
            if s[j] not in freq:
                freq[s[j]]=0
            freq[s[j]]+=1
            while len(freq)>k:
                freq[s[i]]-=1
                if freq[s[i]]==0:
                    del freq[s[i]]
                i+=1
            if len(freq)==k:
                ans = max(ans,j-i+1)
        return ans
