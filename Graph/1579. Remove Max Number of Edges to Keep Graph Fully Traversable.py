'''
https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/
'''

'''Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional
edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges,
the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, 
they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 '''

class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0]*(n+1)
        self.components = n
    def Union(self,x,y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        if x_parent==y_parent:
            return
        if self.rank[x_parent]>self.rank[y_parent]:
            self.parent[y_parent]=x_parent
        elif self.rank[x_parent]<self.rank[y_parent]:
            self.parent[x_parent]=y_parent
        else:
            self.rank[y_parent]=self.rank[y_parent]+1
            self.parent[x_parent]=y_parent
        self.components -=1
    def find(self,i):
        if i==self.parent[i]:
            return i
        self.parent[i] =  self.find(self.parent[i])
        return self.parent[i]
    def singleCom(self):
        return self.components==1
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        Alice = DSU(n)
        Bob = DSU(n)
        edges.sort(key=lambda x :x[0],reverse=True)
        edgeCount = 0
        for t,u,v in edges:
            if t==3:
                addEgeKiyakya = False
                if Alice.find(u)!=Alice.find(v):
                    Alice.Union(u,v)
                    addEgeKiyakya = True
                if Bob.find(u)!=Bob.find(v):
                    Bob.Union(u,v)
                    addEgeKiyakya = True
                if addEgeKiyakya:
                    edgeCount +=1
            elif t==2:
                if Bob.find(u)!=Bob.find(v):
                    Bob.Union(u,v)
                    edgeCount+=1
            else:
                if Alice.find(u)!=Alice.find(v):
                    Alice.Union(u,v)
                    edgeCount+=1 
        if Alice.singleCom() and Bob.singleCom():
            return len(edges)-edgeCount
        return -1
            
