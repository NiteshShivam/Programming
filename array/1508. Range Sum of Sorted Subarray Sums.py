'''
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/
https://youtu.be/oMHO5iti5_c
'''

import heapq
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        hp = []
        mod = 10**9+7
        for i in range(n):
            heapq.heappush(hp,(nums[i],i))
        result = 0
        count =1
        while count<=right:
            value,index = heapq.heappop(hp)
            if index<(n-1):
                heapq.heappush(hp,(value+nums[index+1],index+1))
            if count>=left:
                result+=value
            count+=1
        return result%mod


=======================

import heapq
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result = 0
        hp = []
        mod = 10**9+7
        for i in range(n):
            current = 0
            for j in range(i,n):
                current=current+nums[j]
                heapq.heappush(hp,current)
        count=1
        
        while count!=left:
            t =heapq.heappop(hp)
            count+=1
        while left!=right+1:
            result = result+heapq.heappop(hp)
            left+=1
        result = result%mod
        return result





