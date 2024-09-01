/*
https://leetcode.com/problems/palindromic-substrings/
mik-video:
https://youtu.be/jCK_y0h8VVE?list=PLpIkg8OmuX-JhFpkhgrAwZRtukO0SkwAt
  */

// with memo
class Solution {
public:
    bool check(string& s,int i,int j){
        if(i>=j){
            return true;
        }
        if(s[i]==s[j]){
            return check(s,i+1,j-1);
        }
        else{
            return false;
        }
    }
    int countSubstrings(string s) {
        int n = s.length();
        int result = 0;
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if(check(s,i,j)==true){
                    result++;
                }
            }
        }
        return result;
    }
};


===============================================================
// recursion with memo

class Solution {
public:
    int t[1001][1001];
    bool check(string& s,int i,int j){
        if(i>=j){

            return true;
        }
        if(t[i][j]!=-1){
            return bool(t[i][j]);
        }
        if(s[i]==s[j]){

            bool b = check(s,i+1,j-1);
            if(b==true){
                t[i][j]=1;
            }
            else{
                t[i][j]=0;   
                         }
            return b;
        }
        else{
            t[i][j]=0;
            return false;
        }
    }
    int countSubstrings(string s) {
        memset(t,-1,sizeof(t));
        int n = s.length();
        int result = 0;
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if(check(s,i,j)==true){
                    result++;
                }
            }
        }
        return result;
    }
};









// O(n^2)

====================================================
class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        vector<vector<bool>>t(n,vector<bool>(n,false));
        int count=0;
        for(int L=1;L<=n;L++){
            for(int i=0;i+L-1<n;i++){
                int j = i+L-1;
                if(i==j){
                    t[i][i]=true;
                }
                else if(i+1==j){
                    t[i][j]= (s[i]==s[j]);
                }
                else{
                    t[i][j]= (s[i]==s[j])&&(t[i+1][j-1]);
                }
                if(t[i][j]){
                    count++;
                }
            }
        }
        return count;
    }
};
