```c++
struct ListNode {
	int val;
    ListNode *next;
    ListNode(int x): val(x), next(nullptr) {}
};
```

###### 反转链表

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

###### [环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

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

###### [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

```c++
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode *dummy = new ListNode(0), *node = dummy;
    while (l1 && l2) {
        if (l1->val <= l2->val) {
            node->next = l1;
            l1 = l1->next;
        } else {
            node->next= l2;
            l2 = l2->next;
        }
        node = node->next;
    }
    node->next = l1 ? l1 : l2;
    return dummy->next;
}
```

###### [两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

```c++
ListNode* swapPairs(ListNode* head) {
    ListNode *p = head, *s;
    while (p && p->next) {
        s = p->next;
        p->next = s->next;
        s->next = p;
        head = s;
        while (p->next && p->next->next) {
        	s = p->next->next;
            p->next->next = s->next;
            s->next = p->next;
            p->next = s;
            p = s->next;
        }
    }
    return head;
}
```

###### [交换链表中的节点](https://leetcode-cn.com/problems/swapping-nodes-in-a-linked-list/)

```c++

```

###### [K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)

```c++

```

###### [合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

```c++

```

