###### [用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks/)

```c++
class MyQueue {
    stack<int> in_, out_;
public:
    MyQueue() {

    }
    void push(int x) {
        in_.push(x);
    }
    int pop() {
        in2out();
        int x = out_.top();
        out_.pop();
        return x;
    }
    int peek() {
        in2out();
        return out_.top();
    }
    void in2out() {
        if (out_.empty()) {
            while (!in_.empty()) {
                out_.push(in_.top());
                in_.pop();
            }
        }
    }
    bool empty() {
        return in_.empty() && out_.empty();
    }
};
```

###### [下一个更大元素 I](https://leetcode-cn.com/problems/next-greater-element-i/)

```c++

```

###### [下一个更大元素 II](https://leetcode-cn.com/problems/next-greater-element-ii/)

```c++

```

###### [每日温度](https://leetcode-cn.com/problems/daily-temperatures/)

```c++

```

###### [接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)

```c++

```

###### [接雨水 II](https://leetcode-cn.com/problems/trapping-rain-water-ii/)

```c++

```

###### [柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)

```c++

```

