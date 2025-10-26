-- 코드를 입력하세요
SELECT b.title, b.board_id, r.reply_id, r.writer_id, r.contents, date_format(r.created_date, '%Y-%m-%d') as CREATED_DATE
from used_goods_board as b, used_goods_reply as r
where b.board_id = r.board_id and date_format(b.created_date, '%Y-%m') = '2022-10'
order by r.created_date asc, b.title asc