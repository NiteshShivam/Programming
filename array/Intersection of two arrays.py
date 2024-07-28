'''
https://www.geeksforgeeks.org/problems/intersection-of-two-arrays2404/1
'''
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        a = set(a)
        result = set()
        for each in b:
            if each in a:
                result.add(each)
        return len(result)
