/*
183. Customers Who Never Order

Solution to : https://leetcode.com/problems/customers-who-never-order/

Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
*/

-- Write your MySQL query statement below
-- Method 1: Using LEFT JOIN

SELECT Name AS 'Customers'
FROM Customers c
LEFT JOIN Orders o
ON c.Id = o.CustomerId
WHERE o.CustomerId IS NULL

-- Method 2: Using subqueries

Select name as "Customers"
From Customers
Where Id not in
(
    Select CustomerId
    From Orders o

)
*/
    