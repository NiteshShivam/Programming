'''

https://youtu.be/pOtAvGIW8kQ
https://leetcode.com/problems/filling-bookcase-shelves/description
'''
class Solution:
    def solve(self,index,remainingWidth,maxHeight):
        if index>=self.booklength:
            return maxHeight
        if self.dp[index][remainingWidth]!=-1:
            return self.dp[index][remainingWidth]
        bookH = self.books[index][1]
        bookW = self.books[index][0]
        k = float('inf')
        if bookW<=remainingWidth:
            k = self.solve(index+1,remainingWidth-bookW,max(maxHeight,bookH))
        result = maxHeight + self.solve(index+1,self.shelfWidth-bookW,bookH)
        self.dp[index][remainingWidth] = min(k,result)
        return self.dp[index][remainingWidth]
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        self.books = books
        self.booklength = len(books)
        self.shelfWidth =shelfWidth
        self.dp = [[-1]*1001 for _ in range(1001)]
        remainingWidth = shelfWidth
        return self.solve(0,remainingWidth,0)
