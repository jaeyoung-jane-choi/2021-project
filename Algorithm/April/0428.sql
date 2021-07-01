-- 184. Department Highest Salary

SELECT  D.Name as Department  , E.Name as Employee , E.Salary as Salary
FROM Department as D INNER JOIN  Employee as E on D.Id = E.DepartmentId
WHERE E.Salary = (SELECT MAX(Salary) FROM Employee as E2 WHERE E2.DepartmentId = D.Id ); 

-- 180. Consecutive Numbers
SELECT DISTINCT Num as ConsecutiveNums
FROM Logs 
WHERE (Id+1,Num) in (SELECT  * FRoM Logs ) AND (Id+2 , Num) in (SELECT * FROM Logs) ; 


