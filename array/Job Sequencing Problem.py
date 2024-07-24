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
