/*
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/
mik-video:
https://youtu.be/xhKpOhtqAnM
*/
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int maxNum = nums[0];
        int n=nums.size();
        for(int i=1;i<n;i++){
            maxNum = max(maxNum,nums[i]);
        }
        int result=0;
        int count =0;
        for(int i=0;i<n;i++){
            if(nums[i]==maxNum){
                count++;
            }
            else{
                result = max(count,result);
                count=0;
            }
        }
        result = max(count,result);
        return result;
    }
};
