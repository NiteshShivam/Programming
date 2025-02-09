'''
https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/
'''

'''You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG).
The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges.
'''

#   Approach : 
class Solution:
    def __init__(self):
        self.result = []
        self.connection = []
    def topoSort(self, V, adj):
        indegree = [0]*V
        for u in range(V):
            for v in adj[u]:
                indegree[v]+=1
        q = deque()
        result = []
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
                
        while q:
            temp = q.popleft()
            result.append(temp)
            for each in adj[temp]:
                indegree[each]-=1
                if indegree[each]==0:
                    q.append(each)
        return result
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.result = [set() for i in range(n)]
        self.connection = [[] for i in range(n)]
        for each in edges:
            self.connection[each[0]].append(each[1])
        topop = self.topoSort(n,self.connection)
        for each in topop:
            for v in self.connection[each]:
                self.result[v].add(each)
                self.result[v].update(self.result[each])
        for i in range(n):
            self.result[i] = sorted(self.result[i])
        return self.result


other Approach :
class Solution:
    def __init__(self):
        self.result = []
        self.connection = []
    def dfs(self,i,parent):
        for each in self.connection[i]:
            if  not self.result[each] or self.result[each][-1]!=parent:
                self.result[each].append(parent)
                self.dfs(each,parent)
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.result = [[] for i in range(n)]
        self.connection = [[] for i in range(n)]
        for each in edges:
            self.connection[each[0]].append(each[1])
        for i in range(n):
            self.dfs(i,i)
        return self.result
       
       
