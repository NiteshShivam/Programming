'''
https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
mik-video:
https://youtu.be/UrQv5YMC060?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY

# using bfs
https://youtu.be/UrQv5YMC060?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY
'''
from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
    def __init__(self):
        self.visited=None


    def dfs(self,adj,u,parent):
        self.visited[u]=True
        for each in adj[u]:
            if each==parent:
                continue
            if self.visited[each]==True:
                return True
            if  self.dfs(adj,each,u):
                return True
        return False




    def bfs(self,adj,u):
        self.visited[u]=True
        queue = deque()
        queue.append([u,-1])
        while  queue:
            temp = queue.popleft()
            source = temp[0]
            parent=temp[1]
            for each in adj[source]:
                if each==parent:
                    continue
                if self.visited[each]==True:
                    return True
                self.visited[each]=True
                queue.append([each,source])
        return False




	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		self.visited = [False]*V
		for i in range(V):
		    if not self.visited[i] and self.bfs(adj,i):
		        return True
		return False



# cpp dfs
=================================

class Solution {
  public:
    bool dfs(vector<int> adj[],int u,int parent,vector<bool>& visited){
        visited[u]=true;
        
        for(auto &v:adj[u]){
            if(v==parent)
            continue;
            if(visited[v]==true){
                return true;
            }
            if(dfs(adj,v,u,visited))
            {
                return true;
            }
        }
        return false;
        
    }
    bool isCycle(int V, vector<int> adj[]) {
        vector<bool>visited(V,false);
        for(int i=0;i<V;i++){
            if(visited[i]==0)
            {
                if(dfs(adj,i,-1,visited))
                {
                    return true;
                }
            }
        }
        return false;
    }
};



# bfs
==================================
class Solution {
  public:
    bool isCycle(vector<int> adj[],int i,vector<bool>& visited){
        queue<pair<int,int>> q;
        q.push({i,-1});
        visited[i]=true;
        while(!q.empty()){
            pair<int,int>P =q.front();
            q.pop();
            int parent = P.second;
            int u = P.first;
            for(int &v:adj[u]){
                if(v==parent){
                    continue;
                }
                if(visited[v]==false){
                    visited[v]=true;
                    q.push({v,u});
                }
                else{
                    return true;
                }
            }
        }
        return false;
    
    }
    bool isCycle(int V, vector<int> adj[]) {
         vector<bool> visited(V,false);
        for(int i=0;i<V;i++){
            if(visited[i]==false && isCycle(adj,i,visited)){
                return true;
            }
        }
        return false;
    }
};
