-- 627. Swap Salary

UPDATE Salary 
SET sex = IF(sex='m','f','m') ;


-- 595. Big Countries

SELECT name, population, area 
FROM World
WHERE area > 3000000 OR population > 25000000;

-- #Union is faster! 
SELECT name, population, area
FROM World
WHERE area > 3000000 

UNION

SELECT name, population, area
FROM World
WHERE population > 25000000

-- 1179. Reformat Department Table

SELECT id, 
max(if (month = 'Jan', revenue, null)) AS Jan_Revenue,
max(if (month = 'Feb', revenue, null)) AS Feb_Revenue,
max(if (month = 'Mar', revenue, null)) AS Mar_Revenue,
max(if (month = 'Apr', revenue, null)) AS Apr_Revenue,
max(if (month = 'May', revenue, null)) AS May_Revenue,
max(if (month = 'Jun', revenue, null)) AS Jun_Revenue,
max(if (month = 'Jul', revenue, null)) AS Jul_Revenue,
max(if (month = 'Aug', revenue, null)) AS Aug_Revenue,
max(if (month = 'Sep', revenue, null)) AS Sep_Revenue,
max(if (month = 'Oct', revenue, null)) AS Oct_Revenue,
max(if (month = 'Nov', revenue, null)) AS Nov_Revenue,
max(if (month = 'Dec', revenue, null)) AS Dec_Revenue

FROM Department
GROUP BY id 
ORDER BY id ; 