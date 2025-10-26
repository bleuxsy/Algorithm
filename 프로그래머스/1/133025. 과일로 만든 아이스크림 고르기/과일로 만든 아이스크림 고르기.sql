select f.flavor
from FIRST_HALF f
JOIN ICECREAM_INFO i 
ON f.flavor = i.flavor
where f.total_order > 3000 and i.ingredient_type = 'fruit_based'
order by f.total_order desc;