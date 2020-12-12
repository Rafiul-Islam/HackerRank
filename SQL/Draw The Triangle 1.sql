set @i = 21;
select repeat('* ', @i := @i - 1)
from information_schema.tables