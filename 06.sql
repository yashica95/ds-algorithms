#Write an SQL query to find the employees who earn more than their managers.

SELECT emp1.name as Employee
FROM Employee emp1 JOIN Employee emp2 ON emp2.id = emp1.managerId
WHERE emp1.salary > emp2.salary
