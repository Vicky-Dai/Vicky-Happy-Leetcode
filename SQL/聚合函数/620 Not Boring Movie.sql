-- 方法：使用 MOD() 函数
-- 我们可以使用 mod(id,2)=1 来确定奇数 id，然后添加 description != 'boring' 来解决问题。 是一个 SQL 函数，用于计算 id 列的值除以 2 的余数

select *
from cinema
where mod(id, 2) = 1 and description != 'boring'
order by rating DESC
