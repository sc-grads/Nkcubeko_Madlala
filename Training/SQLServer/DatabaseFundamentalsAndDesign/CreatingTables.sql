USE [FirstDatabase]
GO

/****** Object:  Table [dbo].[personalDetails]    Script Date: 2023/02/28 10:01:11 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[personalDetails](
	[firstName] [varchar](50) NULL,
	[lastName] [varchar](50) NULL,
	[dob] [datetime] NULL,
	[ID] [int] NOT NULL
) ON [PRIMARY]
GO



CREATE TABLE [dbo].[personalDetails](
	[firstName] [varchar](50) NULL,
	[lastName] [varchar](50) NULL,
	[dob] [datetime] NULL,
	[ID] [int] NOT NULL,
 CONSTRAINT [PK_personalDetails] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

