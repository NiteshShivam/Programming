'''
https://www.geeksforgeeks.org/problems/merge-sort/1
'''
class Solution:
    def merge(self,arr, l, m, r): 
        temp = []
        i = l 
        j = m+1
        while i<=m and j<=r:
            if arr[i]<arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        while i<=m:
            temp.append(arr[i])
            i+=1
        while j<=r:
            temp.append(arr[j])
            j+=1
        for i in range(l,r+1):
            arr[i]=temp[i-l]
            
    def mergeSort(self,arr, l, r):
        
        if l<r:
            mid = l+(r-l)//2
            self.mergeSort(arr,l,mid)
            self.mergeSort(arr,mid+1,r)
            self.merge(arr,l,mid,r)

