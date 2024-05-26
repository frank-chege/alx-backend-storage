--create view to manage meetings
DROP VIEW IF EXISTS need_mmeting;
CREATE VIEW need_mmeting AS
SELECT name 
    FROM students
WHERE score < 80 
    AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);