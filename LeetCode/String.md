###### [最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)

```c++
string longestPalindrome(string s) {
    string res;
    for (int i = 0; i < s.size(); i++) {
        // 以 s[i] 为中心的最长回文子串
        string s1 = palindrome(s, i, i);
        // 以 s[i] 和 s[i+1] 为中心的最长回文子串
        string s2 = palindrome(s, i, i + 1);
        res = res.size() > s1.size() ? res : s1;
        res = res.size() > s2.size() ? res : s2;
    }
    return res;
}
string palindrome(string& s, int l, int r) {
    while (l >= 0 && r < s.size() && s[l] == s[r]) {
        l--; r++;
    }
    return s.substr(l + 1, r - l - 1);
}
```

###### [两个字符串的删除操作](https://leetcode-cn.com/problems/delete-operation-for-two-strings/)

```c++
int minDistance(string word1, string word2) {
    int n1 = word1.length(), n2 = word2.length();
    vector<vector<int>> dp(n1 + 1, vector<int>(n2 + 1, 0));
    for (int i = 1; i <= n1; i++) {
        for (int j = 1; j <= n2; j++) {
            if (word1[i - 1] == word2[j - 1])
                dp[i][j] = dp[i - 1][j - 1] +  1;
            else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    return n1 + n2 - dp[n1][n2] * 2;
}
```

###### [两个字符串的最小ASCII删除和](https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/)

```c++

```

