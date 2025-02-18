/* 本题主要考察在 MySQL 内做简单的计算操作，比如求平均值，求和等。在解题前先回顾一下相关的函数。

SUM()：返回某列的和。
AVG()：返回某列的平均值。
COUNT() ：返回某列的行数。
MAX() ：返回某列的最大值。
MIN() ：返回某列的最小值。
 */

SELECT 
    query_name, 
    ROUND(AVG(rating/position), 2) quality,  /* 计算quality 计算rating/position的平均值 */
    ROUND(SUM(IF(rating < 3, 1, 0)) * 100 / COUNT(*), 2) poor_query_percentage
FROM Queries
Where query_name IS NOT NULL
GROUP BY query_name

/* 如果 rating 小于 3，则返回 1；否则返回 0。 由于 IF 表达式返回 1 或 0，SUM 函数会对所有返回 1 的记录进行求和，从而得到评分小于 3 的记录数。
COUNT(*)：计算总记录数。  */