```c++
struct ListNode {
	int val;
    ListNode *next;
    ListNode(int x): val(x), next(nullptr) {}
};
```

# 反转链表

```c++
ListNode* reverseList(ListNode* head) {
    if (!head || !head->next) return head;
    ListNode *last = reverseList(head->next);
    head->next->next = head;
    head->next = nullptr;
    return last;
}
```

```c++
ListNode* reverseList(ListNode* head) {
	ListNode *prev = nullptr, *next;
    while (head) {
    	next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return prev;
}
```

# 判断环

```c++
ListNode* detectCycle(ListNode *head) {
    ListNode *slow = head, *fast = head;
    do {
        if (!fast || !fast->next) return nullptr;
        fast = fast->next->next;
        slow = slow->next;
    } while (fast != slow);
    fast = head;
    while (fast != slow) {
        fast = fast->next;
        slow = slow->next;
    }
    return fast;
}
```

