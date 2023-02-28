USE [FirstDatabase]
GO

INSERT INTO [dbo].[personalDetails]
           ([firstName]
           ,[lastName]
           ,[dob]
           ,[ID])
     VALUES
           ('Nkcubeko'
		   , 'Madlala'
           ,'07/07/1916'
           ,19006)
GO

select * from [dbo].[personalDetails]
GO

