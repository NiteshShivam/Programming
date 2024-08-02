'''
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/
https://youtu.be/t82KJaI1kNQ
'''
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        nums = nums+nums[:ones]
        i = 0
        j = ones
        length = len(nums)
        current = 0
        count = 0
        for k in range(ones):
            if nums[k]==0:
                count+=1
        result = count
        while j<length:
            zeroi=0
            zeroj=0
            if nums[i]==0:
                zeroi=1
            if nums[j]==0:
                zeroj=1
            count =count-zeroi+zeroj
            result = min(result,count)
            j+=1
            i+=1
        return result
