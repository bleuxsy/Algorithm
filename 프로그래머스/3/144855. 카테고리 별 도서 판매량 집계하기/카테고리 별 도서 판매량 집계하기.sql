-- 코드를 입력하세요
SELECT b.category , sum(s.sales) as total_sales
from book as b , book_sales as s
where b.book_id = s.book_id and date_format(s.sales_date , "%Y-%m") = '2022-01'
group by b.category
order by b.category