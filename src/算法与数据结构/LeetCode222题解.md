# 完全二叉树的结点个数

### 分析

给定一个完全二叉树，求结点个数，最好想的办法就是周游, 时间空间复杂度都是O（N）

### AC代码

C++
```cpp []
class Solution {
public:
    int cnt;

    void dfs(TreeNode* root){
        if(root == nullptr) return;
        cnt ++;
        dfs(root -> left);
        dfs(root -> right);
    }

    int countNodes(TreeNode* root) {
        cnt = 0;
        if(root == nullptr) return cnt;
        dfs(root);
        return cnt;
    }
};
```

Python3

```python []
class Solution:

    def __init__(self):
        self.res = 0

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root):
            if not root:
                return 
            self.res += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res
```

### 优化 :clap:

但是，可以从完全二叉树的性质入手来优化：如果这个二叉树是满的，那么结点个数 = 2 ** h - 1, h 为树的高度

这样就可以每次先检查此树是不是满二叉树，如果是满二叉树，则直接用公式得出树的高度，如果不是满二叉树，则递归下去。

```python
2 ** h - 1 写为 1 << h - 1
位运算会快一点
```

此方法的时间复杂度

```python
时间复杂度 = O(h) + O(h - 1) + ... + O(1) = O(h^2/2 + h/2) = O(h^2) = O(logN) * O(logN)
```

C++
```cpp
class Solution {
public:
    int countNodes(TreeNode* root) {
        if(root == nullptr) return 0;

        int hr, hl;
        TreeNode* l = root;
        TreeNode* r = root;

        // 检查是不是满二叉树
        while(l){
            hl ++;
            l = l -> left;
        }
        while(r){
            hr ++;
            r = r -> right;
        }

        // 如果是满的 则直接公式算出节点数
        if(hr == hl) return 1 << hl - 1;

        // 如果不是满的 则递归下去
        return countNodes(root -> left) + 1 + countNodes(root -> right);

    }
};
```

Python3
```python
class Solution:

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = root
        r = root
        lh = 0
        rh = 0

        while l:
            l = l.left
            lh += 1
        while r:
            r = r.right
            rh += 1
        
        if rh == lh:
            return (1 << lh) - 1
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
```

优化方法参考自: [:books:](https://leetcode.com/problems/count-complete-tree-nodes/discuss/61953/Easy-short-c%2B%2B-recursive-solution)