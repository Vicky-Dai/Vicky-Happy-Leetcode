SQL 执行顺序
FROM + JOIN：

确定数据源，连接表格，形成一个基础的“笛卡尔积”或匹配表格。
如果有JOIN，会先执行连接，创建一个新的中间结果表。
WHERE：

在生成的中间表基础上，过滤不符合条件的行。
GROUP BY： tips在 MySQL 中，GROUP BY 子句确实可以使用 SELECT 子句中的别名。这是 MySQL 的一个特性

按指定列对数据进行分组，形成分组后的数据集合。
HAVING：

在分组后的数据上，进一步筛选分组的结果，通常是针对聚合函数的结果进行筛选。
SELECT：

提取指定的列，决定最终返回哪些字段或表达式结果。
ORDER BY：

按指定列对结果进行排序。
LIMIT：

返回指定数量的行，限制最终结果的行数。