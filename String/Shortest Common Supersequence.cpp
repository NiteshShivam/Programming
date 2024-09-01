/*
https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1
mik-video:
https://youtu.be/MTCvNG4Zfd8?list=PLpIkg8OmuX-JhFpkhgrAwZRtukO0SkwAt
  */
class Solution
{
    public:
    vector<vector<int>>dp;
    int solve(string& X,string& Y,int i,int j){
        if(i>=X.size()){
            return Y.size()-j;
        }
        if(j>=Y.size()){
            return X.size()-i;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        if(X[i]==Y[j]){
            return dp[i][j] = 1+solve(X,Y,i+1,j+1);
        }
        else{
            return dp[i][j] =  1+min(solve(X,Y,i+1,j),solve(X,Y,i,j+1));
        }
    }
    int shortestCommonSupersequence(string X, string Y, int m, int n)
    {
        // memset(dp,-1,sizeof(dp));
        dp.resize(m,vector<int>(n,-1));
        return solve(X,Y,0,0);
    }
};
