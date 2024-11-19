SELECT e.name, b.bonus
FROM Employee e 
LEFT JOIN Bonus b
ON e.empId = b.empId --连接的时候别忘记写
WHERE b.bonus < 1000 OR b.bonus IS NULL; --所有语法都要大写，不然会报错