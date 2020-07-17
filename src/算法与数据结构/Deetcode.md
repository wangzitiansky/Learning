# LeetCode 数据库题目

### 175. 组合两个表

### 分析

就是个JOIN，注意LEFT JOIN INNER JOIN RIGHT JOIN 的区别

### AC代码

```sql
SELECT FirstName, LastName, City, State FROM Person LEFT JOIN Address ON Person.PersonId = Address.PersonId
```