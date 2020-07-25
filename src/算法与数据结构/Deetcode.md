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

### 178. 分数排名

### 分析



### AC代码

```sql
SELECT s1.Score AS Score, COUNT(DISTINCT(s2.Score)) AS `Rank`
FROM Scores as s1 INNER JOIN Scores as s2 
WHERE s1.Score <= s2.Score 
GROUP BY s1.id ORDER BY s1.Score DESC;
```