select N, 
    case 
        when P is NULL then 'Root' 
        when N in (select P from BST) then 'Inner'
        else 'Leaf' 
    end
from BST 
order by N;