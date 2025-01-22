
SELECT v.customer_id, COUNT(*) AS count_no_trans /* #句内不同于句话要用逗号隔开 */
FROM Visits v
LEFT JOIN Transactions t    /*#注意LEFT JOIN ON  */
ON v.visit_id = t.visit_id
WHERE t.transaction_id is NULL
GROUP BY customer_id /* #分类 常用于统一个id多次出现，但最后结果只想要一个id一行 */
/* -- #这道题学到了很重要的一点：sql语句执行不是从上到下的，而是从整体到局部，先按条件join，再按where条件筛选，以及group，大的框架做出来之后，再count函数这些 */
