/*
https://leetcode.com/problems/break-a-palindrome/description/
mik-video:
https://youtu.be/Pbx0Pvyh7D4?list=PLpIkg8OmuX-J8_n8Vy9P9I3KvyDcPMzRU
  */
class Solution {
public:
    string breakPalindrome(string palindrome) {
        int n=palindrome.size();
        for(int i=0;i<n/2;i++){
            if(palindrome[i]!='a'){
                palindrome[i]='a';
                return palindrome;
            }
        }
        if(n==1){
            return "";
        }
        palindrome[n-1]='b';
        return palindrome;
    }
};
