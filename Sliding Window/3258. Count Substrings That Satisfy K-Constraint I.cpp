/*
https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/description/
mik->
https://youtu.be/2d1ALG8wwDc

  */
// Brute Force

class Solution {
public:
    int countKConstraintSubstrings(string s, int k) {
        int length = s.size();
        int result =0;
        for(int i=0;i<length;i++){
            int zero=0;
            int one =0;
            for(int j=i;j<length;j++){
                if(s[j]=='0'){
                    zero+=1;
                }
                else{
                    one++;
                }
                if(zero<=k || one<=k){
                    result+=1;
                }
                else{
                    break;
                }
            }
        }
        return result;
    }
};

=============================================
class Solution {
public:
    int countKConstraintSubstrings(string s, int k) {
        int result = 0;
        int i=0;
        int length = s.size();
        int j=0;
        int countZero=0;
        int countOne = 0;
        while(j<length){
            if(s[j]=='0'){
                countZero+=1;
            }
            else{
                countOne+=1;
            }
            while(countZero>k && countOne>k){
                if(s[i]=='0'){
                    countZero-=1;
                }
                else{
                    countOne-=1;
                }
                i+=1;
            }
            
            result+=j-i+1;
            j+=1;
            
            
        }
        return result;
    }
};
