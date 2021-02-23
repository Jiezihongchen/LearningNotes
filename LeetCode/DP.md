# 1. 背包问题

## 1.1 01背包

```c++
int knapsack(int W, int N, vector<int>& wt, vector<int>& val) {
    vector<vector<int>> dp(N + 1, vector<int>(W + 1, 0));
    for (int i = 1; i <= N; i++) {
        for (int w = 1; w <= W; w++) {
            if (w - wt[i - 1] < 0) {
                dp[i][w] = dp[i - 1][w];
            } else {
                dp[i][w] = max(dp[i - 1][w - wt[i - 1]] + val[i - 1], dp[i - 1][w]);
            }
        }
    }
    return dp[N][W];
}
```

## 1.2 子集背包

```c++

```

## 1.3 完全背包

```c++

```

# 2. 股票买卖



# 3. 打家劫舍



# 4. 高楼扔鸡蛋

# 5. 零钱兑换

## 5.1 

[零钱兑换]: https://leetcode-cn.com/problems/coin-change/

```

```

## 5.2 

[零钱兑换II]: https://leetcode-cn.com/problems/coin-change-2/

```c++

```

