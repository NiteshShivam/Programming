/*
https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
mik-video:
dsu
https://youtu.be/Hh_9ppxgzpo?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY

dfs-bfs
https://youtu.be/kOt2VNsU0FE

  */
// using dsu
class Solution {
public:
    vector<int> parent;
    vector<int> rank;
    int find(int x){
        if(x==parent[x]){
            return x;
        }
        x = find(parent[x]);
        return parent[x];
    }
    void Union(int x,int y){
        int parentx = find(x);
        int parenty = find(y);
        if(parentx==parenty){
            return;
        }
        if(rank[parentx]>rank[parenty]){
            parent[parenty]=parentx;
        }
        else if(rank[parentx]<rank[parenty]){
            parent[parentx]=parenty;
        }
        else{
            rank[parentx]+=1;
            parent[parenty]=parentx;
        }
    }
    long long countPairs(int n, vector<vector<int>>& edges) {
        parent.resize(n);
        rank.resize(n,0);
        for(int i=0;i<n;i++){
            parent[i]=i;
        }
        for(auto &v:edges){
            int first=v[0];
            int second = v[1];
            Union(first,second);
        }
        unordered_map<int,int>mp;
        for(int i=0;i<n;i++){
            mp[find(i)]++;
        }
        long long result=0;
        long long remainingNode = n;
        for(auto &it:mp){
            int first = it.first;
            long long size = it.second;
            result+= (size)*(remainingNode-size);
            remainingNode =remainingNode-size;
        }
        return result;
    }
};


// using dfs
===================================
 class Solution {
public:
    void dfs(unordered_map<int,vector<int>>& adj,int i,long long& size,vector<bool>& visited){
        visited[i]=true;
        size++;
        for(auto &v:adj[i]){
            if(visited[v]==false){
                dfs(adj,v,size,visited);
            }
        }
    }

    long long countPairs(int n, vector<vector<int>>& edges) {
        unordered_map<int,vector<int>> adj;
        for(auto &vec:edges){
            int u = vec[0];
            int v = vec[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<bool> visited(n,false);
        long long remaining_nodes = n;
        long long result =0;
        
        for(int i=0;i<n;i++){
            if(visited[i]==false){
                long long size=0;
                dfs(adj,i,size,visited);
                result += size*(remaining_nodes-size);
                remaining_nodes = remaining_nodes-size;
                
            }
        }
        return result;
    }
};
