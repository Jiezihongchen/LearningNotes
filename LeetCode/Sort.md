###### 快排

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

###### 三路快排

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

###### 归并排序

```c++
void mergeSort(vector<int> &nums, int l, int r, vector<int> &temp) {
    if (l + 1 >= r) return;
    int mid = l + (r - l) / 2;
    
    mergeSort(nums, l, mid, temp);
    mergeSort(nums, mid, r, temp);
    
    int p = l, q = mid, i = l;
    while (p < mid || q < r) {
        if (q >= r || (p < mid && nums[p] <= nums[q])) {
            temp[i++] = nums[p++];
        } else {
            temp[i++] = nums[q++];
        }
    }
    for (i = l; i < r; i++) nums[i] = temp[i];
}

void mergeSort(vector<int> &nums, int n) {
    for (int step = 1; step < n; step = step * 2) {
        for (int i = 0; i < n - step; i = i + 2 * step) {
            merge(nums, i, i + step - 1, min(i + 2 * step - 1, n - 1));
        }
    }
}
```

###### 堆排序

```c++
void upAdjust(int low, int high) {
    int i = high, j = high / 2;
    while (j >= low) {
        if (heap[i] > heap[j]) {
            swap(heap[i], heap[j]);
            i = j; j = i / 2;
        } else break;
    }
}
void downAdjust(int low, int high) {
    int i = low, j = low * 2;
    while (j <= high) {
        if (j + 1 <= high && heap[j] < heap[j + 1]) j = j + 1;
        if (heap[i] < heap[j]) {
            swap(heap[i], heap[j]);
            i = j; j = i * 2;
        } else break;
    }
}
void deleteTop() {
    heap[1] = heap[N--];
    downAdjust(1, N);
}
void insertElem(int data) {
    heap[++N] = data;
    upAdjust(1, N);
}
void heapSort() {
    for (int i = N / 2; i >= 1; i--) 
        downAdjust(i, N);
    for (int n = N; n >= 2; n--) {
        swap(heap[1], heap[n]);
        downAdjust(1, n - 1);
    }
}
```

###### [数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

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

###### [颜色分类](https://leetcode-cn.com/problems/sort-colors/)

```c++
void sortColors(vector<int>& nums) {
    int lo = 0, mid = 0, hi = nums.size() - 1;
    int temp = nums[lo];
    while (mid <= hi) {
        if (nums[mid] == 1) mid++;
        else if (nums[mid] == 0) {
            swap(nums[lo], nums[mid]);
            lo++; mid++;
        } else {
            swap(nums[hi], nums[mid]);
            hi--;
        }
    }
}
```

###### Top K Frequent Elements

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
