'''
https://www.geeksforgeeks.org/problems/stickler-theif-1587115621/1

https://youtu.be/SI6Pm8AKqnQ
'''

# cpp
class Solution
{
    public:
    vector<int> dp;
    int solve(int arr[],int index,int n){
        if(index>=n){
            return 0;
        }
        if(dp[index]!=-1){
            return dp[index];
        }
        int l = arr[index]+solve(arr,index+2,n);
        int r= solve(arr,index+1,n);
        return dp[index] = max(l,r);
    }
    int FindMaxSum(int arr[], int n)
    {
        dp.resize(n,-1);
        int index = 0;
        return solve(arr,index,n);
    }
    
};



=========================
class Solution:  
    
    #Function to find the maximum money the thief can get.
    
    def FindMaxSum(self,arr, n):
        prev = 0
        curr = 0
        for i in range(n):
            temp=curr
            curr = max(arr[i]+prev,curr)
            prev =temp
        return curr
        # code here


#c++
class Solution
{
    public:
    //Function to find the maximum money the thief can get.
    int FindMaxSum(int arr[], int n)
    {
            int prev=0;
            int curr=0;
            int temp=0;
            for(int i=0;i<n;i++)
            {
                temp=curr;
                curr = max(arr[i]+prev,curr);
                prev=temp;
            }
            return curr;
    }
};
