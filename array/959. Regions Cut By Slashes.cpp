/*
https://leetcode.com/problems/regions-cut-by-slashes/description/
https://youtu.be/zMqgIbLLsc4
  */
class Solution {
public:
    void dfs(vector<vector<int>>& matrix,int i,int j){
        int row = matrix.size();
        int col = matrix[0].size();
        matrix[i][j]=1;
        int direction[4][2] = {{-1,0},{0,-1},{1,0},{0,1}};
        for(int k = 0;k<4;k++){
            int new_i = i+ direction[k][0];
            int new_j = j+direction[k][1];
            if(new_i>=0 && new_i<row && new_j>=0 && new_j<col && matrix[new_i][new_j]==0){
                matrix[new_i][new_j]=1;
                dfs(matrix,new_i,new_j);
            }
        }
    }
    int regionsBySlashes(vector<string>& grid) {
        int row = grid.size();
        int col = grid[0].size();
        int regions = 0;
        vector<vector<int>> matrix(row*3,vector<int>(col*3,0));
        for(int i=0;i<row;i++){
            for(int j = 0;j<col;j++)
            {
                if(grid[i][j]=='/'){
                    matrix[i*3][j*3+2]=1;
                    matrix[i*3+1][j*3+1]=1;
                    matrix[i*3+2][j*3]=1;
                }
                else if (grid[i][j]=='\\'){
                    matrix[i*3][j*3]=1;
                    matrix[i*3+1][j*3+1]=1;
                    matrix[i*3+2][j*3+2]=1;
                }
            }
        }
        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<matrix[0].size();j++)
            {
                if(matrix[i][j]==0){
                    dfs(matrix,i,j);
                    regions++;
                }
            }
        }
        return regions;
    }
};


// .py
======================================
 class Solution:
    def dfs(self,i,j):
            self.matrix[i][j]=1
            direction = [(-1,0),(0,-1),(1,0),(0,1)]
            for each in direction:
                new_i = i+ each[0]
                new_j = j+each[1]
                if new_i>=0 and new_i<self.rowM and new_j>=0 and new_j<self.colM and self.matrix[new_i][new_j]==0:
                    self.matrix[i][j]=1
                    self.dfs(new_i,new_j)
    def regionsBySlashes(self, grid: List[str]) -> int:
        row = len(grid)
        col = len(grid[0])
        self.matrix = [[0]*(row*3) for i in range(row*3)]
        for i in range(row):
            for j in range(row):
                if grid[i][j]=="/":
                    self.matrix[i*3][j*3+2]=1
                    self.matrix[i*3+1][j*3+1]=1
                    self.matrix[i*3+2][j*3]=1
                elif grid[i][j]=="\\":
                    self.matrix[i*3][j*3]=1
                    self.matrix[i*3+1][j*3+1]=1
                    self.matrix[i*3+2][j*3+2]=1
        count=0
        self.rowM= len(self.matrix)
        self.colM = len(self.matrix[0])
        for i in range(self.rowM):
            for j in range(self.colM):
                if self.matrix[i][j]==0:
                    self.dfs(i,j)
                    count+=1

                    
        return count 
