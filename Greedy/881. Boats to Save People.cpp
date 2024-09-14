/*
https://leetcode.com/problems/boats-to-save-people/description/
mik-video:
https://youtu.be/UsQzOL6r0HY?list=PLpIkg8OmuX-J8_n8Vy9P9I3KvyDcPMzRU
  */
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(),people.end());
        int i=0;
        int j = people.size()-1;
        int boat=0;
        while(i<=j){
            if(people[i]+people[j]<=limit){
                i++;j--;
            }
            else{
                j--;
            }
            boat++;
        }
        return boat;
    }
};
