# 1. 快排

## 1.1  二路快排

```c++
void partation(vector<int> &data, int left, int right) {
    if (left >= right) return;
    int piovet = data[left];
    int i = left;
    int j = right;
    while (i < j) {
        while (i < j && data[j] >= piovet) j--;
        data[i] = data[j];
        while (i < j && data[i] <= piovet) i++;
        data[j] = data[i];
    }
    data[i] = piovet;
    partation(data, left, i-1);
    partation(data, i+1, right);
}
```

## 1.2 三路快排

```c++
void threeQuickSort(int nums[], int low, int high) {
    if (low >= high) return;
    int lt = low, mid = low + 1, gt = high;
    int temp = nums[low];
    while (mid <= gt) {
        if (nums[mid] == temp) mid++;
        else if(nums[mid] < temp) {
            swap(nums[mid], nums[lt]);
            mid++;lt++;
        } else {
            swap(nums[gt], nums[mid]);
            gt--;
        }
    }
    quickSort(nums, low, lt - 1);
    quickSort(nums, gt + 1, high);
}
```

## 1.3 应用

### 1.3.1 Kth Largest Element in an Array

```c++
int findKth(vector<int> a, int n, int K) {
        return quickSort(a, 0, n - 1, K);
    }
int quickSort(vector<int> &a, int left, int right, int k) {
    int temp = a[left];
    int i = left, j = right;
    while (i < j) {
        while (i < j && a[j] <= temp) j--;
        a[i] = a[j];
        while (i < j && a[i] >= temp) i++;
        a[j] = a[i];
    }
    a[i] = temp;
    if ((i + 1) == k) {
        return temp;
    } else if ((i + 1) < k) {
        return quickSort(a, i + 1, right, k);
    } else {
        return quickSort(a, left, i - 1, k);
    }
}
```

### 1.3.2 荷兰旗

```c++

```

# 2. 归并排序

```c++
void mergeSort(vector<int> &nums, int l, int r, vector<int> &temp) {
    if (l + 1 >= r) return;
    int mid = l + (r - l) / 2;
    mergeSort(nums, l, mid, temp);
    mergeSort(nums, mid, r, temp);
    int p = l, q = mid, i = l;
    while (p < m || q < r) {
        if (q >= r || )
    }
}
```

# 3. 桶排序

## 2.1 Top K Frequent Elements

```c++
vector<int> topKFrequent(vector<int> &nums, int k) {
    unordered_map<int, int> counts;
    int max_count = 0;
    for (const int &num : nums) max_count = max(maxcount, ++counts[num]);
    vector<vector<int>> buckets(max_count + 1);
    for (const int &p : counts) buckets[p.second].push_back(p.first);
    vector<int> ans;
    for (int i = max_count; i >= 0 && ans.size() < k; i--) {
        for (const int &num : buckets[i]) {
            ans.push_back(num);
            if (ans.size() == k)
                break;
        }
    }
    return ans;
}
```

# 堆排序

```c++

```
