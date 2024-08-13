/*
https://www.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1
  */
class Solution{
    public:
    int longestUniqueSubsttr(string S){
        int result=0;
        int left=0;
        vector<int> space(26,0);
        for(int right=0;right<S.size();right++){
            int index = S[right]-'a';
            space[index]+=1;
            while(space[index]>1){
                int tempIndex = S[left]-'a';
                space[tempIndex]-=1;
                left++;
            }
            result = max(result,right-left+1);
        }
        return result;
    }
};
