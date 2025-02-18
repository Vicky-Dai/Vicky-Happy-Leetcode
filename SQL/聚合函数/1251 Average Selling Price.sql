-- 方法一：JOIN
/* 本题需要计算每个产品的平均售价，平均售价 = 销售总额 / 总数量，因此我们只需要计算除每个产品的销售总额和总数量即可。总数量可以直接使用 UnitsSold 计算得出，使用 GROUP BY 和 SUM 函数即可：
SELECT product_id, SUM(units) FROM UnitsSold GROUP BY product_id

 */
 /* T 是子查询的别名。别名用于给子查询或表一个临时名称，以便在外部查询中引用它。 */

SELECT
    product_id,
    IFNULL(Round(SUM(sales) / SUM(units), 2), 0) AS average_price
FROM (
    SELECT
        Prices.product_id AS product_id,
        Prices.price * UnitsSold.units AS sales,
        UnitsSold.units AS units
    FROM Prices 
    LEFT JOIN UnitsSold ON Prices.product_id = UnitsSold.product_id
    AND (UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date)
) T 
GROUP BY product_id

/* 这个 SQL 查询使用了嵌套查询（子查询）来计算每个产品的平均售价。 */