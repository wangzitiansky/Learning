# LeetCode 数据库题目

### 175. 组合两个表

### 分析

就是个JOIN，注意LEFT JOIN INNER JOIN RIGHT JOIN 的区别

### AC代码

```sql
SELECT FirstName, LastName, City, State FROM Person LEFT JOIN Address ON Person.PersonId = Address.PersonId
```

### 176. 第二高的薪水

### 分析

注意DISTINCT的使用 还有LIMIT 1 OFFSET 1

### AC代码

```sql
SELECT(SELECT DISTINCT(Salary) FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1) AS SecondHighestSalary;
```