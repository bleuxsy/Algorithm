# # -- 코드를 입력하세요
# # select *
# # from food_product
# SELECT category, max(price) as max_price , product_name
# from food_product
# group by category
# having category in ('과자','국', '김치', '식용유')
# order by max_price desc

# SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
# FROM FOOD_PRODUCT
# WHERE (CATEGORY, PRICE) IN (
#     SELECT CATEGORY, MAX(PRICE)
#     FROM FOOD_PRODUCT
#     WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
#     GROUP BY CATEGORY
# )
# ORDER BY MAX_PRICE DESC;

select category, price as max_price, product_name
from food_product
where (category, price) in (
    select category, max(price)
    from food_product
    where category in ('과자', '국', '김치', '식용유')
    group by category
)
order by max_price desc