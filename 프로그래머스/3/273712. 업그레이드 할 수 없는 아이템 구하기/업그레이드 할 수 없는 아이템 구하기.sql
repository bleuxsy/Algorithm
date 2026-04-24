-- 코드를 작성해주세요
select item_id, item_name, rarity
from item_info
where item_id in (
    select b.item_id
    from item_tree a
    right join item_tree b on a.parent_item_id = b.item_id
    where a.item_id is null
)
order by item_id desc