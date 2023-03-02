--CREATE PROCEDURE SelectAllPersonAddress
--AS
--SELECT * FROM Person.Address 
--GO

--SELECT * FROM Person.Address

--exec SelectAllPersonAddress

--drop procedure SelectAllPersonAddress

CREATE PROCEDURE SelectAllPersonAddressWithParam (@city nvarchar(30) = 'New York')
AS
BEGIN
SET NOCOUNT ON
SELECT * FROM Person.Address WHERE City = @city
END

exec SelectAllPersonAddressWithParam @City = 'Miami'
exec SelectAllPersonAddressWithParam 'Miami'


