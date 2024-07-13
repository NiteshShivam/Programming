'''
Given an array nums[] of size n, construct a Product Array P (of same size n)
such that P[i] is equal to the product of all the elements of nums except nums[i].

https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1
'''
class Solution:
    def productExceptSelf(self, nums, n):
        start = []
        last = []
        current =1
        end = 1
        j=-1
        if n==1:
            return [1]
        for num in nums:
            current = current*num
            start.append(current)
            end= end*nums[j]
            last.append(end)
            j-=1
        last = last[::-1]
        result =[]
        for i in range(n):
            if i==0 and i+1<n:
                result.append(last[i+1])
            elif i==n-1 and i-1>=0:
                result.append(start[i-1])
            else:
                result.append(start[i-1]*last[i+1])
        return result
        
        
        
