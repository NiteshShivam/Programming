'''
https://www.geeksforgeeks.org/problems/heap-sort/1
'''
class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        leftChild = 2*i+1
        rightChild = 2*i+2
        maximum = -1
        if leftChild<n and arr[leftChild]>arr[i]:
            maximum = leftChild
        else:
            maximum=i
        if rightChild<n and arr[rightChild]>arr[maximum]:
            maximum=rightChild
        if maximum!=i:
            arr[maximum],arr[i]=arr[i],arr[maximum]
            self.heapify(arr,n,maximum)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        non_leaf = n//2
        for i in range(non_leaf,-1,-1):
            self.heapify(arr,n,i)
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        last = n-1
        while last>=1:
            arr[0],arr[last]=arr[last],arr[0]
            n=n-1
            last = last-1
            self.heapify(arr,n,0)
