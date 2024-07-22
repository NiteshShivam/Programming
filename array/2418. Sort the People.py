'''
https://leetcode.com/problems/sort-the-people/description/
'''
import heapq
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        space = []
        length = len(names)
        for i in range(length):
            space.append((heights[i],names[i]))
        heapq._heapify_max(space)
        result = []
        while space:
            top = heapq._heappop_max(space)
            result.append(top[1])
        return result
        
