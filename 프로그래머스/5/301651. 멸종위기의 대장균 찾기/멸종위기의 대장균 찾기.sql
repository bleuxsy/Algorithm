# -- 코드를 작성해주세요
with
recursive gen as (
    select id, parent_id, 1 as generation 
    from ecoli_data 
    where parent_id is null
    
    union all
    select e.id, e.parent_id, g.generation + 1
    from ecoli_data e
    join gen g
    on e.parent_id = g.id
)
select count(*) as COUNT, generation
from gen 
where id in (
    select distinct l.id
    from ecoli_data l
    left join ecoli_data r
    on r.parent_id = l.id
    where r.id is null


)
group by generation 
order by generation

 