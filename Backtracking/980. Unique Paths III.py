'''
https://leetcode.com/problems/unique-paths-iii/description/

mik -video
https://youtu.be/eagGLroZXMk?list=PLpIkg8OmuX-KJPC18SGiRUzJQAYo839ox

'''
class Solution:
    def solve(self,grid,i,j,count):
        if i<0 or i>=self.m or j<0 or j>=self.n or grid[i][j]==-1:
            return 
        
        if grid[i][j]==2:
            if count==self.nObj:
                self.result +=1
            return
        if grid[i][j]==1 or grid[i][j]==0:
            count+=1
        grid[i][j]=-1
        for each in self.direction:
            new_i = i+each[0]
            new_j = j+each[1]
            self.solve(grid,new_i,new_j,count)
        grid[i][j]=0
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.nObj = 0
        self.result = 0
        self.direction = [(-1,0),(1,0),(0,-1),(0,1)]
        self.m = len(grid)
        self.n = len(grid[0])
        startI = 0
        startJ = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]==1 or grid[i][j]==0:
                    self.nObj+=1
                if grid[i][j]==1:
                    startI = i
                    startJ = j
        self.solve(grid,startI,startJ,0)
        
        return self.result


# cpp
===============================================
class Solution {
public:
    int m,n,result,nonObj;
    vector<vector<int>> direction{{1,0},{-1,0},{0,1},{0,-1}};
    void backTrack(vector<vector<int>>& grid,int i,int j,int count){
        if(i<0 || i>=m || j<0 || j>=n || grid[i][j]==-1){
            return;
        }
        if(grid[i][j]==2){
            if(count==nonObj){
                result++;
            }
            return;
        }
        grid[i][j]=-1;
        for(vector<int>&dir:direction){
            int new_i = i+dir[0];
            int new_j = j+dir[1];
            backTrack(grid,new_i,new_j,count+1);
        }
        grid[i][j]=0;
    }
    int uniquePathsIII(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        nonObj=0;
        result=0;
        int start_x=0;
        int start_y =0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==0 || grid[i][j]==1){
                    nonObj+=1;
                }
                if(grid[i][j]==1){
                    start_x=i;
                    start_y=j;
                }
            }
        }
        int count=0;
        backTrack(grid,start_x,start_y,count);
        return result;
    }
};
