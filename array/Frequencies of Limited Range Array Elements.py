'''
https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1

https://youtu.be/B2hI-QPoisk
'''

'''Given an array arr[] of n positive integers which can contain integers from 1 to p
where elements can be repeated or can be absent from the array.
Your task is to count the frequency of all numbers from 1 to n.
Do modify the array in-place changes in arr[], such that arr[i] = frequency(i) and assume 1-based indexing.

Note: The elements greater than n in the array can be ignored for counting. 
'''

Approach 1 using space:
class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        hashM = {}
        for i in range(N):
            hashM[arr[i]]=hashM.get(arr[i],0)+1
        for i in range(N):
            arr[i]=0
        for key,value in hashM.items():
            if key<=N:
                arr[key-1]=value


Approach 2:
class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        i = 0
        while i<N:
            if arr[i]<=0:
                i+=1
                continue
            value = arr[i]-1
            if value>=N:
                arr[i]=0
                i+=1
                continue
            if arr[value]<=0:
                arr[value]-=1
                arr[i]=0
                i+=1
            else:
                arr[i] = arr[value]
                arr[value]=-1
        #print(arr)
        for i in range(N):
            arr[i]=abs(arr[i])
            
