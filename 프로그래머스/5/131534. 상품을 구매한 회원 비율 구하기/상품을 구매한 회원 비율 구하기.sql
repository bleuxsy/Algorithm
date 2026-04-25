-- 코드를 입력하세요
WITH cnt AS (
    SELECT COUNT(*) AS cntt
    FROM USER_INFO
    WHERE YEAR(JOINED) = 2021
)

select year(s.sales_date), month(s.sales_date), count(distinct s.user_id) as purchased_users, round(count(distinct s.user_id) / (select cntt from cnt) , 1) as purchased_ratio
from user_info i
join online_sale  s
on i.user_id = s.user_id
where year(i.joined) = '2021'
group by year(s.sales_date), month(s.sales_date)
order by  year(s.sales_date), month(s.sales_date)