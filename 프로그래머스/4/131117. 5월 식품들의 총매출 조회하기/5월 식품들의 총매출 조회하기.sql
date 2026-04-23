# -- 코드를 입력하세요
# # SELECT p.product_id, p.product_name, sum(p.price *o.amount) as total_sales
select p.product_id, p.product_name, p.price * sum(o.amount) as total_sales
from food_product p
left join food_order o on p.product_id = o.product_id
where year(o.produce_date)='2022'and month(o.produce_date) = '5'
GROUP BY p.product_id, p.product_name, p.price
order by total_sales desc , p.product_id

# SELECT
#     p.product_id,
#     p.product_name,
#     SUM(p.price * o.amount) AS total_sales
# FROM food_product p
# JOIN food_order o
#     ON p.product_id = o.product_id
# WHERE o.produce_date BETWEEN '2022-05-01' AND '2022-05-31'
# GROUP BY p.product_id, p.product_name
# ORDER BY total_sales DESC, p.product_id;