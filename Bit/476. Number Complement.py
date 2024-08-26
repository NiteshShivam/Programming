'''
https://leetcode.com/problems/number-complement/description/
codestorywith mik
https://youtu.be/QaVwcw2f-pM

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

# mik concepts start here
# cpp
# time O(log2(num))
=======================
class Solution {
public:
    int findComplement(int num) {
        int length = int(log2(num))+1;
        for(int i=0;i<length;i++){
            num = num^(1<<i);
        }
        return num;
    }
};

===============================
class Solution {
public:
    int findComplement(int num) {
        int numb_bits = int(log2(num))+1;
        # 1U = 1 is unsigned.
        unsigned int mask_bits = (1U<<numb_bits)-1; 
        return mask_bits^num;
    }
};



===================================
class Solution {
public:
    int findComplement(int num) {
        int i=0;
        int complement = 0;
        while(num){
            if(!(num&1)){
                complement = complement| (1<<i);

            }
            num=num>>1;
            i+=1;
        }
        return complement;
    }
};
