'''
https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
https://youtu.be/2JSQIhPcHQg
'''
class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,n ,arr ,m):
        if n<m:
            return -1
        start = max(arr)
        end = sum(arr)
        result = -1
        def isValid(arr,n,m,mid):
            student = 1
            add = 0
            for i in range(n):
                add = add + arr[i]
                if add>mid:
                    student+=1
                    add = arr[i]
                if student>m:
                    return False
            return True
        while start<=end:
            mid = start+(end-start)//2
            if isValid(arr,n,m,mid):
                result = mid
                end=mid-1
            else:
                start=mid+1

        return result
