'''
https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
'''
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        ans = sum(Arr[:K])
        j = K
        current = ans
        i = 0
        while j<N:
            current = current+Arr[j]-Arr[i]
            i+=1
            j+=1
            ans = max(ans,current)
        return ans
