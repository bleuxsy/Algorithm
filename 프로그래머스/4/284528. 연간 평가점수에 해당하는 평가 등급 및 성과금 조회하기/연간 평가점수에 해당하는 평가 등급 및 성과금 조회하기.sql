-- 코드를 작성해주세요
# select emp_no, emp_name, grade , bonus
select e.emp_no, e.emp_name, g.grade , 
    case 
        when g.grade = 'S' then e.sal * 0.2
        when g.grade = 'A' then e.sal * 0.15
        when g.grade = 'B' then e.sal * 0.1
        else 0
    end as bonus
        
from hr_employees e
join (
        select emp_no , 
            case 
                WHEN AVG(SCORE) >= 96 THEN 'S'
                WHEN AVG(SCORE) >= 90 THEN 'A'
                WHEN AVG(SCORE) >= 80 THEN 'B'
                else 'C'
            end as grade
        from hr_grade
        group by emp_no

) g on e.emp_no = g.emp_no
order by emp_no