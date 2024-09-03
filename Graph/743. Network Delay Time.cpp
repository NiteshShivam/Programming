/*
https://leetcode.com/problems/network-delay-time/description/
mik-video:
https://youtu.be/hptQEIpvaxM?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY
  */
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
     priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
     vector<int> result(n+1,INT_MAX);
     unordered_map<int,vector<pair<int,int>>> adj;
     for(auto & time: times){
        int u = time[0];
        int v = time[1];
        int w = time[2];
        adj[u].push_back({v,w});
     }
     
     result[k]=0;
     pq.push({0,k});
     while(!pq.empty()){
        pair<int,int> p = pq.top();
        pq.pop();
        int dist = p.first;
        int node = p.second;
        for(auto &vec : adj[node]){
            int v = vec.first;
            int w = vec.second;

            if(dist+w <result[v]){
                result[v] =dist+w;
                pq.push({result[v],v});
            }
        }
     }
     int d=0;
     for(int i=1;i<=n;i++){
        if(result[i]==INT_MAX){
            return -1;
        }
        d = max(d,result[i]);
     }
     return d;

    }
};
