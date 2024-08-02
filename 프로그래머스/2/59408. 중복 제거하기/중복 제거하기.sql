SELECT COUNT(c.name) as name
FROM (SELECT name
    FROM ANIMAL_INS
    GROUP BY name) as c