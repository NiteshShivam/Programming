/*
https://leetcode.com/problems/bag-of-tokens/description/
mik-video:
https://youtu.be/LCx1WzlYgvw?list=PLpIkg8OmuX-J8_n8Vy9P9I3KvyDcPMzRU

  */
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(),tokens.end());
        int score=0;
        int i=0;
        int j=tokens.size()-1;
        int result=0;
        while(i<=j){
            if(power>=tokens[i]){
                power-=tokens[i];
                score++;
                i+=1;
            }
            else if(score>=1){
                power+=tokens[j];
                j-=1;
                score--;
            }
            else{
                break;
            }
            result = max(result,score);
        }
        return result;
    }
};
