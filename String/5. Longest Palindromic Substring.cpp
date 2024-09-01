/*
https://leetcode.com/problems/longest-palindromic-substring/description/
mik-video:
https://youtu.be/ij3X5SAhf_0?list=PLpIkg8OmuX-JhFpkhgrAwZRtukO0SkwAt
  */


// recursion with memo.
class Solution {
public:
    vector<vector<int>>t;
    bool palindrome(string& s,int i,int j){

        if(i>=j){
            return true;
        }
        if(t[i][j]!=-1){
            return t[i][j];
        }
        if(s[i]==s[j]){
            return t[i][j]= palindrome(s,i+1,j-1);
        }
        else{
            return t[i][j] =false;
        }
    }
    string longestPalindrome(string s) {
        int n = s.length();
        t = vector<vector<int>> (n,vector<int>(n,-1));
        // t= (n,vector<int>(n,-1));
        int maxlen =0;
        int start=0;
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if(palindrome(s,i,j)){
                    if(j-i+1>maxlen){
                        maxlen=j-i+1;
                        start=i;
                    }
                }
            }
        }
        return s.substr(start,maxlen);
    }
};



// bottom -up
=========================================================
 
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
