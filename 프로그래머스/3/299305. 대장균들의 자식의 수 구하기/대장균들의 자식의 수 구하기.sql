select e.id , ifnull(count(d.id), null) as child_count
from ecoli_data as e
left join ecoli_data as d
on e.id = d.parent_id
group by e.id
order by e.id