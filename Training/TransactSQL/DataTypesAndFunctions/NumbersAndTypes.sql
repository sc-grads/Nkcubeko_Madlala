-- IMPLICIT

DECLARE @myvar as Decimal(5,2) = 3

SELECT @myvar

-- explicit

SELECT CONVERT(decimal(5,2),3)/2
SELECT CAST(3 as decimal(5,2))/2

SELECT CONVERT(decimal(5,2),1000) -- this does not work

SELECT 3/2 -- EQUALS 1
SELECT 3/2.0 -- EQUALS 1.5

SELECT CONVERT(INT,12.345)+CONVERT(INT,12.7) -- This equals 24.
SELECT CONVERT(INT,12.345+12.7) -- This equals 25.

