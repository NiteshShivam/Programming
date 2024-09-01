/*
https://leetcode.com/problems/convert-1d-array-into-2d-array/description/

mik-video
https://youtu.be/4jQErv8WK6o
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




=================================================

 class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        int total = m*n;
        if(total!=original.size()){
            return {};
        }
        int i;
        int j;
        vector<vector<int>>result(m,vector<int>(n));
        
        for(int k=0;k<original.size();k++){
            i=k/n;
            j=k%n;
            result[i][j]=original[k];

        }
        return result;
    }
};
