###### [跳跃游戏](https://leetcode-cn.com/problems/jump-game/)

```cc
bool canJump(vector<int>& nums) {
    int k = 0;
    for (int i = 0, n = nums.size(); i < n; i++) {
        if (i > k) return false;
        k = max(k, i + nums[i]);
    }
    return true;
}
```

