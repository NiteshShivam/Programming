'''
https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
'''
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        result = 0
        arr.sort(key=lambda x:x.value/x.weight,reverse=True)
        i = 0
        length = len(arr)
        while i<length :
            if arr[i].weight>w:
                result = result +(w/arr[i].weight) *arr[i].value
                w = 0
                break
            else:
                result = result+arr[i].value
                w = w -arr[i].weight
            i+=1
        return result
