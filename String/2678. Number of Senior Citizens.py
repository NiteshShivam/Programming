'''
https://leetcode.com/problems/number-of-senior-citizens/description/
'''
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for each in details:
            age = int(each[11:13])
            if age>60:
                result+=1
        return result
