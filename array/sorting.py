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

    def insertionSort(self,nums):
        length = len(nums)
        for j in range(1,length):
            key = nums[j]
            i=j-1
            while i>=0 and nums[i]>key:
                nums[i+1]=nums[i]
                i-=1
            nums[i+1]=key
    def selectionSort(self,nums):
        length = len(nums)
        for i in range(length):
            minV =nums[i]
            minI = i
            for j in range(i+1,length):
                if minV>nums[j]:
                    minV = nums[j]
                    minI = j
            nums[i],nums[minI]=nums[minI],nums[i]
    def partition(self,nums,left,right):
        value = nums[right]
        i = left-1
        for k in range(left,right):
            if nums[k]<=value:
                i = i+1
                nums[i],nums[k]=nums[k],nums[i]
        nums[i+1],nums[right]=nums[right],nums[i+1]
        return i+1
    def quickSort(self,nums,left,right):
        if left<right:
            p = self.partition(nums,left,right)
            self.quickSort(nums,left,p-1)
            self.quickSort(nums,p+1,right)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,0,len(nums)-1)

        #self.insertionSort(nums)
        #nums.sort()
        #self.selectionSort(nums)
        #self.quickSort(nums,0,len(nums)-1)
        return nums
