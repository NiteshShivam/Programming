'''
https://leetcode.com/problems/path-with-maximum-probability/description/
https://youtu.be/zTM9k6jqpXI
'''
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        result = [float('-inf')]*n
        pq = []
        adj = defaultdict(list)
        i=0
        for each in edges:
            adj[each[0]].append([each[1],succProb[i]])
            adj[each[1]].append([each[0],succProb[i]])
            i+=1
        result[start_node]=1
        heapq.heappush(pq,(-1,start_node))
        while pq:
            value,node = heapq.heappop(pq)
            for each in adj[node]:
                new_node = each[0]
                prob = -(each[1])
                if value*prob>result[new_node]:
                    result[new_node] = value*prob
                    heapq.heappush(pq,(-result[new_node],new_node))
        # print(result)
        if result[end_node]==float('-inf'):
            return  0.00000
        return result[end_node]
