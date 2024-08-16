'''
https://www.geeksforgeeks.org/problems/cutted-segments1642/1
'''
class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        dp = [0]*(n+1)
        for i in range(1,n+1):
            count1 = 0
            count2 = 0
            count3 = 0
            if i-x>=0:
                if i-x==0 or dp[i-x]!=0:
                    count1 = 1 + dp[i-x]
            if i-y>=0:
                if i-y==0 or dp[i-y]!=0:
                    count2 = 1 + dp[i-y]
            if i-z>=0:
                if i-z==0 or dp[i-z]!=0:
                    count3 = 1 + dp[i-z]
            dp[i] = max(count1,count2,count3)
        # print(dp)
        return dp[n]

# cpp
=================================
class Solution
{
    public:
    //Function to find the maximum number of cuts.
    int maximizeTheCuts(int n, int x, int y, int z)
    {
        vector<int> dp(n+1,0);
        for(int i=1;i<=n;i++){
            if(i-x>=0 and( (i-x==0) or  dp[i-x]!=0))
            {
                dp[i] = max(dp[i],1+dp[i-x]);
            }
            if(i-y>=0 and( (i-y==0) or  dp[i-y]!=0))
            {
                dp[i] = max(dp[i],1+dp[i-y]);
            }
            
            if(i-z>=0 and( (i-z==0) or  dp[i-z]!=0))
            {
                dp[i] = max(dp[i],1+dp[i-z]);
            }
            
            
        }
        return dp[n];
    }
};
