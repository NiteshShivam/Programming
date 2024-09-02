/*
https://leetcode.com/problems/course-schedule-ii/description/
mik-video:

https://youtu.be/W1WhSN9wAw0?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY

// dfs
https://youtu.be/yiR95dxinjs?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY
  */
class Solution {
public:
     bool checkTopo(unordered_map<int,vector<int>>& mp,vector<int>& indegree,int n,vector<int>& result){
        queue<int> q;
        // vector<int> result;
        int count=0;
        for(int i=0;i<n;i++){
            if(indegree[i]==0){
                q.push(i);
            }
        }
        while(!q.empty()){
            int u = q.front();
            result.push_back(u);
            count++;
            q.pop();
            for(int &v:mp[u] ){
                indegree[v]--;
                if(indegree[v]==0){
                    q.push(v);
                }
            }
        }
        return count==n;

    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int,vector<int>> mp;
        vector<int> indegree(numCourses,0);
        for(auto &vec:prerequisites){
            int a = vec[0];
            int b = vec[1];
            mp[b].push_back(a);
            indegree[a]++;
        }
        vector<int> result;
        bool b= checkTopo(mp,indegree,numCourses,result);
        if(b==false){
            return {};
        }
        return result;
        
    }
};



// dfs
=================================================
 class Solution {
public:
    bool checkDfs(unordered_map<int,vector<int>>& adj,int i,vector<bool> &inStack,vector<bool> &visited,stack<int>&s){
        visited[i]=true;
        inStack[i] =true;
        for(auto &v:adj[i]){
            if(visited[v]==false && checkDfs(adj,v,inStack,visited,s)){
                return true;
            }
            if(inStack[v]==true){
                return true;
            }
        }
        s.push(i);
        inStack[i]=false;
       return false;
    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int,vector<int>> adj;
     vector<bool> inStack(numCourses,false);
     vector<bool> visited(numCourses,false);
     for(int i=0;i<prerequisites.size();i++){
        int a = prerequisites[i][0];
        int b = prerequisites[i][1];
        adj[b].push_back(a);
    }
    stack<int> s;
    bool flag=false;
    for(int i=0;i<numCourses;i++){
        if(!visited[i] && checkDfs(adj,i,inStack,visited,s)){
           flag=true;
           break;
        }
    }
    if(flag){
        return {};
    }
      
    vector<int> r;
    while(s.size()>0){
        int t = s.top();
        r.push_back(t);
        s.pop();
    }
    return r;
    }
};
