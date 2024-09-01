/*
https://leetcode.com/problems/convert-1d-array-into-2d-array/description/
  */
class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        int total = m*n;
        if(total!=original.size()){
            return {};
        }
        int j=0;
        vector<vector<int>>result;
        vector<int>temp;
        for(int i=0;i<original.size();i++){
            
            temp.push_back(original[i]);
            j++;
            if(j==n){
                j=0;
                result.push_back(temp);
                temp.clear();
            }


        }
        return result;
    }
};
