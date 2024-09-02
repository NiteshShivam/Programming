/*
https://leetcode.com/problems/satisfiability-of-equality-equations/description/
mik-video:
https://youtu.be/0Z8lt7U_kiE?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY
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
        else if (rank[parentx]<rank[parenty]){
            parent[parentx]=parenty;
        }
        else{
            rank[parenty] +=1;
            parent[parentx]=parenty;
        }
    }
    bool equationsPossible(vector<string>& equations) {
        parent.resize(26);
        rank.resize(26,0);
        for(int i=0;i<26;i++){
            parent[i]=i;
        }
        for(string &s:equations){
            if(s[1]=='='){
                Union(s[0]-'a',s[3]-'a');
            }
        }
        for(string &s:equations){
            if(s[1]=='!'){
                int x =find(s[0]-'a');
                int y = find(s[3]-'a');
                if(x==y){
                    return false;
                }
            }
        }
        return true;
    }
};
