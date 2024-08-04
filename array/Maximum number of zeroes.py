'''
https://www.geeksforgeeks.org/problems/maximum-number-of-zeroes4048/1
'''
class Solution:
    def maxZero(self,arr):
        zero = 0
        ans =""
        n = len(arr)
        for i in range(n):
            curr = arr[i]
            count = curr.count('0')
            if count>0 and count>zero:
                zero=count
                ans=curr
            elif count>0 and count==zero:
                if len(curr)>len(ans):
                    ans=curr
                elif len(curr)==len(ans):
                    if curr>ans:
                        ans=curr
        if ans=="":
            return '-1'
        return ans
