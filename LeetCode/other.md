###### [只出现一次的数字](https://leetcode-cn.com/problems/single-number/)

```c++
int singleNumber(vector<int>& nums) {
    int res = 0;
    for (int i = 0, n = nums.size(); i < n; i++) res ^= nums[i];
    return res;
}
```

