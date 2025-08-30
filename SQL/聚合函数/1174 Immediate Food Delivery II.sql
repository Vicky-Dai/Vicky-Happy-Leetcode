select round (
    sum(order_date = customer_pref_delivery_date) * 100 /
    count(*),
    2
) as immediate_percentage
from Delivery
where (customer_id, order_date) in ( /* 子查询其实只有两个值，但是上面主查询FROM，把符合要求的整行都留下了 */
    select customer_id, min(order_date)
    from delivery
    group by customer_id
)


/* 表达式	含义
COUNT(expression)	统计非 NULL 的个数，不管值是多少
SUM(expression)	计算数值的和，如果是布尔表达式，true 视为 1，false 视为 0 */