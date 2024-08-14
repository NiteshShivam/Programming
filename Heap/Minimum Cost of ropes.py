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
