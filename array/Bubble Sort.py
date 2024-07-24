'''

https://www.geeksforgeeks.org/problems/bubble-sort/1
https://www.youtube.com/watch?v=xli_FI7CuzA
'''
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j+1],arr[j]=arr[j],arr[j+1]
