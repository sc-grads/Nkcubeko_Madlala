

CREATE TABLE FunctionEmployee(
	EmpID int PRIMARY KEY,
	FirstName varchar(50) NULL,
	LastName varchar(50) NULL,
	Salary int NULL,
	Address varchar(100) NULL,
)

INSERT INTO FunctionEmployee(EmpID,FirstName,LastName,Salary,Address) VALUES(1,'Akhona','Bham',3500,'Ivory')
INSERT INTO FunctionEmployee(EmpID,FirstName,LastName,Salary,Address) VALUES(2,'Lizwe','Jele',2700,'Rissik')
INSERT INTO FunctionEmployee(EmpID,FirstName,LastName,Salary,Address) VALUES(3,'Akhona','Duba',3100,'Bree')
INSERT INTO FunctionEmployee(EmpID,FirstName,LastName,Salary,Address) VALUES(4,'Andile','Gasa',5450,'Ivory')

SELECT * FROM FunctionEmployee

CREATE FUNCTION fnGetFullName
( @FirstName varchar(50), @LastName varchar(50))
returns varchar(101)
AS
BEGIN 
return (SELECT @FirstName + ' '+ @LastName);
END

SELECT dbo.fnGetFullName (FirstName,LastName) AS FullName , Salary FROM FunctionEmployee













