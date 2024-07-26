'''
https://www.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair-1587115620/1
'''
class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        first = 1
        second = 2
        ans = 0
        mod = 10**9+7
        mod =  1e9 + 7
        if n<=2:
            return n
        for i in range(3,n+1):
            ans = (first+second)%mod
            first = second
            second = ans
        return int(ans%mod)
