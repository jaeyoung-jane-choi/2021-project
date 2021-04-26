
-- 176. Second Highest Salary

SELECT MAX(Salary) as SecondHighestSalary
FROM Employee 
WHERE Salary < (SELECT max(Salary) FROM Employee) ; 


-- 183. Customers Who Never Order

SELECT C.Name as Customers 
FROM Customers as C
LEFT JOIN Orders as O on  C.Id = O.CustomerId
WHERE O.CustomerId is NULL ; 

-- 620. Not Boring Movies

SELECT * 
FROM cinema as c 
WHERE c.id % 2 != 0 AND Lower(c.description) NOT LIKE '%boring%'
ORDER BY rating  DESC ;

-- 596. Classes More Than 5 Students
SELECT class 
FROM courses 
GROUP BY class
HAVING COUNT(distinct(student)) >= 5 ;

-- 196. Delete Duplicate Emails

DELETE p2
FROM Person as p1, Person as p2 
WHERE p1.Email = p2.Email
AND p1.ID < p2.ID ;
