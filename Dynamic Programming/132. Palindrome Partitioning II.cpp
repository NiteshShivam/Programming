/*
https://leetcode.com/problems/palindrome-partitioning-ii/description/
mik-video
https://youtu.be/XSe1_koFPzo

  */

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
