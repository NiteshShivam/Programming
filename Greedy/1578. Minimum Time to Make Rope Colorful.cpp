/*
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/
mik-video:
https://youtu.be/_xNrzKfORNA?list=PLpIkg8OmuX-J8_n8Vy9P9I3KvyDcPMzRU
  */
class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int time=0;
        int n= colors.size();
        int prevMax =0;
        for(int i=0;i<n;i++){
            if(i>0 && colors[i]!=colors[i-1]){
                prevMax=0;
            }
            int curr = neededTime[i];
            time += min(curr,prevMax);
            prevMax = max(prevMax,curr);
            
        }
        return time;
    }
};
