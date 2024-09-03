'''
Given a weighted, undirected and connected graph of V vertices and 
an adjacency list adj where adj[i] is a list of lists containing two integers 
where the first integer of each list j denotes there is edge between i and j ,
second integers corresponds to the weight of that  edge . 
You are given the source vertex S and You to Find the shortest distance of 
all the vertex's from the source vertex S. You have to return a list of integers denoting shortest distance between each node and Source vertex S.
 

Note: The Graph doesn't contain any negative weight cycle.

https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

https://youtu.be/xQ3vjWwFRuI


using-set mik
https://youtu.be/3qIoYIMidpc?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY
'''
import sys
import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        pq = []
        result = [sys.maxsize]*V
        result[S]=0
        heapq.heappush(pq,(0,S))
        while pq:
            distance,source = heapq.heappop(pq)
            for each in adj[source]:
                adjNode = each[0]
                weight = each[1]
                if distance+weight<result[adjNode]:
                    result[adjNode]=distance+weight
                    heapq.heappush(pq,(distance+weight,adjNode))
        return result



============================


class Solution
{
	public:
	//Function to find the shortest distance of all the vertices
    //from the source vertex S.
    vector <int> dijkstra(int V, vector<vector<int>> adj[], int S)
    {
       vector<int> result(V,INT_MAX);
       result[S]=0;
       set<pair<int,int>> s;
       s.insert({0,S});
       while(!s.empty()){
           auto &it = *s.begin();
           int d= it.first;
           int node =it.second;
           s.erase(it);
           for(auto &vec:adj[node]){
               int adjNode =vec[0];
               int dist = vec[1];
               if(d+dist<result[adjNode]){
                   if(result[adjNode]!=INT_MAX){
                       s.erase({result[adjNode],adjNode});
                   }
                   result[adjNode]=d+dist;
                   
                   s.insert({d+dist,adjNode});
               }
           }
           
       }
       return result;
    }
};
