###### [二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

```c++
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root) return root;
    if (p->val < root->val && q->val > root->val) return root;
    if (q->val < root->val && p->val > root->val) return root;
    if (p->val < root->val && q->val < root->val) return lowestCommonAncestor(root->left, p, q);
    if (p->val > root->val && q->val > root->val) return lowestCommonAncestor(root->right, p, q);
    return root;
}
```

###### [二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)

```c++
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (root == NULL) return NULL;
    if (root == p || root == q) return root;
    TreeNode* left = lowestCommonAncestor(root->left, p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);
    if (left == NULL) return right;
    if (right == NULL) return left;
    return root;
}
```

###### [二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)

```c++
int kthLargest(TreeNode* root, int k) {
    int ans;
    dfs(root, k, ans);
    return ans;
}
void dfs(TreeNode *root, int &n, int &ans) {
    if (!root) return;
    dfs(root->right, n, ans);
    if (n == 1) ans = root->val;
    n--;
    dfs(root->left, n, ans);
}
```

###### [二叉树的锯齿形层序遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)

```c++

```

