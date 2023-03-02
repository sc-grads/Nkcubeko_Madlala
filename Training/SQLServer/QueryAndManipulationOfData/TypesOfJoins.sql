Use FirstDatabase
GO

SELECT * FROM dbo.Student
GO

SELECT * FROM dbo.Course
GO

SELECT s.rollno,s.studentname,c.courseid FROM Student s
 JOIN Course c
on s.rollno = c.rollno

SELECT s.rollno,s.studentname,c.courseid FROM Student s
INNER JOIN Course c
on s.rollno = c.rollno

SELECT s.rollno,s.studentname,c.courseid FROM Student s
LEFT JOIN Course c
on s.rollno = c.rollno

SELECT s.rollno,s.studentname,c.courseid FROM Student s
RIGHT JOIN Course c
on s.rollno = c.rollno

SELECT s.rollno,s.studentname,c.courseid FROM Student s
 FULL JOIN Course c
on s.rollno = c.rollno


