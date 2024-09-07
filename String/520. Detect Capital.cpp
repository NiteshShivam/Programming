/*
https://leetcode.com/problems/detect-capital/description/
mik-video:
https://youtu.be/DrVLI_NXaic?list=PLpIkg8OmuX-KRHVXwqSixQC9UE6DsHnWa
  */
class Solution {
public:
    bool allCapital(string word){
        int n = word.length();
        for(int i =0;i<n;i++){
            int value = word[i]-'A';
            if(value>=0 && value<=26){
                continue;
            }
            else{
                return false;
            }
        }
        return true;
    }
    bool allSmall(string word){
        int n = word.length();
        for(int i =0;i<n;i++){
            int value = word[i]-'a';
            if(value>=0 && value<=26){
                continue;
            }
            else{
                return false;
            }
        }
        return true;
    }
    bool detectCapitalUse(string word) {
        return allCapital(word)||allSmall(word)||allSmall(word.substr(1));
    }
};
