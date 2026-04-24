-- 코드를 입력하세요
SELECT year(s.sales_date) , month(s.sales_date), i.gender , count(distinct i.user_id) as users
from online_sale s
join user_info i on s.user_id = i.user_id
where i.gender is not null
group by year(s.sales_date) , month(s.sales_date), i.gender
order by year(s.sales_date) , month(s.sales_date), i.gender 