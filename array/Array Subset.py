'''
  https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1
'''
def isSubset(a1, a2,n,m):
    hashM = {}

    def solve(a):
        
        for each in a:
            hashM[each] = hashM.get(each, 0) + 1

    def check(a):
        
        for each in a:
            if each not in hashM or hashM[each] <= 0:
                return "No"
            hashM[each] -= 1
        return "Yes"
    
    
    solve(a1)
    return check(a2)
    
