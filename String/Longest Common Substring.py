'''
https://www.geeksforgeeks.org/problems/longest-common-substring1452/1
'''
class Solution:
    
    def longestCommonSubstr(self, S1, S2, n, m):
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if S2[i-1]==S1[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
        result = 0
        for i in range(m+1):
            for j in range(n+1):
                result = max(result,dp[i][j])
        return result


# cpp
========================================
class Solution {
  public:
    int longestCommonSubstr(string str1, string str2) {
        int m = str1.size();
        int n = str2.size();
        int result = 0;
        vector<vector<int>>matrix(m+1,vector<int>(n+1,0));
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(str1[i]==str2[j]){
                    matrix[i+1][j+1] = 1 + matrix[i][j];
                    result = max(result,matrix[i+1][j+1]);
                }
                else{
                    matrix[i+1][j+1] =0;
                }
            }
        }
        return result;
        
    }
};
