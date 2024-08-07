'''
Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. 
The task is to find the element that would be at the kth position of the final sorted array.

 
https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
nice Solution : https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/
https://youtu.be/nv7F4PiLUzo
'''

class Solution:
    
    def kthElement(self, k, arr1, arr2):
        def kth(k,arr1,arr2):
            length1 = len(arr1)
            length2 = len(arr2)
            if length1==0:
                return arr2[k]
            if length2==0:
                return arr1[k]
            mid1 = length1//2
            mid2 = length2//2
            if mid1+mid2<k:
                if arr1[mid1]>arr2[mid2]:
                    return kth(k-mid2-1,arr1,arr2[mid2+1:])
                else:
                    return kth(k-mid1-1,arr1[mid1+1:],arr2)
            else:
                if arr1[mid1]>arr2[mid2]:
                    return kth(k,arr1[:mid1],arr2)
                else:
                    return kth(k,arr1,arr2[:mid2])
        return kth(k-1,arr1,arr2)
======================================

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        i = 0
        j = 0
        k-=1
        while k>0:
            if i<n and (j>=m or arr1[i]<=arr2[j]):
                i+=1
            elif j<m and( i>=n or arr1[i]>arr2[j]):
                j+=1
            k-=1
        if i<n and (j>=m or arr1[i]<arr2[j]):
            return arr1[i]
        return arr2[j]


========================================
#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        n = len(arr1)
        m = len(arr2)
        if n>m:
            # we are appling binary search on smaller array.
            return self.kthElement(k,arr2,arr1)
        low = max(0,k-m)
        high = min(k,n)
        while low<=high:
            # middle element.
            cut1 = (low+high)>>1 
            cut2 = k-cut1

         
            l1 = float('-inf') if cut1==0 else arr1[cut1-1]
            l2 = float('-inf') if cut2==0 else arr2[cut2-1]
            r1 = float('inf') if cut1==n else arr1[cut1]
            r2 = float('inf') if cut2==m else arr2[cut2]
            
            
            if l1<=r2 and l2<=r1:
                return max(l1,l2)
            elif l1>r2:
                high = cut1-1
            else:
                low = cut1+1
        return 1
        
        
