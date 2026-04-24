-- 코드를 입력하세요
with recursive hours as (
    select 0 as hour
    
    union all
    
    select hour+1 from hours
    where hour < 23
)
,
 cnt as (
select hour(datetime) as hour, count(*) as c
from animal_outs
group by hour(datetime)
)
select hours.hour, ifnull(cnt.c, 0)
from hours
left join cnt on hours.hour = cnt.hour
