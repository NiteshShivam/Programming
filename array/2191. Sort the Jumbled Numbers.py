'''
https://www.youtube.com/watch?v=BXHWgX4UX04
https://leetcode.com/problems/sort-the-jumbled-numbers/description/
'''
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        space = {}
        for each in nums:
            st = str(each)
            result = 0
            for ch in st:
                value = mapping[int(ch)]
                result  = result*10+value
            if result not in space:
                space[result]=[]
                space[result].append(each)
            else:
                space[result].append(each)
        res = sorted(space.keys())
        result = []
        for each in res:
            for value in space[each]:
                result.append(value)
        return result



============================

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        space = []
        i = 0
        for each in nums:
            st = str(each)
            result = 0
            for ch in st:
                value = mapping[int(ch)]
                result  = result*10+value
            space.append((result,i))
            i+=1
        space.sort()
        result = []
        for each in space:
            result.append(nums[each[1]])
        return result

