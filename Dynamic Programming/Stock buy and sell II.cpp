class Solution {
  public:
  vector<vector<int>> dp; 
    int solve(vector<int>& prices, int n, int i, bool buy) {
        if (i >= n) {
            return 0;
        }
        if (dp[buy][i] != -1) {
            return dp[buy][i];
        }
        if (buy) {
            
            int take = solve(prices, n, i + 1, false) - prices[i];
            int not_take = solve(prices, n, i + 1, true);
            dp[buy][i] = max(take, not_take);
        } else {
           
            int sell = prices[i] + solve(prices, n, i + 1, true);
            int not_sell = solve(prices, n, i + 1, false);
            dp[buy][i] = max(sell, not_sell);
        }

        return dp[buy][i];
    }





// python given 

=============================
import sys
sys.setrecursionlimit(99999)
from typing import List
class Solution:
  

    def stockBuyAndSell(self, n: int, prices: List[int]) -> int:
       
        dp = [[-1] * 2 for _ in range(n)]
        def solve( i: int, buy: bool) -> int:
            if i >= n:
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
            if buy:
                take = solve(i + 1, False) - prices[i]
                not_take = solve(i + 1, True)
                dp[i][buy] = max(take, not_take)
            else:
                sell = prices[i] + solve( i + 1, True)
                not_sell = solve(i + 1, False)
                dp[i][buy] = max(sell, not_sell)
            return dp[i][buy]

        return solve(0, True)
    int stockBuyAndSell(int n, vector<int> &prices) {
        dp.resize(2, vector<int>(n, -1));
        return solve(prices, n, 0, true);
    }
};
