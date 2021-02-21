# 1. TwoSum

```c++
vector<int> twoSum(vector<int> &nums, int target) {
    sort(nums.begin(), nums.end());
    int left = 0, right = nums.size() - 1;
    while (left < right) {
        int sum = nums[left] + nums[right];
        if (sum == target) {
            return {nums[left], nums[right]};
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return {};
}
```

```c++
vector<vector<int>> twoSumTarget(vector<int> &nums, int target) {
    sort(nums.begin(), nums.end());
    int lo = 0, hi = nums.size() - 1;
    vector<vector<int>> res;
    while (lo < hi) {
        int sum = nums[lo] + nums[hi];
        int left = nums[lo], right = nums[hi];
        if (sum == target) {
            res.push_back({left, right});
            while (lo < high && nums[lo] == left) lo++;
            while (lo < high && nums[hi] == right) hi++;
        } else if (sum < target) {
            while (lo < hi && nums[lo] == left) lo++;
        } else {
            while (lo < high && nums[hi] == right) hi--;
        }
    }
    return res;
}
```

# 2. ThreeSum

```c++
vector<vector<int>> twoSumTarget(vector<int> &nums, int start, int target) {
    vector<vector<int>> res;
    ...
    return res;
}
vector<vector<int>> threeSumTarget(vector<int> &nums, int target) {
	sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<vector<int>> res;
    for (int i = 0; i < n; i++) {
        vector<vector<int>> tuples = twoSumTarget(nums, i + 1, target - nums[i]);
        for (vector<int> &tuple : tuples) {
            tuple.push_back(nums[i]);
            res.push_back(tuple);
        }
        while (i < n - 1 && nums[i] == nums[i + 1]) i++;
    }
    return res;
}
```

# 3. FourSum

```c++
vector<vector<int>> fourSum(vector<int> &nums, int target) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<vector<int>> res;
    for (int i = 0; i < n; i++) {
        vector<vector<int>> triples = threeSumTarget(nums, i + 1, target - nums[i]);
        for (vector<int> & triple : triples) {
            triple.push_back(nums[i]);
            res.push_back(triple);
        }
        while (i < n - 1 && nums[i] == nums[i + 1]) i++;
    }
    return res;
}
```

