'''
https://leetcode.com/problems/rank-transform-of-an-array/description/

'''
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        tempA = sorted(arr)
        result = []
        length = len(arr)
        mp = {}
        for i in tempA:
            if i not in mp:
                mp[i]=len(mp)+1
        for i in arr:
            result.append(mp[i])
        return result

# c++
====================================
class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<int> A (arr);
        sort(A.begin(),A.end());
        unordered_map<int,int> st;
        for(int i=0;i<A.size();i++){
            if(st.find(A[i])==st.end()){
                st[A[i]]=st.size()+1;
            }
        }
        vector<int>result;
        for(const auto &num:arr){
            result.push_back(st[num]);
        }
        return result;
    }
};
