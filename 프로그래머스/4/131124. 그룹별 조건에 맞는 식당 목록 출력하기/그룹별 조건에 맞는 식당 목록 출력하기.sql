-- 코드를 입력하세요
with review as (
select member_id, count(*) as cnt
from rest_review
group by member_id
order by cnt desc
limit 1
)
select p.member_name, r.review_text, r.review_date
from rest_review r
join member_profile p on r.member_id = p.member_id
where r.member_id in (select member_id 
                      from review)
order by r.review_date, r.review_text