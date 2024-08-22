'''
https://leetcode.com/problems/number-complement/description/
'''
class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)
        result = ""
        for i in range(2,len(binary)):
            if binary[i]=='0':
                result+='1'
            else:
                result+='0'
        return int(result,2)
