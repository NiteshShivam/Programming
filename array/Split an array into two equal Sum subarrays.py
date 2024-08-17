'''
https://www.geeksforgeeks.org/problems/split-an-array-into-two-equal-sum-subarrays/1
'''
class Solution:
    def canSplit(self, arr):
        s = sum(arr)
        current =0
        for each in arr:
            current+=each
            if s-current==current:
                return True
        return False


================================
# cpp
class Solution {
  public:
    bool canSplit(vector<int>& arr) {
        int sum=0;
        for(int i=0;i<arr.size();i++){
            sum+=arr[i];
        }
        int current=0;
        for(int i=0;i<arr.size();i++){
            current+=arr[i];
            if(sum-current==current){
                return true;
            }
        }
        return false;
    }
};
