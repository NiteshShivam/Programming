'''
https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
https://youtu.be/zPtI8q9gvX8
'''
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        deadline = 0
        
        for each in Jobs:
            deadline = max(deadline,each.deadline)
        Jobs.sort(key = lambda x:x.profit,reverse=True)
        length = len(Jobs)
        count =0
        profit = 0
        dead = [-1]*(deadline+1)
        for i in range(length):
            for j in range(Jobs[i].deadline,0,-1):
                if dead[j]==-1:
                    profit = profit+Jobs[i].profit
                    dead[j]=1
                    count+=1
                    break
            
        return (count,profit)








# cpp
=================================
class Solution 
{
    public:
    static bool compareByProfit(Job a,Job b){
        return a.profit>b.profit;
    }
    //Function to find the maximum profit and the number of jobs done.
    vector<int> JobScheduling(Job arr[], int n) 
    { 
        int maxDead = 0;
        for(int i=0;i<n;i++){
            maxDead = max(maxDead,arr[i].dead);
        }
        vector<int> space(maxDead,0);
        sort(arr,arr+n,compareByProfit);
        int count=0;
        int profit=0;
        for(int i=0;i<n;i++){
            for(int j=arr[i].dead-1;j>=0;j--){
                if(space[j]==0){
                    space[j]=1;
                    profit+=arr[i].profit;
                    count++;
                    break;
                }
            }
        }
        return {count,profit};
    } 
};
