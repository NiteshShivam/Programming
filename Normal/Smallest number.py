'''
Given two integers s and d. The task is to find the smallest number such that the sum of its digits is s 
and the number of digits in the number are d. Return a string that is the smallest possible number. 
If it is not possible then return -1.




https://www.youtube.com/watch?v=H7iqIjbWty4
https://www.geeksforgeeks.org/problems/smallest-number5829/1
'''
class Solution:
    def smallestNumber(self, s, d):
        # code here
        if 9*d<s:
            return -1
        result = ''
        
        for i in range(d-1,-1,-1):
            if s>9:
                result = '9'+result
                s -=9
            else:
                if i==0:
                    result = str(s)+result
                else:
                    result = str(s-1)+result
                    i-=1
                    while i>0:
                        result = str(0)+result
                        i-=1
                    result = '1'+result
                    break
        return result
        
