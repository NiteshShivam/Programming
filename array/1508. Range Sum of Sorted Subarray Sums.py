'''
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/
'''
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





