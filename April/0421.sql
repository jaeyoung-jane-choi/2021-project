
-- 181. Employees Earning More Than Their Managers

SELECT E1.Name as Employee
FROM Employee as E1 , Employee as E2
WHERE E1.ManagerId = E2.Id  and E1.Salary > E2.Salary


SELECT e1.Name
FROM Employee e1 Inner Join Employee e2 on e1.ManagerId=e2.Id
WHERE e1.Salary>e2.Salary


-- 182. Duplicate Emails

SELECT Email
FROM Person 
GROUP BY Email 
HAVING count(*)>1 ;  

-- 197. Rising Temperature

SELECT w1.id as id
FROM Weather as w1, Weather as w2
WHERE (DATEDIFF(w1.recordDate, w2.recordDate) = 1) AND w1.Temperature > w2.Temperature;