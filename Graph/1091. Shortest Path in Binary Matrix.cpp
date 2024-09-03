/*
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
mik-video:
https://youtu.be/XsF-Xj_y5x8?list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY
  */
class Solution {
public:
    typedef pair<int,int>pa;
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        if(n==1){
            if(grid[0][0]==0){
                return 1;
            }
        }
        queue<pair<int,int>> q;
        if(grid[0][0]==1){
            return -1;
        }
        grid[0][0]=1;
        vector<pa> direction = {{1,0},{-1,0},{0,1},{0,-1},{1,1},{-1,-1},{1,-1},{-1,1}};
        q.push({0,0});
        int count=0;
        while(!q.empty()){
            int length = q.size();
            count++;
            while(length--){
            pair<int,int> p = q.front();
            q.pop();
            int u = p.first;
            int v = p.second;
            for(auto &temp:direction){
                int t1 = temp.first+u;
                int t2 = temp.second+v;
                if(t1>=0 && t1<m && t2>=0 && t2<n && grid[t1][t2]==0){
                    grid[t1][t2]=1;
                    q.push({t1,t2});
                    if(t1==m-1 && t2==n-1){
                        return count+1;
                    }
                }
            }
            }

        }

        return -1;
    }
};
