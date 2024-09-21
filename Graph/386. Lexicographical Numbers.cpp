/*
https://leetcode.com/problems/lexicographical-numbers/description/
  */
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> result;
        
        for(int i=1;i<=n;i++){
            
            result.push_back(i);
        }
        sort(result.begin(),result.end(),[](int x,int y){
            string s1 = to_string(x);
            string s2 = to_string(y);
            return s1<s2;
        });
        return result;
    }
};
