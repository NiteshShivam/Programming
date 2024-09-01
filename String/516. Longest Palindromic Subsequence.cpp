/*
https://leetcode.com/problems/longest-palindromic-subsequence/
mik-video:
https://youtu.be/M4pfB3G-YQc
  */
class Solution {
public:
    int t[1001][1001];
    int solve(string& s,int i,int j){
        if(i>j){
            return 0;
        }
        if(t[i][j]!=-1){
            return t[i][j];
        }
        if(s[i]==s[j]){
            if(i==j){
                return t[i][j]= 1+solve(s,i+1,j-1);
            }
            return t[i][j]=  2+solve(s,i+1,j-1);
        }
        return t[i][j]=  max(solve(s,i+1,j),solve(s,i,j-1));
    }
    int longestPalindromeSubseq(string s) {
        memset(t,-1,sizeof(t));

        return solve(s,0,s.size()-1);
    }
};



// LCS recursion + memo.
======================================

 class Solution {
public:
    int t[1001][1001];
    int LCS(string& s1,string &s2,int m,int n){
        if(m==0 || n==0){
            return t[m][n]=0;
        }
        if(t[m][n]!=-1)
            return t[m][n];
        if(s1[m-1]==s2[n-1]){
            return t[m][n] = 1+LCS(s1,s2,m-1,n-1);
        }
        return t[m][n] = max(LCS(s1,s2,m-1,n),LCS(s1,s2,m,n-1));
    }
    int longestPalindromeSubseq(string s) {
        memset(t,-1,sizeof(t));
        int m = s.size();
        string s2 = s;
        reverse(s2.begin(),s2.end());
        return LCS(s,s2,m,m);
        
    }   
};



// LCS bottom up
===============================
 class Solution {
public:
    int t[1001][1001];
    int LCS(string& s1,string &s2,int m,int n){
        for(int i=0;i<=m;i++){
            for(int j=0;j<=n;j++){
                if(i==0||j==0){
                    t[i][j]=0;
                }
                else if(s1[i-1]==s2[j-1]){
                    t[i][j] = 1+ t[i-1][j-1];
                }
                else{
                    t[i][j] = max(t[i-1][j],t[i][j-1]);
                }
            }
        }
        return t[m][n];
    }
    int longestPalindromeSubseq(string s) {
        memset(t,-1,sizeof(t));
        int m = s.size();
        string s2 = s;
        reverse(s2.begin(),s2.end());
        return LCS(s,s2,m,m);
        
    }   
};
