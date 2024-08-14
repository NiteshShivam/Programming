'''
https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1
'''
import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
    
        
        result = 0
        space =[]
        for i in range(n):
            heapq.heappush(space,arr[i])
        while len(space)!=1:
            first = heapq.heappop(space)
            second = heapq.heappop(space)
            result = result+first+second
            heapq.heappush(space,first+second)
        return result




==============================
class Solution
{
    public:
    //Function to return the minimum cost of connecting the ropes.
    long long minCost(long long arr[], long long n) {
        priority_queue<long long,vector<long long>,greater<long long>> pq;
        for(int i=0;i<n;i++){
            pq.push(arr[i]);
        }
        long long result=0;
        while(pq.size()!=1){
            long long first = pq.top();
            pq.pop();
            long long second = pq.top();
            pq.pop();
            result = result+first+second;
            pq.push(first+second);
        }
        return result;
    }
};
