
-- 177. Nth Highest Salary

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT e1.Salary
      FROM (SELECT DISTINCT Salary FROM Employee) as e1
      WHERE (SELECT COUNT(*) FROM (SELECT DISTINCT Salary FROM Employee) as e2 
             WHERE e2.Salary > e1.Salary) = N - 1      
      
      LIMIT 1
  );
END


-- 178. Rank Scores

SELECT S.Score , COUNT(S2.Score) AS `Rank` 
FROM Scores AS S, (SELECT DISTINCT Score FROM Scores) AS S2 
WHERE S.Score <=S2.Score
GROUP BY S.Id
ORDER BY S.Score DESC ; 

-- 185. Department Top Three Salaries

SELECT D.Name AS Department , E.Name AS Employee , E.Salary as Salary 
FROM Employee AS E INNER JOIN Department AS D ON E.DepartmentId = D.Id
WHERE 3 > 
(SELECT COUNT(DISTINCT E2.Salary) FROM Employee as E2 WHERE E2.Salary > E.Salary AND E.DepartmentId= E2.DepartmentId)

