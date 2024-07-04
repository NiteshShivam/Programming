'''Given an array arr[] of N non-negative integers representing the height of blocks.
If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
 '''
Approach : 

class Solution:
    def trappingWater(self, arr,n):
        #Code here
        leftmax = [arr[0]]
        rightmax = [arr[-1]]
        j = n-2
        for i in range(1,n):
            leftmax.append(max(arr[i],leftmax[i-1]))
            rightmax.append(max(arr[j],rightmax[i-1]))
            j=j-1
        result = 0
        j = n-1
        for i in range(n):
            result =result + min(leftmax[i],rightmax[j])-arr[i]
            j=j-1
        
        return result
