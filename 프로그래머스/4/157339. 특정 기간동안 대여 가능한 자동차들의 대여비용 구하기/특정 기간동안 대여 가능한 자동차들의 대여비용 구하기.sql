# -- 코드를 입력하세요
with car as (
SELECT h.Car_id ,c.car_type, sum(datediff(h.end_date , h.start_date)) as duration
from CAR_RENTAL_COMPANY_RENTAL_HISTORY h
join CAR_RENTAL_COMPANY_CAR c 
on h.car_id = c.car_id
where c.car_type in ('SUV','세단')
AND NOT EXISTS (
      SELECT 1
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
      WHERE H.CAR_ID = C.CAR_ID
        AND H.START_DATE <= '2022-11-30'
        AND H.END_DATE >= '2022-11-01'
  )
group by h.car_id
)
, 
discount as (
    select c.car_id ,c.car_type , ifnull(p.discount_rate,0) as ratio
    from car c
    left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
    on c.car_type = p.car_type and 
    p.duration_type = '30일 이상'
   
  
)

select c.car_id, c.car_type, 
c.daily_fee * (100- d.ratio)/100 * 30 as fee
from discount d
join CAR_RENTAL_COMPANY_CAR c
on d.car_id = c.car_id
where c.daily_fee * (100- d.ratio)/100 * 30 between 500000 and 2000000
order by fee desc, car_type , car_id desc




