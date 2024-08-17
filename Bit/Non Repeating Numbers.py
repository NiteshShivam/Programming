'''
https://www.youtube.com/watch?v=pnx5JA9LNM4
https://www.geeksforgeeks.org/problems/finding-the-numbers0215/1
'''
class Solution:
	def singleNumber(self, nums):
		result =0
		for each in nums:
		    result = result^each
		number = result & -result
		x = 0
		y =0
		for each in nums:
		    if each & number:
		        x = x ^each
		    else:
		        y = y ^ each
		if x>y:
		    return [y,x]
		return [x,y]



# cpp
=============================
class Solution
{
public:
    vector<int> singleNumber(vector<int> nums) 
    {
        int result=0;
        int length = nums.size();
        for(int i=0;i<length;i++){
            result = result^nums[i];
        }
        int number = result & -result;
        int x = 0;
        int y=0;
        for(int i=0;i<length;i++){
            if(nums[i]&number){
                x = x^nums[i];
            }
            else{
                y = y^nums[i];
            }
        }
        if(x>y){
            return {y,x};
        }
        return {x,y};
    }
};
