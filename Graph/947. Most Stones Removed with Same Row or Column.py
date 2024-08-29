'''
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

mik-video

https://youtu.be/ZsGTpXm966E

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
