-- 自关联 
SELECT a.id
FROM weather a, weather b /* 使用了旧的隐式连接语法，从同一个表 weather 中创建了两个别名 a 和 b。这意味着我们在同一张表中进行了自连接（self-join），a 和 b 代表了 weather 表的两个不同实例。 */
WHERE a.temperature > b.temperature
AND DATEDIFF(a.recordDate, b.recordDate) = 1;  /* 前 - 后 = 1 ， 函数用于计算两个日期之间的天数差。在这里，它用来判断 a.recordDate 和 b.recordDate 之间的差值是否为 1，表明 a 记录的日期是 b 记录日期的后一天。 */
