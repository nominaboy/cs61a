-- Creating TABLES

SELECT name FROM records WHERE supervisor = 'Oliver Warbucks';

SELECT * FROM records as a WHERE a.name = a.supervisor;

SELECT name FROM records WHERE salary > 50000 ORDER BY name ;

-- JOINS

SELECT m.day, m.time FROM records as r, meetings as m WHERE r.supervisor = 'Oliver Warbucks' AND r.division = m.division GROUP BY m.day, m.time;

SELECT a.name, b.name FROM records as a, records as b
WHERE b.division = a.division 
AND a.name < b.name;

SELECT a.name FROM records as a, records as b
WHERE a.supervisor = b.name
AND a.division <> b.division;

-- Aggregation

SELECT supervisor, SUM(salary) FROM records
GROUP BY supervisor;

SELECT m.day FROM records as r, meetings as m
WHERE r.division = m.division
GROUP BY m.day
HAVING COUNT(*) < 5;

SELECT a.division FROM records as a, records as b
WHERE a.name <> b.name
AND a.division = b.division
GROUP BY a.division
HAVING MAX(a.salary + b.salary) < 100000;

-- Tutorial

CREATE TABLE num_taught AS
    SELECT professor, course, COUNT(*) as times FROM courses
    GROUP BY professor, course;

SELECT a.professor, b.professor, a.times FROM num_taught as a, num_taught as b
WHERE a.course = b.course
AND a.times = b.times
AND a.professor < b.professor;

SELECT a.professor, b.professor FROM courses as a, courses as b
WHERE a.course = b.course
AND a.semester = b.semester
AND a.professor < b.professor
GROUP BY a.professor, b.professor
HAVING COUNT(*) > 1;
 
