/*
https://leetcode.com/problems/palindrome-partitioning-ii/description/
mik-video
https://youtu.be/XSe1_koFPzo

  */

// passing all test case.
class Solution {
public:
    vector<int> dp;
    bool palindrome(string& s,int start,int end){
        int i=start;
        int j = end;
        while(i<=j){
            if(s[i]==s[j]){
                i++;
                j--;
            }
            else{
                return false;
            }
        }
        return true;

    }
    int solve(string& s,int start,vector<int>& dp){
        if(start==s.size() || palindrome(s,start,s.size()-1)){
            return 0;
        }
       
        if(dp[start]!=INT_MAX){
            return dp[start];
        }
        int min_cut=INT_MAX;
        for(int end=start;end<s.size();end++){
            if(palindrome(s,start,end)){
                int result = 1+solve(s,end+1,dp);
                min_cut = min(min_cut,result);
            }
        }
        return dp[start]=min_cut;
    }
    
    int minCut(string s) {
        int length = s.size();
        dp.resize(length,INT_MAX);
        return solve(s,0,dp);
    }
};



==========================

// giving time limit
class Solution {
public:
    int dp[2000][2000];
    bool palindrome(string& s,int start,int end){
        int i=start;
        int j = end;
        while(i<=j){
            if(s[i]==s[j]){
                i++;
                j--;
            }
            else{
                return false;
            }
        }
        return true;
    }
    int solve(string& s,int start,int end){
        if(start>=end){
            return 0;
        }
        if(dp[start][end]!=-1){
            return dp[start][end];
        }
        if(palindrome(s,start,end)){
            return 0;
        }
        int result=INT_MAX;
        for(int k=start;k<=end-1;k++){
            int part = 1+solve(s,start,k)+solve(s,k+1,end);
            result = min(result,part);
        }
        return  dp[start][end] = result;
    }
    int minCut(string s) {
       
        int l = s.size();
        memset(dp,-1,sizeof(dp));
       
        return solve(s,0,l-1);
    }
};
