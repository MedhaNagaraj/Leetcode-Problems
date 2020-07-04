/*
176. Second Highest Salary

Solution to : https://leetcode.com/problems/second-highest-salary/

Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
*/

-- Method 1
SELECT 
    max(salary) as "SecondHighestSalary"
FROM
    Employee
WHERE 
    salary < (SELECT max(salary)
              FROM Employee)
    
-- Method 2
SELECT DISTINCT
        salary as SecondHighestSalary
FROM Employee
ORDER BY salary DESC
LIMIT 1,1

-- Method 3
select a.salary as SecondHighestSalary
from
    (select salary, rank() over (order by salary desc) as rn
from employee) a
where a.rn = 2