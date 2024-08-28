/*
https://leetcode.com/problems/count-sub-islands/description/
mik video:
https://youtu.be/OeaEOoM-g98
*/
class Solution {
public:
    bool checkIsSubIsland(vector<vector<int>>& grid1,vector<vector<int>>& grid2,int i,int j){
        if(i<0 || i>=grid2.size() || j<0 || j>=grid2[0].size()){
            return true;
        }
        if(grid2[i][j]!=1){
            return true;
        }
        grid2[i][j]=-1;
        
        bool result = (grid1[i][j]==1);
        result = result & checkIsSubIsland(grid1,grid2,i-1,j);
        result = result  & checkIsSubIsland(grid1,grid2,i+1,j);
        result = result  & checkIsSubIsland(grid1,grid2,i,j-1);
        result = result  & checkIsSubIsland(grid1,grid2,i,j+1);
        return result;
    }
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int m = grid2.size();
        int n = grid2[0].size();
        int substring=0;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++){
                if(grid2[i][j]==1 && checkIsSubIsland(grid1,grid2,i,j)){
                    substring++;
                }
            }
        }
        return substring;
    }
};

==========================================================


  from typing import List

class Solution:
    
    def checkIsSubIsland(self, grid1: List[List[int]], grid2: List[List[int]], i: int, j: int) -> bool:
        # Boundary check
        if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]):
            return True
        
        # If the cell is not part of an island in grid2
        if grid2[i][j] != 1:
            return True
        
        # Mark the cell as visited
        grid2[i][j] = -1
        
        # Initialize the result based on the current cell's correspondence in grid1
        result = (grid1[i][j] == 1)
        
        # Recursively check all four directions
        // note & it is bitwise 
        result = result & self.checkIsSubIsland(grid1, grid2, i - 1, j)
        result = result & self.checkIsSubIsland(grid1, grid2, i + 1, j)
        result = result & self.checkIsSubIsland(grid1, grid2, i, j - 1)
        result = result & self.checkIsSubIsland(grid1, grid2, i, j + 1)
        
        return result
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                # Start checking for sub-islands only if the cell is part of an island in grid2
                if grid2[i][j] == 1 and self.checkIsSubIsland(grid1, grid2, i, j):
                    count += 1
        
        return count

=========================================
from typing import List

class Solution:
    
    def checkIsSubIsland(self, grid1: List[List[int]], grid2: List[List[int]], i: int, j: int) -> bool:
        # Boundary check
        if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]):
            return True
        
        # If the cell is not part of an island in grid2
        if grid2[i][j] != 1:
            return True
        
        # Mark the cell as visited
        grid2[i][j] = -1
        
        # Initialize the result based on the current cell's correspondence in grid1
        result = (grid1[i][j] == 1)
        
        # Recursively check all four directions
        l =  self.checkIsSubIsland(grid1, grid2, i - 1, j)
        r =   self.checkIsSubIsland(grid1, grid2, i + 1, j)
        d = self.checkIsSubIsland(grid1, grid2, i, j - 1)
        u = self.checkIsSubIsland(grid1, grid2, i, j + 1)
        
        return l and r and d and u and result
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                # Start checking for sub-islands only if the cell is part of an island in grid2
                if grid2[i][j] == 1 and self.checkIsSubIsland(grid1, grid2, i, j):
                    count += 1
        
        return count







// bfs python
====================================================
from typing import List
from collections import deque
class Solution:
    
    def checkIsSubIsland(self, grid1: List[List[int]], grid2: List[List[int]], i: int, j: int) -> bool:
        q = deque()
        q.append((i,j))
        m = len(grid1)
        n = len(grid1[0])
        direction = [(-1,0),(0,1),(0,-1),(1,0)]

        while q:
            t =q.popleft()
            grid2[t[0]][t[1]]=0
            result =  grid1[t[0]][t[1]]==1
            for each in direction:
                new_i = t[0]+each[0]
                new_j = t[1]+each[1]
                if 0<=new_i<m and 0<=new_j<n and grid2[new_i][new_j]==1:
                    result = result & self.checkIsSubIsland(grid1,grid2,new_i,new_j)
            return result
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
               
                if grid2[i][j] == 1 and self.checkIsSubIsland(grid1, grid2, i, j):
                    count += 1
        
        return count


    =====================================================
    class Solution {
public:
    bool checkIsSubIsland(vector<vector<int>>& grid1,vector<vector<int>>& grid2,int i,int j){
        int m = grid1.size();
        int n = grid1[0].size();
        bool result=true;
        queue<pair<int,int>> q;
        q.push({i,j});
        vector<pair<int,int>> direction = {{0,1},{0,-1},{-1,0},{1,0}};
        grid2[i][j]=0;
        while(!q.empty()){
            auto[x,y]=q.front();
            q.pop();
            
            if(grid1[x][y]!=1){
                result = false;
            }
            for(int k=0;k<4;k++){
                int new_i = x+ direction[k].first;
                int new_j = y+direction[k].second;
                if(new_i>=0 && new_i<m && new_j>=0 && new_j<n && grid2[new_i][new_j]==1){
                    q.push({new_i,new_j});
                    grid2[new_i][new_j]=0;

                   
                }
            }
        }
        return result;
    }
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int m = grid2.size();
        int n = grid2[0].size();
        int substring=0;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++){
                if(grid2[i][j]==1 && checkIsSubIsland(grid1,grid2,i,j)){
                    substring++;
                }
            }
        }
        return substring;
    }
};

