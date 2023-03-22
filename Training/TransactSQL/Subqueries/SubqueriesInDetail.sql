select T.* 
from tblTransaction as T
inner join tblEmployee as E
on E.EmployeeNumber = T.EmployeeNumber
where E.EmployeeLastName like 'y%'
order by T.EmployeeNumber

select * 
from tblTransaction as T
Where EmployeeNumber in
    (Select EmployeeNumber from tblEmployee where EmployeeLastName like 'y%')
order by EmployeeNumber
select * 
from tblTransaction as T
Where EmployeeNumber = some -- or "some"
    (Select EmployeeNumber from tblEmployee where EmployeeLastName like 'y%')
order by EmployeeNumber

select * 
from tblTransaction as T
Where EmployeeNumber <> any -- does not work properly
    (Select EmployeeNumber from tblEmployee where EmployeeLastName like 'y%')
order by EmployeeNumber

select * 
from tblTransaction as T
Where EmployeeNumber <> all 
    (Select EmployeeNumber from tblEmployee where EmployeeLastName like 'y%')
order by EmployeeNumber

select * 
from tblTransaction as T
Where EmployeeNumber <= all
    (Select EmployeeNumber from tblEmployee where EmployeeLastName like 'y%')
order by EmployeeNumber

-- anything up to 126 AND
-- anything up to 127 AND
-- anything up to 128 AND
-- anything up to 129

-- ANY = anything up to 129
-- ALL = anything up to 126

-- any/some = OR
-- all = AND

-- 126 <> all(126,127,128,129)
-- 126<>126 AND 126<>127 AND 126<>128 AND 126<>129
-- FALSE    AND TRUE = FALSE

-- 126 <> any(126,127,128,129)
-- 126<>126 OR 126<>127 OR 126<>128 OR 126<>129
-- FALSE    OR TRUE = TRUE
select * 
from tblTransaction as T
left join (select * from tblEmployee
where EmployeeLastName like 'y%') as E
on E.EmployeeNumber = T.EmployeeNumber
order by T.EmployeeNumber

select * 
from tblTransaction as T
left join tblEmployee as E
on E.EmployeeNumber = T.EmployeeNumber
Where E.EmployeeLastName like 'y%'
order by T.EmployeeNumber

select * 
from tblTransaction as T
left join tblEmployee as E
on E.EmployeeNumber = T.EmployeeNumber
and E.EmployeeLastName like 'y%'
order by T.EmployeeNumber
Select *, (select count(EmployeeNumber)
           from tblTransaction as T
		   where T.EmployeeNumber = E.EmployeeNumber) as NumTransactions,
		  (Select sum(Amount)
		   from tblTransaction as T
		   where T.EmployeeNumber = E.EmployeeNumber) as TotalAmount
from tblEmployee as E
Where E.EmployeeLastName like 'y%' --correlated subquery
