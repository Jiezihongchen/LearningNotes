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

###### [合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

```c++

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
ListNode* reverseKGroup(ListNode* head, int k) {
    ListNode *dummy = new ListNode, *pre;
    dummy->next = head; pre = dummy;
    while (head) {
        ListNode *tail = pre;
        int cnt = k;
        while (cnt--) {
        	tail = tail->next;
            if (!tail) return dummy->next;
        }
        ListNode *tail_ = tail->next;
        pair<ListNode*, ListNode*> result = reverseList(head, tail);
        head = result.first;
        tail = result.second;
        
        pre->next = head;
        tail->next = tail_;
        pre = tail;
        head = tail->next;
    }
    return dummy->next;
}
pair<ListNode*, ListNode*> reverseList(ListNode* head, List* tail) {
	ListNode *prev = null, *next, *tail_ = head;
    while (head != tail->next) {
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return {prev, tail_};
}
```

###### [ 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/)

```c++
bool isPalindrome(ListNode* head) {
	if (!head || !head->next) return true;
    ListNode *slow = head, *fast = head;
    while (fast->next && fast->next->next) {
        fast = fast->next->next;
        slow = slow->next;
    }
    slow->next = reverseList(slow->next);
    slow = slow->next;
    while (slow) {
        if (head->val != slow->val) return false;
        head = head->next;
        slow = slow->next;
    }
    return true;
}
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

###### [排序链表](https://leetcode-cn.com/problems/sort-list/)

```c++

```

###### [两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

```c++
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* dummy = new ListNode, *cur = dummy;
    int cnt = 0;
    while (l1 && l2) {
        cur->next = new ListNode((l1->val + l2->val + cnt) % 10);
        cur = cur->next;
        cnt = (l1->val + l2->val + cnt) / 10;
        l1 = l1->next;
        l2 = l2->next;
    }
    while (l1) {
        cur->next = new ListNode((l1->val + cnt) % 10);
        cur = cur->next;
        cnt = (l1->val + cnt) / 10;
        l1 = l1->next;
    }
    while (l2) {
        cur->next = new ListNode((l2->val + cnt) % 10);
        cur = cur->next;
        cnt = (l2->val + cnt) / 10;
        l2 = l2->next;
    }
    if (cnt) cur->next = new ListNode(cnt);
    return dummy->next;
}
```

