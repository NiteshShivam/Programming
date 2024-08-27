/*
https://www.geeksforgeeks.org/problems/search-pattern0205/1
mik video
https://youtu.be/qases-9gOpk

  */
class Solution
{
    public:
    void compute(string &pat,vector<int> &LPS,int M){
        int length=0;
        int i=1;
        while(i<M){
            if(pat[i]==pat[length]){
                length++;
                LPS[i]=length;
                i++;
            }
            else{
                if(length!=0)
                length = LPS[length-1];
                else
                { 
                    LPS[i]=0;
                    // it's already zerp
                  i++;
                }
            }
        }
    }
        vector <int> search(string pat, string txt)
        {
            int N = txt.size();
            int M = pat.length();
            vector<int> result;
            
            vector<int> LPS(M,0);
            compute(pat,LPS,M);
            
            int i=0;
            int j=0;
            while(i<N){
                if(txt[i]==pat[j]){
                    i+=1;
                    j+=1;
                }
                if(j==M){
                    
                    result.push_back(i-M+1);
                    j = LPS[j-1];
                }
                else if(txt[i]!=pat[j]){
                    if(j!=0){
                        j=LPS[j-1];
                        
                    }
                    else{
                        i+=1;
                    }
                    
                }
                    
               
                
                
            }
        return result;
        }
     
};
