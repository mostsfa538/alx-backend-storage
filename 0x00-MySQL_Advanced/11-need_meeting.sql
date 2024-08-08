--  creates a view need_meeting
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80 AND (last_meeting IS NULL or last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH))
