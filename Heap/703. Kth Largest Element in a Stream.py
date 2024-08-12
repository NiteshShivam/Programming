'''

https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
https://youtu.be/3Bge5OCcXUk
'''
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = []
        self.k = k
        for i in range(len(nums)):
            heapq.heappush(self.hp,nums[i])
            if len(self.hp)>k:
                heapq.heappop(self.hp)
        return None

    def add(self, val: int) -> int:
        heapq.heappush(self.hp,val)
        if len(self.hp)>self.k:
            heapq.heappop(self.hp)
        return self.hp[0]

