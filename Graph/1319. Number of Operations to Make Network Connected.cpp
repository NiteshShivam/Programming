/*
https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
mik-video:
https://youtu.be/q2xBd-D_1KQ?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY
using dsu

  */
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
            rank[parenty]+=1;
            parent[parentx]=parenty;
        }
    }
    int makeConnected(int n, vector<vector<int>>& connections) {
        int components = connections.size();

        if(components<n-1){
            return -1;
        }
        parent.resize(n);
        rank.resize(n,0);
        for(int i=0;i<n;i++){
            parent[i]=i;
        }
        components =n;
        for(auto &v: connections){
            int x = v[0];
            int y = v[1];
            int parentx = find(x);
            int parenty = find(y);
            if(parentx!=parenty){
                Union(x,y);
                components--;
            }
        }
        return components-1;
    }
};
