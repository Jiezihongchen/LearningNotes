###### 01背包

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

###### 子集背包

```c++

```

###### 完全背包

```c++

```

###### [打家劫舍](https://leetcode-cn.com/problems/house-robber/)

```c++

```

###### [打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/)

```c++

```

###### [打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii/)

```c++

```

###### [零钱兑换](https://leetcode-cn.com/problems/coin-change/)

```

```

###### [零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2/)

```c++

```

###### [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)

```c++
int maxSubArray(vector<int>& nums) {
    if (nums.size() == 0) return 0;
    int ans = nums[0];
    int siz = nums.size();
    int *p = new int[siz + 1];
    p[0] = nums[0];
    for (int i = 1; i < siz; i++) {
        p[i] = max(nums[i], p[i - 1] + nums[i]);
        ans = max(ans, p[i]);
    }
    return ans;
}
```

###### [最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)

```c++
int longestCommonSubsequence(string text1, string text2) {
    int dp[1024][1024] = {0};
    int len1 = text1.length(), len2 = text2.length();
    for (int i = 1; i <= len1; i++) {
        for (int j = 1; j <= len2; j++) {
            if (text1[i - 1] == text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[len1][len2];
}
```

###### [最长回文子序列](https://leetcode-cn.com/problems/longest-palindromic-subsequence/)

```c++
int longestPalindromeSubseq(string s) {
    int n = s.length();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) dp[i][i] = 1;
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i + 1; j < n; j++) {
            if (s[i] == s[j]) {
                dp[i][j] = dp[i + 1][j - 1] + 2;
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[0][n - 1];
}
```

###### [最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)

```c++
int lengthOfLIS(vector<int>& nums) {
    int n = nums.size(), cnt = 1;
    vector<int> dp(n, 1);
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j])
                dp[i] = max(dp[i], dp[j] + 1);
        }
        cnt = max(cnt, dp[i]);
    }
    return cnt;
}
```

###### [买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

```c++

```

###### [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

```c++

```

###### [买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)

```c++

```

###### [买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)

```c++

```

###### [最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

```c++

```

###### [买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

```c++

```

###### [鸡蛋掉落](https://leetcode-cn.com/problems/super-egg-drop/)

```c++

```

