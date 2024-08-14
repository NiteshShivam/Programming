/*
https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
https://youtu.be/hx8Ssz_3XSs
  */
class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        int first = *min_element(nums.begin(),nums.end());
        int last = *max_element(nums.begin(),nums.end());
        vector<int>result(last-first+1,0);
        int answer=0;
        for(int i =0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                answer = abs(nums[i]-nums[j]);
                result[answer]++;
            }
        }
        answer=0;
        for(int i=0;i<result.size();i++){
            answer+=result[i];
            if(answer>=k){
                return i;
            }
        }
        return answer;
    }
    
};
