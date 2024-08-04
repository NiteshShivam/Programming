'''
https://www.geeksforgeeks.org/problems/find-the-minimum-time0253/1
'''

class Solution:
    def minTime(self, S1, S2, N):
        start =0
        end = min(S1*N,S2*N)
        ans =0
        def possible(s1,s2,n,mid):
            if mid//s1 +mid//s2>=n:
                return True
            return False
        while start<=end:
            mid = start+(end-start)//2
            if possible(S1,S2,N,mid):
                ans = mid
                end =mid-1
            else:
                start = mid+1
                
        return ans
