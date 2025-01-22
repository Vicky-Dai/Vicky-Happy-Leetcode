""" 这道题考察AVG LEFT JOIN """
SELECT 
    s.user_id,
    ROUND(IFNULL(AVG(c.action='confirmed'), 0), 2) AS confirmation_rate /* 0是如果结果是NULL,就返回0  2是ROUND到小数点后两位 */
FROM 
    Signups AS s 
LEFT JOIN /* 保证左侧用户都有，右侧没有 */
    Confirmations AS c 
ON 
    s.user_id = c.user_id
GROUP BY 
    s.user_id /* #合并多行数据，确保每个 user_id 在结果中只出现一次。这是为了避免由于 LEFT JOIN 导致的 重复行，从而确保每个用户只有一行包含他们的确认率。 */
    