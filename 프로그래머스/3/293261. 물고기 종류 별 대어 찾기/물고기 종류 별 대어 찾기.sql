-- 코드를 작성해주세요
with fish as (
    select i.fish_type, max(i.length) as length
    FROM FISH_INFO I
    JOIN FISH_NAME_INFO N
    ON I.FISH_TYPE = N.FISH_TYPE
    group by N.FISH_NAME
)

SELECT I.ID, N.FISH_NAME, I.LENGTH
FROM FISH_INFO I
JOIN FISH_NAME_INFO N
    ON I.FISH_TYPE = N.FISH_TYPE
WHERE (I.fish_type, I.length) IN (
    SELECT fish_type, length
    FROM fish
)
order by i.id 