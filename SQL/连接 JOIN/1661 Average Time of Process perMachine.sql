SELECT
   machine_id,
   round( sum( IF ( activity_type = 'start',-TIMESTAMP,TIMESTAMP ))/ count( 1 )* 2, 3 ) AS processing_time 
FROM
   Activity 
GROUP BY
   machine_id


-- SUM 的作用：将一组值进行求和。
-- 内部逻辑（IF）：根据条件生成的值是正或负，SUM 将这些值求和。