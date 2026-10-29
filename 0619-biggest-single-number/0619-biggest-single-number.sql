# Write your MySQL query statement below
SELECT max(num) as num from mynumbers 
where num in (select num from mynumbers 
group by num 
having count(*)=1)