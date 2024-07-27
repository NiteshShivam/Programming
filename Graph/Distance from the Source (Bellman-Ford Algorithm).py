'''
https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1
https://www.youtube.com/watch?v=5yTkgeTqKK0
'''
class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        maxV = 10**8
        distance= [maxV]*V
        distance[S]=0
        for i in range(V-1):
            for each in edges:
                u = each[0]
                v = each[1]
                w = each[2]
                if distance[u]!=maxV and distance[u]+w<distance[v]:
                    distance[v]=distance[u]+w
        for each in edges:
            u = each[0]
            v = each[1]
            w = each[2]
            if distance[u]!=maxV and distance[u]+w<distance[v]:
                return [-1]
        return distance
