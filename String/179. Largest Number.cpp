/*
https://leetcode.com/problems/largest-number/description/
mik-video:
https://youtu.be/oJyl4fbfpM0
  */
class Solution {
public:
    string largestNumber(vector<int>& nums) {
     vector<string> r;
     int n=nums.size();
     auto comparator=[](string &s1,string &s2){
        return s1+s2>s2+s1;};
     for(int i=0;i<n;i++){
        r.push_back(to_string(nums[i]));
     }   
     sort(begin(r),end(r),comparator);
     string result="";
     if(r[0]=="0"){
        return "0";
     }
     for(string &s:r){
        result = result+s;
     }
    
     return result;
    }
};
