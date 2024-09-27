'''
https://leetcode.com/problems/my-calendar-i/description/
mik-video:
https://youtu.be/45hKBSytI2E
'''
class MyCalendar:

    def __init__(self):
        self.s = []

    def book(self, start: int, end: int) -> bool:
        for each in self.s:
            if start<each[1] and each[0]<end:
                return False
               
        self.s.append([start,end])
        return True



=============================

class MyCalendar {
public:
    set<pair<int,int>> st;
    MyCalendar() {
        
        
    }
    
    bool book(int start, int end) {
        auto it = st.lower_bound({start,end});
    
    if(it!=st.end() && it->first<end){
        return false;
    }
    if(it!=st.begin()){
        auto prevI = prev(it);
        if(start<prevI->second){
            return false;
        }
    } 
    st.insert({start,end});
    return true;
    }
};

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
