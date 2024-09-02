'''
https://youtu.be/K_LamGUvwUc
https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
'''
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        visited = [0]*V
        currentdfs = [0]*V
        def dfs(i):
            visited[i]=1
            currentdfs[i]=1
            for each in adj[i]:
                if visited[each]==0 and dfs(each):
                    return True
                elif currentdfs[each]==1:
                    return True
            currentdfs[i]=0
            return False
        
        for i in range(V):
            if visited[i]==0 and dfs(i):
                return True
        return False
        




# cpp
==========================
class Solution {
  public:
    bool dfs(int u,vector<int> adj[],vector<bool>& visited,vector<bool>& inStack){
        visited[u]=true;
        inStack[u]=true;
        for(int &v:adj[u]){
            if(visited[v]==false && dfs(v,adj,visited,inStack)){
                return true;
            }
            else if(inStack[v]==true){
                return true;
            }
        }
        inStack[u]=false;
        return false;
    }
    bool isCyclic(int V, vector<int> adj[]) {
       vector<bool>visited(V,false);
       vector<bool>inStack(V,false);
       for(int i=0;i<V;i++){
           if(visited[i]==false && dfs(i,adj,visited,inStack)){
               return true;
           }
       }
       return false;
    }
};
