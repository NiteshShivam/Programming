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

# nice way
=======================
class Solution:
    def findComplement(self, num: int) -> int:
        n = 0
        while n < num:
            n = (n << 1) | 1
        return n - num

# c++
=====================
class Solution {
public:
    int findComplement(int num) {
     int n=0;
     while(n<num){
        n = (n<<1)|1;
     }   
     return n-num;
    }
};
