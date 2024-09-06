/*
https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1
mik-video:
https://youtu.be/E6DeC0Zpdns?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY
*/
class Solution
{
	public:
	
	void dfsT(vector<vector<int>>& adjR,vector<bool>& visited,int u){
	    visited[u]=true;
	    for(auto &v:adjR[u]){
	        if(visited[v]==false)
	        dfsT(adjR,visited,v);
	    }
	}
	
	void dfs(vector<vector<int>>& adj,vector<bool>& visited,stack<int>& st,int u){
	    visited[u]=true;
	    for(auto &v:adj[u]){
	        if(visited[v]==false){
	            dfs(adj,visited,st,v);
	        }
	    }
	    st.push(u);
	}
    int kosaraju(int V, vector<vector<int>>& adj)
    {
        stack<int> st;
        vector<bool> visited(V,false);
        for(int i=0;i<V;i++){
            if(visited[i]==false){
                dfs(adj,visited,st,i);
            }
        }
    
    vector<vector<int>> reverseAdj(V);
    for(int u=0;u<V;u++){
        for(int &v:adj[u]){
            reverseAdj[v].push_back(u);
        }
    }
    
    int count=0;
    visited=vector<bool>(V,false);
    while(!st.empty()){
        int node =st.top();
        st.pop();
        if(!visited[node]){
            dfsT(reverseAdj,visited,node);
            count+=1;
        }
    }
    
    return count;
    }
};
