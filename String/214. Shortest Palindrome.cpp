/*
https://leetcode.com/problems/shortest-palindrome/description/
mik-video:
https://youtu.be/5DACQK9kud0
  */
class Solution {
public:
    string shortestPalindrome(string s) {
       string rev =s;
       reverse(begin(rev),end(rev));
       int n=s.length();
       for(int i=0;i<n;i++){
        if(!(memcmp(s.c_str(),rev.c_str()+i,n-i))){
            return rev.substr(0,i)+s;
        }
       } 
       return "";
    }
};
