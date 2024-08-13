/*
https://youtu.be/bfKwLi6jtDk
https://leetcode.com/problems/combination-sum-ii/description/
  */
class Solution {
public:
    vector<vector<int>> result;
    int target;
    void solve(vector<int>& candidates,int idx,int currentSum,vector<int> currentArray){
        if(currentSum==target){
            result.push_back(currentArray);
            return;
        }
        if(idx>=candidates.size() || currentSum>target)
        {
            return;
        }
        
        for(int i=idx;i<candidates.size();i++){
            if(i>idx && candidates[i]==candidates[i-1] ){
                continue;
            }
        
        currentArray.push_back(candidates[i]);
        solve(candidates,i+1,currentSum+candidates[i],currentArray);
        currentArray.pop_back();
        // solve(candidates,i+1,currentSum,currentArray);
        }

    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> r;
        this->target=target;
        sort(candidates.begin(),candidates.end());
        solve(candidates,0,0,r);
        return result;
        
    }
};
