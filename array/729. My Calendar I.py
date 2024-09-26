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

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
