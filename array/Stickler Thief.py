'''
https://www.geeksforgeeks.org/problems/stickler-theif-1587115621/1
'''
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
