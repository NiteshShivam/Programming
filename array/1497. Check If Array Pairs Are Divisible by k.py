'''
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/

mik-video:
https://youtu.be/Lye_llDcSuI
'''
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        length = len(arr)
        for i in range(length):
            r = arr[i]%k
            if r<0:
                r = r+k
            arr[i] = r
      
        s = [0]*k
        for i in range(length):
            required = (k-arr[i])%k
            if s[required]!=0:
                s[required]-=1
                
            else:
                s[arr[i]]+=1
           
       
        for i in range(k):
            if s[i]!=0:
                return 0
        return 1
