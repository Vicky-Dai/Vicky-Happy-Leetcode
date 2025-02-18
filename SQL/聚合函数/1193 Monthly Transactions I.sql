/* 预备知识
本题使用到的 MySQL 函数的说明：

DATE_FORMAT(date, format) ：用于以不同的格式显示日期/时间数据。date 参数是合法的日期，format 规定日期/时间的输出格式。

方法一：DATE_FORMAT() 函数、GROUP BY
思路 本题要求 查找每个月和每个国家/地区的事务数及其总金额、已批准的事务数及其总金额*
1. 查找每个月和每个国家/地区
2. 查找总的事务数。
3. 查找总金额。
4. 查找已批准的事物数。
5. 查找已批准的事物的总金额。*/


SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    COUNT(IF(state = 'approved', 1, NULL)) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM Transactions
GROUP BY month, country

/* COUNT(IF(state = 'approved', 1, NULL))：

COUNT 函数会计算表达式结果为非 NULL 的记录数。
由于 IF 表达式在 state 等于 'approved' 时返回 1，否则返回 NULL，因此 COUNT 函数会计算 state 为 'approved' 的记录数。 */

/* 注意COUNT 是NULL SUM是0 */