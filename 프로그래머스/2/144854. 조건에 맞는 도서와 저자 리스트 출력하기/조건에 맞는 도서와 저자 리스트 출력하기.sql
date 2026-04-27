-- 코드를 입력하세요
SELECT b.book_id, a.author_name, b.PUBLISHED_DATE 
from book b
join author a on b.author_id = a.author_id
where b.category = '경제'
order by b.PUBLISHED_DATE