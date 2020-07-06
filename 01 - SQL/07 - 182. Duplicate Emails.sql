/*
182. Duplicate Emails

Solution to : https://leetcode.com/problems/duplicate-emails/

Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.
*/

# Write your MySQL query statement below

-- Method 1: Using Derived Tables
Select email 
From
    (
        Select email, count(email) as "Email_Count"
        From Person
        Group by email
    ) as Result
Where Result.Email_Count > 1


-- Method 2 : Using the Group By Having method

Select email
From person
group by email
having count(email) > 1
