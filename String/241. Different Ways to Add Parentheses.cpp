/*
https://leetcode.com/problems/different-ways-to-add-parentheses/description/
mik-video:
https://youtu.be/vWW67t_a--8
  */
class Solution {
public:
    vector<int> solve(string s){
        vector<int> result;
        for(int i=0;i<s.length();i++){
            if(s[i]=='+' || s[i]=='-' || s[i]=='*'){
                vector<int> left = solve(s.substr(0,i));
                vector<int> right = solve(s.substr(i+1));
                for(int &x:left){
                    for(int &y:right){
                        if(s[i]=='+'){
                            result.push_back(x+y);
                        }
                        else if(s[i]=='-'){
                            result.push_back(x-y);
                        }
    
                        else{
                            result.push_back(x*y);
                        }
                    }
                }
            }
            
        }
        if(result.empty()){
            result.push_back(stoi(s));
        }
        return result;
    }
    vector<int> diffWaysToCompute(string expression) {
        return solve(expression);
    }
};
