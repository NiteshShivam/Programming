/*
https://leetcode.com/problems/lexicographical-numbers/description/
mik-video:
https://youtu.be/vuS3US_bDBo
  */
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> result;
        
        for(int i=1;i<=n;i++){
            
            result.push_back(i);
        }
        sort(result.begin(),result.end(),[](int x,int y){
            string s1 = to_string(x);
            string s2 = to_string(y);
            return s1<s2;
        });
        return result;
    }
};


// using dfs
=====================================================
 class Solution {
public:
    void dfs(int i,vector<int>& result,int n){
        if(i>n){
            return;
        }
        for(int j=0;j<=9;j++){
            if(i*10+j<=n){
                result.push_back(i*10+j);
                dfs(i*10+j,result,n);
            }
        }
    }
    vector<int> lexicalOrder(int n) {
     vector<int> result;
     for(int i=1;i<=9;i++){
        if(i<=n){
        result.push_back(i);
        dfs(i,result,n);}
     }
     return result;   
    }
};
