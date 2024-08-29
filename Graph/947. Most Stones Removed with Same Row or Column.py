'''
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

mik-video

dfs
https://youtu.be/ZsGTpXm966E

dsu
https://youtu.be/cmqIeBFx01w

'''
class Solution:
    def dfs(self,stones,index):
        self.visited[index]=True
        for i in range(self.n):
            if (self.visited[i]==False) and(stones[i][0]==stones[index][0] or stones[i][1]==stones[index][1]):
                self.dfs(stones,i)
    def removeStones(self, stones: List[List[int]]) -> int:
        self.n = len(stones)
        self.visited = [False]*self.n
        group=0
        for i in range(self.n):
            if self.visited[i]==False:
                self.dfs(stones,i)
                group+=1
        return self.n -group



# cpp
=========================

class Solution {
public:
    void dfs(vector<bool>& visited,vector<vector<int>>& stones,int index){
        visited[index]=true;
        for(int i=0;i<stones.size();i++){
            if((visited[i]==false)&&
            
            (stones[index][0]==stones[i][0] || stones[index][1]==stones[i][1])){
                dfs(visited,stones,i);
            }
        }
    }
    int removeStones(vector<vector<int>>& stones) {
        int n = stones.size();
        vector<bool> visited(n,false);
        int group=0;
        for(int i=0;i<n;i++){
            if(visited[i]==false){
                dfs(visited,stones,i);
                group+=1;
            }
        }
        return n-group;
    }
};




# python dsu
======================================

class Solution:
    def find(self,i):
        if i==self.parent[i]:
            return i
        self.parent[i] =self.find(self.parent[i])
        return self.parent[i]
    def union(self,x,y):
        parentx = self.find(x)
        parenty = self.find(y)
        if parentx==parenty:
            return
        if self.rank[parentx]>self.rank[parenty]:
            self.parent[parenty]=parentx
        elif self.rank[parentx]<self.rank[parenty]:
            self.parent[parentx]=parenty
        else:
            self.rank[parenty] = self.rank[parenty]+1
            self.parent[parentx]=parenty
    def removeStones(self, stones: List[List[int]]) -> int:
        self.length = len(stones)
        self.rank = [1]*self.length
        self.parent = [i for i in range(self.length)]

        for i in range(self.length):
            for j in range(i+1,self.length):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    self.union(i,j)
        group = 0
        for i in range(self.length):
            if self.parent[i]==i:
                group+=1
        return self.length-group
