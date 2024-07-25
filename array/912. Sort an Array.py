'''
https://leetcode.com/problems/sort-an-array/description/
'''
class Solution:
    def merge(self,nums,left,mid,right):
        temp = []
        i=left
        j=mid+1
        while i<=mid and j<=right:
            if nums[i]<nums[j]:
                temp.append(nums[i])
                i+=1
            else:
                temp.append(nums[j])
                j+=1
        while i<=mid:
            temp.append(nums[i])
            i+=1
        while j<=right:
            temp.append(nums[j])
            j+=1
        length = len(temp)
        for i in range(length):
            nums[i+left]=temp[i]
    def mergeSort(self,nums,left,right):
        if left<right:
            mid = left+(right-left)//2
            self.mergeSort(nums,left,mid)
            self.mergeSort(nums,mid+1,right)
            self.merge(nums,left,mid,right)


    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,0,len(nums)-1)
        return nums
