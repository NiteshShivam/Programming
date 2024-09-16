/*
https://leetcode.com/problems/minimum-time-difference/description/
mik-video:
https://youtu.be/ftCheG0m85k
  */
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        
        int n = timePoints.size();
        int result=INT_MAX;
        vector<int> space;
        for(int i=0;i<n;i++){
            int first_min = stoi(timePoints[i].substr(0,2));
            first_min = first_min*60+stoi(timePoints[i].substr(3,2));
            space.push_back(first_min);
        }
        sort(space.begin(),space.end());
        n = space.size();
        for(int i=0;i<n-1;i++){
           
            result = min(result,abs(space[i+1]-space[i]));
        }
        result = min(result,24*60-space[n-1]+space[0]);
        return result;
    }
};
