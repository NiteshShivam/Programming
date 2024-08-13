// https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1
//https://discuss.geeksforgeeks.org/comment/11f03968c46cdcbc8874195d9c99548e/practice
class Solution
{ long long int solve(string s, int k){
    long long ans=0;
    	int left=0;
    	vector<int> space(26,0);
    	int distinct=0;
    	for(int right=0;right<s.size();right++){
    	    int index = s[right]-'a';
    	    space[index]+=1;
    	    if(space[index]==1){
    	        distinct++;
    	    }
    	    while(distinct>k){
    	        int newIndex = s[left]-'a';
    	        space[newIndex]-=1;
    	        if(space[newIndex]==0){
    	            distinct--;
    	        }
    	        left++;
    	    }
    	    ans = ans+(right-left+1);
    	}
    	return ans;
}
  public:
    long long int substrCount (string s, int k) {
    	return solve(s,k)-solve(s,k-1);
    }
};




// python
========================
class Solution:
    def solve(self,s,k):
        left=0
        ans=0
        space = [0]*26
        distinct=0
        for right in range(len(s)):
            index = ord(s[right])-ord('a')
            space[index]+=1
            if space[index]==1:
                distinct+=1
            while(distinct>k):
                newIndex = ord(s[left])-ord('a')
                space[newIndex]-=1
                if space[newIndex]==0:
                    distinct-=1
                left+=1
            ans = ans+right-left+1
        return ans
            
    def substrCount (self,s, k):
        return self.solve(s,k)-self.solve(s,k-1)
    
