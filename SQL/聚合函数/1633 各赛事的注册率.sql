# Write your MySQL query statement below
select contest_id , round(count(user_id) * 100/ (select count(*) from users), 2) percentage 
from Register
group by contest_id
order by percentage desc, contest_id /* 先降序排percentage tie了再contest_id升序 */

/* * 100 是为了将比例转换为百分比，as percentage 是给计算结果起一个别名，使查询结果中的这一列名称为 percentage。 */