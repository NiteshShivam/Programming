'''
https://leetcode.com/problems/non-decreasing-subsequences/description/
mik-video:
https://youtu.be/8dfPwZvvDc8?list=PLpIkg8OmuX-KJPC18SGiRUzJQAYo839ox

'''
class Solution:
    def solve(self,index,curr):
        if len(curr)>=2:
            self.result.append(curr[:])
        s = set()
        for i in range(index,self.length):
            if (not curr or curr[-1]<=self.nums[i]) and self.nums[i] not in s:
                curr.append(self.nums[i])
                self.solve(i+1,curr)
                curr.pop()
                s.add(self.nums[i])
        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        self.result = []
        self.nums = nums
        self.length = len(nums)
        self.solve(0,[])
        return self.result


# cpp
==============================

class Solution {
public:
    int n;
    void solve(int index,vector<int>&curr,vector<vector<int>>&result,vector<int>& nums){
        if(curr.size()>=2){
            result.push_back(curr);
        }
        unordered_set<int> st;
        for(int i=index;i<n;i++){
            if((curr.size()==0 or curr.back()<=nums[i]) && st.find(nums[i])==st.end()){
                curr.push_back(nums[i]);
                solve(i+1,curr,result,nums);
                st.insert(nums[i]);
                curr.pop_back();
            }
        }
    }

    vector<vector<int>> findSubsequences(vector<int>& nums) {
    n = nums.size();
    vector<int>curr;
    vector<vector<int>> result;
    solve(0,curr,result,nums);
    return result;
    }
};
