/*
https://leetcode.com/problems/longest-palindromic-substring/description/
mik-video:
https://youtu.be/ij3X5SAhf_0?list=PLpIkg8OmuX-JhFpkhgrAwZRtukO0SkwAt
  */

class Solution {
public:
    string longestPalindrome(string s) {
        int result =0;
        int start=0;
        int end=0;
        int n = s.length();
        vector<vector<bool>>t(n,vector<bool>(n,false));
        for(int L=1;L<=n;L++){
            for(int i=0;i+L-1<n;i++){
                int j=i+L-1;
                if(i==j){
                    t[i][j]=true;
                    
                }
                else if(i+1==j){
                    t[i][j]=s[i]==s[j];
                }
                else{
                    t[i][j] = (s[i]==s[j])&&(t[i+1][j-1]);
                }
                if(t[i][j]){
                    if (result<j-i+1){
                        result = j-i+1;
                        start =i;
                        end=j;
                    }
                }
            }
        }
        return s.substr(start,result);
    }
};
