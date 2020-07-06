/*
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
*/

-- Method 1

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      -- Write your MySQL query statement below.
     
      SELECT salary 
      FROM
            (SELECT DISTINCT salary
             FROM Employee 
             ORDER BY salary DESC
             LIMIT N) AS Result
      ORDER BY salary
      LIMIT 1
  );
END

-- Method 2

WITH Result as 
(
	Select 	Salary,
			DENSE_RANK() over (ORDER BY salary DESC) as Drank
	From Employee
) 
Select Distinct Salary
From Result
Where Result.Drank = N