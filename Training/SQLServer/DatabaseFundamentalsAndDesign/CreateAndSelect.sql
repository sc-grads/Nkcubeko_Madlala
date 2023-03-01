CREATE TABLE [AdventureWorks2019].[sales].[visits](
visit_id INT PRIMARY KEY IDENTITY(1,1),
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
visited_at DATETIME,
phone VARCHAR(20),
store_id INT NOT NULL,

)

CREATE TABLE [AdventureWorks2019].[sales].[storenew](
store_id INT NOT NULL,
sales INT
)

SELECT * FROM [AdventureWorks2019].[sales].[visits]