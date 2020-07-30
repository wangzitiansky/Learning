# 剑指offer题解

多种编程语言打卡剑指offer :clap:

|  题目  |  链接   |  分类    |     备注    |
|--------|---------|---------|-------------|
|3.找出数组中重复数字 |[找出数组中重复数字](#找出数组中重复数字) | 数组 |
|4.二维数组查找 | [二维数组查找](#二维数组查找) | 数组 |
|5.替换空格|[替换空格](#替换空格)|字符串 |
|6.从尾到头打印链表| [从尾到头打印链表](#从尾到头打印链表)| 链表 |
|7.重建二叉树|[重建二叉树](#重建二叉树)| 树 |
|8.二叉树的下一个节点|[二叉树的下一个节点](#二叉树的下一个节点)| 树 |
|9.用两个栈实现队列|[用两个栈实现队列](#用两个栈实现队列)| 栈与队列 |
|10.斐波那契数列|[斐波那契数列](#斐波那契数列)| 动态规划 |
|11.旋转数组的最小值|[旋转数组的最小值](#旋转数组的最小值)|二分|
|12.矩阵中的路径|[矩阵中的路径](#矩阵中的路径)|DFS|
|18.删除链表的节点| [删除链表的节点](#删除链表的节点) | 链表 |
|22.链表倒数第k个节点|[链表倒数第k个节点](#链表倒数第k个节点)| 链表 |
|24.反转链表|[反转链表](#反转链表)| 链表 |
|26.树的子结构|[树的子结构](#树的子结构)| 树 |
|27.二叉树的镜像|[二叉树的镜像](#二叉树的镜像)| 树 | 
|32.1从上到下打印二叉树| [从上到下打印二叉树](#从上到下打印二叉树) | 宽度优先搜索 |
|32.2分层从上到下打印二叉树2| [分层从上到下打印二叉树2](#分层从上到下打印二叉树2) | 宽度优先搜索 |
|32.3分层从上到下打印二叉树3| [分层从上到下打印二叉树3](#分层从上到下打印二叉树3) | 宽度优先搜索 |
|42.连续子数组的最大和| [连续子数组的最大和](#连续子数组的最大和) | 动态规划 |
|58.左旋字符串|[左旋字符串](#左旋字符串)| 字符串 |
|59.队列最大值|[队列最大值](#队列最大值)|单调队列|

### 找出数组中重复数字

##### 思路分析

```Cpp
/**
长度为n的数组，所有数字都在0 - n-1 范围内
根据容斥原理 必定有重复元素
解题思路是 将数组元素换位置 使得其元素的值和下标的值一致
如果发现要换位置的两个元素相等 则找到了重复的元素
**/
for i - nums.length:
    while nums[i] != i：
        if nums[i] nums[nums[i]] 相等:
            return
        swap(nums[i], nums[nums[i]])
```

##### Java
```java
class Solution {
    public int duplicateInArray(int[] nums) {
        int n = nums.length;
        if(n == 0){
            return -1;
        }

        for(int i = 0; i < n; i ++){
            if(nums[i] < 0 || nums[i] > n - 1)
                return -1;
        }

        for(int i = 0; i < n; i ++){
            while(nums[i] != i){
                if(nums[i] == nums[nums[i]]){
                    return nums[i];
                }
                int temp = nums[i];
                nums[i] = nums[temp];
                nums[temp] = temp;
            }
        }
        return -1;
    }
}
```

##### Cpp
```cpp
class Solution {
public:
    int duplicateInArray(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) return -1;
        for(int i = 0; i < n; i ++){
            if(nums[i] < 0 || nums[i] > n - 1){
                return -1;
            }
        }
        for(int i = 0; i < n; i ++){
            while(nums[i] != i){
                if(nums[i] == nums[nums[i]]){
                    return nums[i];
                }
                swap(nums[i], nums[nums[i]]);
            }
        }
        return -1;
    }
};
```

##### Python
```python
class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        if not nums:
            return -1
        length = len(nums)
        for n in nums:
            if n < 0 or n > length - 1:
                return -1
        for i in range(length):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]
        return -1
```

### 不修改数组找出重复数字

##### Cpp
```cpp
class Solution {
public:
    int duplicateInArray(vector<int>& nums) {
        int l = 1;
        int r = nums.size() - 1;
        while(l < r){
            int mid = l + r >> 1;
            int s = 0;
            for(auto x : nums) s += (x >= l && x <= mid ? 1 : 0);
            if(s > mid -l + 1){
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return r;
    }
};
```
##### Java
```java
class Solution {
    public int duplicateInArray(int[] nums) {
        int l = 1;
        int r = nums.length - 1;
        while(l < r){
            int mid = l + r >> 1;
            int s = 0;
            for(int x : nums) s += x >= l && x <= mid ? 1 : 0;
            if(s > mid - l + 1){
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
}
```

#### 二维数组查找

### 分析

根据题意，从右上角开始搜索，此点下面的点都比他大，左边的点都比他小

### AC代码

Java
```java
class Solution {
    public boolean searchArray(int[][] array, int target) {
        int maxRow = array.length;
        if(array == null || maxRow == 0){
            return false;
        }
        int maxCol = array[0].length;
        int row = 0;
        int col = array[0].length - 1;
        while(row >= 0 && row < maxRow && col >= 0 && col < maxCol){
            if(array[row][col] == target)
                return true;
            else if(array[row][col] > target)
                col--;
            else if(array[row][col] < target)
                row++;
        }
        return false;
    }
}

```

C++

```cpp
class Solution {
public:
    bool searchArray(vector<vector<int>> array, int target) {
        int rows = array.size();
        if(rows == 0) return false;
        int cols = array[0].size();
        int row = 0;
        int col = cols - 1;
        while(row < rows && col >= 0){
            if(array[row][col] > target){
                col --;
            } else if(array[row][col] < target){
                row ++;
            } else {
                return true;
            }
        }
        return false;
    }
};

```

### 替换空格

### 分析

先将字符串通过追加空格变长，之后再从后往前将字符串进行替换

### AC代码

Java
```java
public String replaceSpaces(StringBuffer str) {
// 先计算替换后的字符串的长度
    int bef = str.length();
    for(int i = 0; i < bef; i++){
        if(str.charAt(i) == ' '){
            str.append("  ");
        }
    }
    int aft = str.length();
    int i = bef - 1;
    int j = aft - 1;
    
    // 从后往前 对于每个空格进行替换
    while(j >= 0){
        char ch = str.charAt(i --);
        if(ch != ' '){
            str.setCharAt(j --, ch);
        } else {
            str.setCharAt(j --, '0');
            str.setCharAt(j --, '2');
            str.setCharAt(j --, '%');
        }
    }
    return str.toString();
}
```

### 从尾到头打印链表

### 分析

可以先顺序打印，之后再进行反转

### AC代码

Java
```java
class Solution {
    public int[] reversePrint(ListNode head) {
        List<Integer> res = new ArrayList<>();
        if(head == null) return new int [] {};
        while(head != null){
            res.add(head.val);
            head = head.next;
        }
        Collections.reverse(res);
        return res.stream().mapToInt(o -> o).toArray();
    }
}
```

### 重建二叉树

### 分析

### AC代码

Java

  ```java
// 从中序遍历得到左右子树的长度

// 从前序遍历得到根节点

private Map<Integer, Integer> map = new HashMap<>();
    
public TreeNode buildTree(int[] preorder, int[] inorder) {

    // 将 下标 - 值 记录 
    for(int i = 0; i < inorder.length; i++){
        map.put(inorder[i], i);
    }
    return build(preorder, 0, preorder.length - 1, 0);
}
public TreeNode build(int[] preorder, int prel, int prer, int inl){

    // 边界
    if(prel > prer)
        return null;

    // 根节点
    int val = preorder[prel];
    TreeNode root = new TreeNode(val);

    // 中序遍历 inl - index 求出左树的长度
    int index = map.get(val);
    int len = index - inl;

    // 左右递归 求出 left right
    root.left = build(preorder, prel + 1, prel + len, inl);
    root.right = build(preorder, prel + len + 1, prer, index + 1);
    return root;
}
  ```

Python
```python
class Solution(object):
    def buildTree(self, preorder, inorder):
        map = {}
        def build(preL, preR, inL):
            if preL > preR:
                return 
            # preorder root
            # 根节点
​            val = preorder[preL]
​            root = TreeNode(val)
​            index = map.get(val)
​            length = index - inL
​            root.left = build(preL + 1, preL + length, inL)
​            root.right = build(preL + length + 1, preR, index + 1)
​            return root
​        for i in range(len(inorder)):
​            map[inorder[i]] = i
​        return build(0, len(preorder) - 1, 0)
```

### 二叉树的下一个节点

### 分析

### AC代码

Java
```java
public TreeNode inorderSuccessor(TreeNode p) {
        
  // 特别判断一下
  if(p == null)
    return p;

  // 如果右子树不为空 则结果一定是右树的最左子结点
  if(p.right != null){
    TreeNode q = p.right;
    while(q != null){
      p = q;
      q = q.left;
    }
    return p;
  } else {

    // 如果右子树为空 则结果一定为其整个子树的父节点000    
    TreeNode par = p.father;
    while(par != null && par.right == p){
      p = par;
      par = par.father;
    }
    return par;
  }
}
```

Python
```python
class Solution(object):
    def inorderSuccessor(self, q):
        """
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not q:
            return None
        # 右子树的最左节点
        if q.right:
            q = q.right
            p = q
            while q:
                p = q
                q = q.left
            return p
        else:
            # 整个子树的父节点
            f = q.father
            while f and f.right == q:
                q = f
                f = q.father
            return f
```


### 用两个栈实现队列

### 分析

### AC代码

Java 

```java
class MyQueue {

    Deque<Integer> in;
    Deque<Integer> out;
    /** Initialize your data structure here. */
    public MyQueue() {
        in = new ArrayDeque<>();
        out = new ArrayDeque<>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        in.push(x);
    }
    
    // 假如out是空 则调用此函数填充in
    public void clearIn(){
        while(!in.isEmpty()){
            out.push(in.pop());
        }
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if(out.isEmpty()){
            clearIn();
        }
        return out.pop();
    }
    
    /** Get the front element. */
    public int peek() {
        if(out.isEmpty()){
            clearIn();
        }
        return out.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return out.isEmpty() && in.isEmpty();
    }
}
```

Python

```python
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.com = []
        self.out = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.com.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.out:
            while len(self.com):
                self.out.append(self.com.pop())
        return self.out.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.out:
            while len(self.com):
                self.out.append(self.com.pop())
        return self.out[len(self.out) - 1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.com) == 0 and len(self.out) == 0;

```

### 斐波那契数列

### 分析

### AC代码

```java
// a b (c)
public int Fibonacci(int n) {
    int a = 0, b = 1, c = 0;
    while(n -- > 0){
      c = a + b;
      a = b;
      b = c;
    }
    return a;
}
```

### 旋转数组的最小值

### 分析

### AC代码

二分查找

```java
public int findMin(int[] nums) {
    int n = nums.length - 1;
    if(n < 0) return -1;

    // 去除nums[n] == nums[0] 的部分
    while(n > 0 && nums[n] == nums[0]) n --;
    if(nums[n] >= nums[0]) return nums[0];
    int l = 0, r = n;
    while(l < r){
      int mid = l + r >> 1;

      // 二分的性质选取的是 左边的都 >= nums[0] 右边的都 < nums[0] 
      if(nums[mid] >= nums[0]){
        l = mid + 1;
      } else {
        r = mid;
      }
    }
    return nums[r];
}
```

### 删除链表的节点

### 分析

因为要删除，所以需要找到被删除结点cur，并且需要记录cur的前一个结点pre。注意被删除的结点是第一个结点的特殊情况。

### AC代码

Java
```java
class Solution {
    public ListNode deleteNode(ListNode head, int val) {
        ListNode cur = head;
        ListNode pre = null;
        while(cur.val != val){
            pre = cur;
            cur = cur.next;
        }
        if(pre != null)
            pre.next = cur.next;
        else
            head = head.next;
        cur.next = null;
        return head;
    }
}
```

### 链表倒数第k个节点

### 分析

双指针，一个指针想走k步，之后快慢指针一起走，快指针是null的时候，返回慢指针

### AC代码

```java
class Solution {
    public ListNode getKthFromEnd(ListNode head, int k) {
        ListNode cur = head;
        while(cur != null && k -- > 0){
            cur = cur.next;
        }
        if(k > 0) return null;
        ListNode pre = head;
        while(cur != null){
            pre = pre.next;
            cur = cur.next;
        }
        return pre;
    }
}
```

### 反转链表

### 分析

### AC代码

##### Java

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null) return head;
        ListNode pre = null;
        ListNode cur = head;
        ListNode ne = cur.next;
        while(ne != null){
            cur.next = pre;
            pre = cur;
            cur = ne;
            ne = cur.next;
        }
        cur.next = pre;
        return cur;
    }
}
```

### 树的子结构

### 分析

其实就是递归做

### AC代码

```java
class Solution {

    public boolean isSub(TreeNode A, TreeNode B){
        if(B == null) return true;
        if(A == null) return false;
        if(A.val == B.val) return isSub(A.left, B.left) && isSub(A.right, B.right);
        else return false;
    }

    public boolean isSubStructure(TreeNode A, TreeNode B) {
        if(B == null) return false;
        if(A == null) return false;
        if(A.val == B.val) {
            if(isSub(A.left, B.left) && isSub(A.right, B.right))  return true;
        }
        return isSubStructure(A.left, B) || isSubStructure(A.right, B);
    }

}
```
### 二叉树的镜像

### 分析

递归，注意交换节点的写法

### AC代码

```java
class Solution {
    public TreeNode mirrorTree(TreeNode root) {
        if(root == null) return root;
        TreeNode tmp = root.right;
        root.right = mirrorTree(root.left);
        root.left = mirrorTree(tmp);
        return root;
    }
}
```

### 对称的二叉树

### 分析

如果当前节点的值不相等，返回false，如果相等，就递归(left.left, right.right) && (left.right, right.left)

### AC代码

```java
class Solution {

    public boolean dfs(TreeNode p, TreeNode q){
        if(q == null || p == null) return (p == null) && (q == null);
        if(p.val != q.val) return false;
        return dfs(p.left, q.right) && dfs(p.right, q.left);
    }

    public boolean isSymmetric(TreeNode root) {
        if(root == null) return true;
        return dfs(root.left, root.right);
    }
}
```

### 矩阵中的路径

##### Java
```java
class Solution {
    
    public boolean hasPath(char[][] matrix, String str) {
        int rows = matrix.length;
        if(rows == 0) return false;
        int cols = matrix[0].length;
        for(int i = 0; i < rows; i ++)
            for(int j = 0; j < cols; j ++){
                if(matrix[i][j] == str.charAt(0)){
                    if(dfs(rows, cols, str, 0, matrix, i, j))
                        return true;
                }
            }
        return false;
    }
    
    public boolean dfs(int rows, int cols, String str, int l, char[][] matrix, int row, int col){
        if(l == str.length() - 1) return true;
        char ch = matrix[row][col];
        
        // 标记为走过
        matrix[row][col] = '*';
        int[] pathx = {0, 1, 0, -1};
        int[] pathy = {1, 0, -1, 0};
        for(int i = 0; i < 4; i++){
            int x = row + pathx[i];
            int y = col + pathy[i];
            if(x >= 0 && x < rows && y >= 0 && y < cols && matrix[x][y] == str.charAt(l + 1)){
                if(dfs(rows, cols, str, l + 1, matrix, x, y))
                    return true;
            }
        }
        
        // 将原来的矩阵复位
        matrix[row][col] = ch;
        return false;
    }
}
```

##### Python

```python
class Solution(object):
    def hasPath(self, matrix, string):

        def dfs(row, col, k):
            if k == len(string) - 1:
                return True
            # 标记此点已经走过
            c = matrix[row][col]
            matrix[row][col] = '*'
            path = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for i in range(4):
                nx = row + path[i][0]
                ny = col + path[i][1]
                if nx >= 0 and nx < rows and ny >= 0 and ny < cols and matrix[nx][ny] == string[k + 1]:
                    if dfs(nx, ny, k + 1):
                        return True
            # 讲此点恢复
            matrix[row][col] = c
            return False

        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == string[0]:
                    if dfs(i, j, 0):
                        return True
        return False
```

### 面试题13:机器人的运动范围

##### Java
```java
class Solution {
    
    // dfs 搜索 看能搜索多少个格子
    private int rows;
    private int cols;
    private int threshold;
    private boolean[][] reach;
    private int num;
    private int[][] path = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    public int movingCount(int threshold, int rows, int cols)
    {
        this.rows = rows;
        this.cols = cols;
        if(rows <= 0 || cols <= 0) return 0;
        this.threshold = threshold;
        
        // 标记是否走过
        reach = new boolean[rows][cols];
        dfs(0, 0);
        return num;
    }
    public void dfs(int row, int col){
        num ++;
        reach[row][col] = true;
        for(int i = 0; i < 4; i ++){
            int x = row + path[i][0];
            int y = col + path[i][1];
            if(x >= 0 && x < rows && y >=0 && y < cols && !reach[x][y] && get_sum(x, y) <= threshold){
                dfs(x, y);
            }
        }
    }
    // 算出行坐标和列坐标的数位之和
    public int get_sum(int a, int b){
        return get_num(a) + get_num(b);
    }
    
    public int get_num(int a){
        int sum = 0;
        while(a > 0){
            sum += a % 10;
            a /= 10;
        }
        return sum;
    }
}
```
##### Python
```Python

```

<details>
  <summary>面试题21:调整数据顺序使奇数位于偶数前面</summary>


```java
   public void reOrderArray(int [] array) {
        int l = -1, r = array.length;
        if(r == 0) return;
        
        // 其实就是快排的思想
        while(l < r){
            do l ++; while(array[l] % 2 != 0);
            do r --; while(array[r] % 2 == 0);
            if(l < r){
                int temp = array[l];
                array[l] = array[r];
                array[r] = temp;
            }
        }
    }
```




### 从上到下打印二叉树

### 分析

层序遍历

### AC代码

```java
   public List<Integer> printFromTopToBottom(TreeNode root) {
        List<Integer> res = new LinkedList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        if(root == null)
            return res;
        queue.add(root);
        while(!queue.isEmpty()){
            TreeNode tree = queue.poll();
            res.add(tree.val);
            if(tree.left != null) queue.add(tree.left);
            if(tree.right != null) queue.add(tree.right);
        }
        return res;
    }
```

### 分层从上到下打印二叉树2

面试题32.2

### 分析

层序遍历

### AC代码

```java
   public List<List<Integer>> printFromTopToBottom(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        List<List<Integer>> res = new ArrayList<>();
        if(root == null){
            return res;
        }
        queue.add(root);
        while(!queue.isEmpty()){
            int size = queue.size();
            List<Integer> l = new ArrayList<>();
            while(size -- > 0){
                TreeNode tree = queue.poll();
                l.add(tree.val);
                if(tree.left != null)
                    queue.add(tree.left);
                if(tree.right != null)
                    queue.add(tree.right);
            }
            res.add(l);
        }
        return res;
    }
```

### 分层从上到下打印二叉树3

### 分析

宽搜模板提

### AC代码

```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if(root == null) return res;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        boolean reverse = false;
        while(!queue.isEmpty()){
            int size = queue.size();
            List<Integer> tmp = new ArrayList<>();
            while(size -- > 0){
                TreeNode node = queue.poll();
                tmp.add(node.val);
                if(node.left != null) queue.add(node.left);
                if(node.right != null) queue.add(node.right);
            }
            if(reverse) Collections.reverse(tmp);
            reverse = !reverse;
            res.add(tmp);
        }
        return res;
    }
}
```

### 连续子数组的最大和

### 题意分析

动态规划的思想: 如果之前的和小于0，则丢弃，如果不是0，则加上下一个元素求现在的元素和

### AC代码

```Cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res = INT_MIN;
        int s = 0;
        for(auto x : nums){
            if(s < 0) s = 0;
            s += x;
            res = max(res, s);
        }
        return res;
    }
};
```

### 二叉树中和为某一值的路径

### 

### AC代码

```java
class Solution {

    public void dfs(List<List<Integer>> res, List<Integer> tmp, TreeNode root, int sum){
        if(root == null) return;
        int val = root.val;
        tmp.add(val);
        if(val == sum && root.left == null && root.right == null){
            res.add(new ArrayList<>(tmp));
            tmp.remove(tmp.size() - 1);
            return;
        }
        dfs(res, tmp, root.left, sum - val);
        dfs(res, tmp, root.right, sum - val);
        tmp.remove(tmp.size() - 1);
    }

    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<>();
        if(root == null) return res;
        dfs(res, new ArrayList<>(), root, sum);
        return res;
    }
}
```


### 左旋字符串

面试题58

### 分析

将字符串后面的若干字符转移到前面，可以用切片求解

### AC代码

Python
```python
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]
```

### 队列最大值

面试题59

### 分析

给定一个数组和窗口大小，求滑动窗口的最大值

可以用单调队列求解

所有元素只会进队一次，出队一次，所以时间负责度是O(N)

```
for(){
  1. 如果超出滑动窗口范围，则弹出队头
  if(队头 <= i - k)
  队头弹出
  2. 维护单增的队列
  while(队尾元素 <= 当前元素)
  队尾弹出
  3. 把当前元素的下标放入队尾
}
```

### AC代码

Java

```java
class Solution {
    public int[] maxInWindows(int[] nums, int k) {
        int n = nums.length;
        if(n == 0)
            return new int[] {};
        List<Integer> res = new ArrayList<>();
        int[] q = new int[n];
        int hh = 0;
        int tt = -1;
        for(int i = 0; i < n; i ++){
            // 如果超出滑动窗口范围 则弹出队头
            if(hh <= tt && q[hh] < i - k + 1){
                hh ++;
            }
            // 如果当前元素 >= 队列头元素 则弹出
            while(hh <= tt && nums[q[tt]] <= nums[i]){
                tt --;
            }
            // 将元素如队尾
            q[++ tt] = i;
            // 每次打印队头
            if(i >= k - 1){
                res.add(nums[q[hh]]);
            }
        }
        // ArrayList to []
        return res.stream().mapToInt(i -> i).toArray();
    }
}
```


Python

```python
class Solution(object):
    def maxInWindows(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        res = []
        q = deque()
        if not nums:
            return res

        for i in range(len(nums)):
            if q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

```

C++

```c++
class Solution {
public:
    vector<int> maxInWindows(vector<int>& nums, int k) {
        vector<int> res;
        int n = nums.size();
        int q[n], hh = 0, tt = -1;
        if(n == 0){
            return res;
        }

        for(int i = 0; i < n; i++){
            if(hh <= tt && q[hh] <= i - k){
                hh ++;
            }
            while(hh <= tt && nums[q[tt]] < nums[i]){
                tt --;
            }
            q[++ tt] = i;
            if(i >= k - 1){
                res.push_back(nums[q[hh]]);
            }
        }
        return res;
    }
};
```

JavaScript

```javascript
var maxInWindows = function(nums, k) {
    var res = [];
    var q = [];
    for(var i = 0; i < nums.length; i ++){
        if(q.length !== 0 && q[0] <= i - k){
            q.shift();
        }
        while(q.length !== 0 && nums[q[q.length - 1]] <= nums[i]){
            q.pop();
        }
        q.push(i);
        if(i >= k - 1){
            res.push(nums[q[0]]);
        }
    }
    return res;
};

```

