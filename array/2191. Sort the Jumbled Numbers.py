'''
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
