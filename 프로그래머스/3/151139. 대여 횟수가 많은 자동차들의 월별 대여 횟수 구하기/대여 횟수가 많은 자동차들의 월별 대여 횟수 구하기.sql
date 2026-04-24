-- 코드를 입력하세요
SELECT month(start_date) as month, car_id, count(*) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where car_id in (
    SELECT car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    where month(start_date) between '8' and '10'
    group by car_id
    having count(*) >= 5
) and month(start_date) between '8' and '10'
group by month(start_date), car_id
order by month(start_date), car_id desc
