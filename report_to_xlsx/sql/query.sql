select coi.column_1 optin, cec.column_2, cec.column_3, cb.column_4
from TB_1 coi
inner join TB_2 cec on coi.column_1 = cec.column_2
inner join TB_3 cb on cb.column_3 = cec.column_4
where coi.column_5 = 'XXXXXX'
and cb.column_1 > SYSDATE -90
ORDER BY cb.column_1 DESC