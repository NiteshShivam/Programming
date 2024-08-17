'''
Given an array nums[] of size n, construct a Product Array P (of same size n)
such that P[i] is equal to the product of all the elements of nums except nums[i].

https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1
'''
class Solution:
    def productExceptSelf(self, nums, n):
        start = []
        last = []
        current =1
        end = 1
        j=-1
        if n==1:
            return [1]
        for num in nums:
            current = current*num
            start.append(current)
            end= end*nums[j]
            last.append(end)
            j-=1
        last = last[::-1]
        result =[]
        for i in range(n):
            if i==0 and i+1<n:
                result.append(last[i+1])
            elif i==n-1 and i-1>=0:
                result.append(start[i-1])
            else:
                result.append(start[i-1]*last[i+1])
        return result
        
        
# cpp
=========================
class Solution {
  public:
    // nums: given vector
    // return the Product vector P that hold product except self at each index
    vector<long long int> productExceptSelf(vector<long long int>& nums) {
        int length = nums.size();
        vector<long long int> start(length,1);
        vector<long long int>end(length,1);
        vector<long long int>result;
        int j=length-1;
        long long int a=1;
        long long int b=1;
        for(int i=1;i<length;i++){
            a = a*nums[i-1];
            start[i]=a;
            b = b*nums[j];
            end[j-1]=b;
            j-=1;
        }
        
        for(int i=0;i<length;i++){
        
            result.push_back(start[i]*end[i]);
        }
        return result;
    }
};
