'''
https://www.geeksforgeeks.org/problems/sum-of-middle-elements-of-two-sorted-arrays2305/1

https://youtu.be/6D9T2ZY8h5c
'''
class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        length1 = len(arr1)
        length2 = len(arr2)
        temp = []
        i=0
        j=0
        while i<length1 and j<length2:
            if arr1[i]<arr2[j]:
                temp.append(arr1[i])
                i+=1
            else:
                temp.append(arr2[j])
                j+=1
        while i<length1:
            temp.append(arr1[i])
            i+=1
        while j<length2:
            temp.append(arr2[j])
            j+=1
        result = 0
        if (length1+length2)%2==0:
            t = (length1+length2)//2
            result = temp[t]+temp[t-1]
        else:
            t = (length1+length2)//2
            result = temp[t]
        return result



=========================
#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        length1 = len(arr1)
        length2 = len(arr2)
        t1  = (length1+length2)//2
        t2 = t1-1
        ans1= 0
        ans2=0
        i=0
        j=0
        k = 0
        while i<length1 and j<length2:
            if arr1[i]<arr2[j]:
                if k==t1:
                    ans1=arr1[i]
                elif k==t2:
                    ans2 = arr1[i]
                k+=1
                i+=1
            else:
                if k==t1:
                    ans1=arr2[j]
                elif k==t2:
                    ans2 = arr2[j]
                k+=1
                j+=1
                
                
        while i<length1:
            if k==t1:
                ans1=arr1[i]
            elif k==t2:
                ans2 = arr1[i]
            k+=1
            i+=1
        while j<length2:
            if k==t1:
                ans1=arr2[j]
            elif k==t2:
                ans2 = arr2[j]
            k+=1
            j+=1
        result = 0
        if (length1+length2)%2==0:
            result = ans1+ans2
        else:
           
            result = ans1
        return result
