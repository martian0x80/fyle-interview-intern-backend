-- Write query to find the number of grade A's given by the teacher who has graded the most assignments

SELECT COUNT(*) AS GRADE_A_COUNT FROM assignments AS ASS JOIN teachers as TEA ON ASS.teacher_id = TEA.id WHERE ASS.grade = 'A' GROUP BY TEA.id ORDER BY COUNT(*) DESC LIMIT 1;