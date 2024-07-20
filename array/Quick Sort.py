'''
https://www.geeksforgeeks.org/problems/quick-sort/1
'''
#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low<high:
            pivot = self.partition(arr,low,high)
            self.quickSort(arr,low,pivot-1)
            self.quickSort(arr,pivot+1,high)
        return arr
    def partition(self,arr,low,high):
        prev = low-1
        temp = arr[high]
        for i in range(low,high):
            if arr[i]<=temp:
                prev+=1
                arr[prev],arr[i]=arr[i],arr[prev]
        prev+=1
        arr[prev] ,arr[high]= temp,arr[prev]
        return prev







===================================================
#Approach 2
class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low<high:
            pivot = self.partition(arr,low,high)
            self.quickSort(arr,low,pivot-1)
            self.quickSort(arr,pivot+1,high)
        return arr
    def partition(self,arr,low,high):
        pivot = arr[low]
        i = low
        j = high
        while True:
            while i<=high and arr[i]<=pivot:
                i+=1
            while j>=low and arr[j]>pivot:
                j-=1
            if i<j:
                arr[i],arr[j] = arr[j],arr[i]
            else:
                break
        arr[low],arr[j]=arr[j],arr[low]
        return j
        
