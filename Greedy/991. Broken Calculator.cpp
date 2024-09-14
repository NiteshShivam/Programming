/*
https://leetcode.com/problems/broken-calculator/description/
mik-video:
https://youtu.be/svM2wbyMT4g?list=PLpIkg8OmuX-J8_n8Vy9P9I3KvyDcPMzRU
  */
class Solution {
public:
    int brokenCalc(int startValue, int target) {
        if(startValue==target){
            return 0;
        }
        if(startValue>target){
            return startValue-target;
        }
        if(target%2==0){
            return 1+brokenCalc(startValue,target/2);
        }
        else{
            return 1+brokenCalc(startValue,target+1);
        }
    }
};
