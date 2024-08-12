'''
https://www.geeksforgeeks.org/problems/sum-of-middle-elements-of-two-sorted-arrays2305/1
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
