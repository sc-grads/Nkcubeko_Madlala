declare @x xml
set @x = '<Shopping ShopperName="Phillip Burton" Weather="Nice">
<ShoppingTrip ShoppingTripID="L1">
    <Item Cost="5">Bananas</Item>
    <Item Cost="4">Apples</Item>
    <Item Cost="3">Cherries</Item>
</ShoppingTrip>
<ShoppingTrip ShoppingTripID="L2">
    <Item>Emeralds</Item>
    <Item>Diamonds</Item>
    <Item>Furniture</Item>
</ShoppingTrip>
</Shopping>'

select @x

update [dbo].[tblEmployee] 
set XMLOutput = @x
where EmployeeNumber = 200

select * from [dbo].[tblEmployee]
 FOR XML RAW
select E.EmployeeNumber, E.EmployeeFirstName, E.EmployeeLastName
	   , E.DateOfBirth, T.Amount, T.DateOfTransaction
from [dbo].[tblEmployee] as E
left join [dbo].[tblTransaction] as T
on E.EmployeeNumber = T.EmployeeNumber
where E.EmployeeNumber between 200 and 202
for xml raw('MyRow'), elements
FOR XML AUTO
select E.EmployeeNumber, E.EmployeeFirstName, E.EmployeeLastName
	   , E.DateOfBirth, T.Amount, T.DateOfTransaction
from [dbo].[tblEmployee] as E
left join [dbo].[tblTransaction] as T
on E.EmployeeNumber = T.EmployeeNumber
where E.EmployeeNumber between 200 and 202
for xml auto, elements
 FOR XML PATH
select E.EmployeeFirstName as '@EmployeeFirstName'
	   , E.EmployeeLastName as '@EmployeeLastName'
	   , E.EmployeeNumber
       , E.DateOfBirth
	   , T.Amount as 'Transaction/Amount'
	   , T.DateOfTransaction as 'Transaction/DateOfTransaction#'
from [dbo].[tblEmployee] as E
left join [dbo].[tblTransaction] as T
on E.EmployeeNumber = T.EmployeeNumber
where E.EmployeeNumber between 200 and 202
for xml path('Employees'), ROOT('MyXML')
 FOR XML EXPLICIT
select 1 as Tag, NULL as Parent
       , E.EmployeeFirstName as [Elements!1!EmployeeFirstName]
	   , E.EmployeeLastName as [Elements!1!EmployeeLastName]
	   , E.EmployeeNumber as [Elements!1!EmployeeNumber]
       , E.DateOfBirth as [Elements!1!DateOfBirth]
	   , null as [Elements!2!Amount]
	   , null as [Elements!2!DateOfTransaction]
from [dbo].[tblEmployee] as E
where E.EmployeeNumber between 200 and 202
union all
select 2 as Tag, 1 as Parent
       , null as [EmployeeFirstName]
	   , null as [EmployeeLastName]
	   , T.EmployeeNumber
	   , null as DateOfBirth
	   , Amount
	   , DateOfTransaction
from [dbo].[tblTransaction] as T
inner join [dbo].[tblEmployee] as E on T.EmployeeNumber = E.EmployeeNumber
where T.EmployeeNumber between 200 and 202
order by EmployeeNumber, [Elements!2!Amount]
for xml explicit
 XQuery Value method
declare @x xml  
set @x='<Shopping ShopperName="Phillip Burton" >  
<ShoppingTrip ShoppingTripID="L1" >  
  <Item Cost="5">Bananas</Item>  
  <Item Cost="4">Apples</Item>  
  <Item Cost="3">Cherries</Item>  
</ShoppingTrip>  
<ShoppingTrip ShoppingTripID="L2" >  
  <Item>Emeralds</Item>  
  <Item>Diamonds</Item>  
  <Item>Furniture</Item>  
</ShoppingTrip>  
</Shopping>'  
select @x.value('(/Shopping/ShoppingTrip/Item/@Cost)[1]','varchar(50)')
 XQuery Modify method
set @x.modify('replace value of (/Shopping/ShoppingTrip[1]/Item[3]/@Cost)[1]
                  with "6.0"')
select @x
set @x.modify('insert <Item Cost="5">New Food</Item>
			   into (/Shopping/ShoppingTrip)[2]')
select @x
 XQuery Query and FLWOR 1
select @x.query('for $ValueRetrieved in /Shopping/ShoppingTrip/Item
                 return $ValueRetrieved')
select @x.query('for $ValueRetrieved in /Shopping/ShoppingTrip/Item
                 return string($ValueRetrieved)')
select @x.query('for $ValueRetrieved in /Shopping/ShoppingTrip[1]/Item
                 return concat(string($ValueRetrieved),";")')
 XQuery Query and FLWOR 2
select @x.query('for $ValueRetrieved in /Shopping/ShoppingTrip[1]/Item
                 let $CostVariable := $ValueRetrieved/@Cost
                 where $CostVariable >= 4
                 order by $CostVariable
                 return concat(string($ValueRetrieved),";")')
