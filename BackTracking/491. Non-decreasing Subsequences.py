'''
https://leetcode.com/problems/non-decreasing-subsequences/description/
mik-video:
https://youtu.be/8dfPwZvvDc8?list=PLpIkg8OmuX-KJPC18SGiRUzJQAYo839ox

'''
class Solution:
    def solve(self,index,curr):
        if len(curr)>=2:
            self.result.append(curr[:])
        s = set()
        for i in range(index,self.length):
            if (not curr or curr[-1]<=self.nums[i]) and self.nums[i] not in s:
                curr.append(self.nums[i])
                self.solve(i+1,curr)
                curr.pop()
                s.add(self.nums[i])
        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        self.result = []
        self.nums = nums
        self.length = len(nums)
        self.solve(0,[])
        return self.result
