/*
https://leetcode.com/problems/determine-if-two-strings-are-close/description/
mik-video:

https://youtu.be/KbdCp4nUDiQ?list=PLpIkg8OmuX-KRHVXwqSixQC9UE6DsHnWa

  */
class Solution {
public:
    bool closeStrings(string word1, string word2) {
        int n1 = word1.size();
        int n2 = word2.size();
        if(n1!=n2){
            return false;
        }
        vector<int> first(26,0);
        vector<int> second(26,0);
        for(int i=0;i<n1;i++){
            int temp = word1[i]-'a';
            first[temp]++;
            int temp2 = word2[i]-'a';
            second[temp2]++;
        }
        
        for(int i=0;i<26;i++){
            if((first[i]!=0 && second[i]==0)||(first[i]==0 && second[i]!=0) )
            {
                return false;
            }
        }
        sort(first.begin(),first.end());
        sort(second.begin(),second.end());
        
        for(int i=0;i<26;i++){
            if(first[i]!=second[i]){
                return false;
            }
        }
        return true;
    }
};
