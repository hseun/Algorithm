SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE LOWER(NAME) LIKE '%el%' AND ANIMAL_TYPE = "Dog"
ORDER BY LOWER(NAME)