/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [EmpID]
      ,[EmpName]
      ,[EmpTitle]
  FROM [AdventureWorks2019].[dbo].[Employee]

INSERT INTO [dbo].[Employee]
           ([EmpID]
           ,[EmpName]
           ,[EmpTitle])
     VALUES
           (1325
		   , 'Madlala'
           ,'CEO')
GO

INSERT INTO [dbo].[Employee]
           ([EmpID]
           ,[EmpName]
           ,[EmpTitle])
     VALUES
           (2134
		   , 'Bona'
           ,'Assistant')
GO

INSERT INTO [dbo].[Employee]
           ([EmpID]
           ,[EmpName]
           ,[EmpTitle])
     VALUES
           (1907
		   , 'Danko'
           ,'Manager')
GO

SELECT * FROM Employee


CREATE TRIGGER EmployeeInsert
   ON  Employee
   AFTER INSERT
AS 
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for trigger here
	INSERT INTO EmployeeTriggerHostory VALUES((SELECT TOP(1) EmpID FROM Employee),'Insert')
END
GO

SELECT * FROM EmployeeTriggerHostory

INSERT INTO [Employee] VALUES

ALTER TABLE [Employee]
ADD ID int identity(1, 1)
GO

ALTER TABLE [Employee] DROP Column EmpID
GO



