Use AdventureWorks2019
GO

SELECT * FROM Person.Address

SELECT addressid,city,modifieddate FROM [Person].[Address]

SELECT city,addressid,modifieddate FROM [Person].[Address]

SELECT TOP 10 * FROM [Person].[Address]

--------------------------------------------------------------------------------------------------------------------------------------

SELECT * FROM Person.Address WHERE PostalCode = '98011'

SELECT * FROM Person.Address WHERE PostalCode != '98011'

SELECT * FROM Person.Address WHERE PostalCode <> '98011'

SELECT COUNT(*) FROM Person.Address WHERE PostalCode <> '98011'

SELECT * FROM Person.Address WHERE ModifiedDate >= '2013-11-08'

SELECT * FROM [Person].[Person] WHERE FirstName LIKE 'MAT%'

SELECT MAX(Rate) FROM [HumanResources].[EmployeePayHistory] 

SELECT MIN(Rate) FROM [HumanResources].[EmployeePayHistory] 

SELECT * FROM [Production].[ProductCostHistory] WHERE StartDate = '2013-05-30'

SELECT * FROM [Production].[ProductCostHistory] WHERE StartDate = '2013-05-30' AND StandardCost >= 200.00

SELECT * FROM [Production].[ProductCostHistory] WHERE (StartDate = '2013-05-30' AND StandardCost >= 200.00) OR ProductID > 800

SELECT * FROM [Production].[ProductCostHistory] WHERE (StartDate = '2013-05-30' AND StandardCost >= 200.00) AND ProductID > 800


SELECT * FROM [Production].[ProductCostHistory] WHERE ProductID in (802,803,820,900)

SELECT * FROM [Production].[ProductCostHistory] WHERE EndDate is NULL

SELECT * FROM [Production].[ProductCostHistory] WHERE EndDate is NOT NULL

--------------------------------------------------------------------------------------------------------------------------------------------

SELECT * FROM [HumanResources].[EmployeePayHistory] ORDER BY rate

SELECT * FROM [HumanResources].[EmployeePayHistory] ORDER BY rate ASC

SELECT * FROM [HumanResources].[EmployeePayHistory] ORDER BY rate DESC

SELECT * FROM [HumanResources].[EmployeePayHistory] WHERE ModifiedDate = '2010-06-30 00:00:00.000' ORDER BY ModifiedDate DESC

SELECT * FROM [HumanResources].[EmployeePayHistory] WHERE YEAR(ModifiedDate) >= '2014' ORDER BY ModifiedDate DESC

SELECT COUNT(*) FROM Person.Address WHERE PostalCode = '98011' --26

SELECT * FROM Person.Address WHERE PostalCode = '98011'

SELECT COUNT(*) FROM Person.Address WHERE PostalCode = '98225'  --213

SELECT COUNT(*),PostalCode FROM Person.Address GROUP BY PostalCode ORDER BY PostalCode DESC

SELECT COUNT(*),City FROM Person.Address GROUP BY City ORDER BY City DESC

------------------------------------------------------------------------------------------------------------------------------------------------

SELECT COUNT(1) As CountOfProduct,Color FROM [Production].[Product] WHERE Color = 'Yellow' GROUP BY Color

SELECT COUNT(1) As CountOfProduct,Color FROM [Production].[Product] GROUP BY Color HAVING Color = 'Yellow' 

SELECT COUNT(1) As CountOfProduct,Color,Size FROM [Production].[Product] GROUP BY Color,Size HAVING Size >= '44' 



