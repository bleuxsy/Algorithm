-- 코드를 작성해주세요
select d.dept_id, d.dept_name_en, round(avg(h.sal),0) as avg_sal
from hr_department d
join hr_employees h on d.dept_id = h.dept_id
group by d.dept_id, d.dept_name_en
order by avg_sal desc