/*
https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
https://youtu.be/hx8Ssz_3XSs
  */
// python
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = nums[-1]-nums[0]
        result=0
        def sliding(nums,d):
            i=0
            j=1
            count=0
            n = len(nums)
            while j<n:
                while nums[j]-nums[i]>d:
                    i+=1
                count += j-i
                j+=1
            return count
        while left<=right:
            mid = left+(right-left)//2
            countPair = sliding(nums,mid)
            if countPair<k:
                left = mid+1
            else:
                result=mid
                right=mid-1
        return result








==========
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

=================================================
class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int>result(n*(n-1)/2);
        int idx=0;
        int answer=0;
        for(int i =0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                answer = abs(nums[i]-nums[j]);
                result[idx]=answer;
                idx++;
            }
        }
        nth_element(begin(result),begin(result)+k-1,end(result));
        return result[k-1];
    }
    
};

