/*
https://leetcode.com/problems/course-schedule-ii/description/
mik-video:
https://youtu.be/W1WhSN9wAw0?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY
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
