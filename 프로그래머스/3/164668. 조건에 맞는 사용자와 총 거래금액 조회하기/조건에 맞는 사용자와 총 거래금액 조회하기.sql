SELECT 
    u.user_id, 
    u.nickname, 
    SUM(b.price) AS total_sales
FROM used_goods_board b
JOIN used_goods_user u
    ON b.writer_id = u.user_id
#그룹 묶기 전에 행을 거름
where b.status = 'DONE'
GROUP BY u.user_id, u.nickname
# 그룹 묶은 후에 결과를 거름
HAVING total_sales >= 700000
ORDER BY total_sales;