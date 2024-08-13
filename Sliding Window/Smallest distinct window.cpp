// https://www.geeksforgeeks.org/problems/smallest-distant-window3132/1
class Solution{
    public:
    int findSubString(string str)
    {
        int result=INT_MAX;
        vector<int> space(256,0);
        int unique=0;
        
        for(int right=0;right<str.size();right++){
            int index = str[right];
            space[index]++;
            if(space[index]==1){
                unique++;
            }
        }
        for(int i =0;i<256;i++){
            space[i]=0;
        }
        
        int left=0;
        int current=0;
        for(int right=0;right<str.size();right++){
            space[str[right]]+=1;
            if(space[str[right]]==1){
                current+=1;
            }
            while(current==unique){
                space[str[left]]--;
                if(space[str[left]]==0){
                    current--;
                }
                result = min(result,right-left+1);
                left++;
            }
        }
        
        return result;
    }
};
