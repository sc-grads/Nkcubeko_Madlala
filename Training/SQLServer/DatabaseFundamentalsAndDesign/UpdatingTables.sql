USE [FirstDatabase]
GO

UPDATE [dbo].[personalDetails]
   SET [firstName] = 'Athi'
      ,[lastName] = 'Bude'
      ,[dob] = '02/01/1981'
      ,[ID] = 1122
 WHERE [firstName] = 'Lizwe'
GO

