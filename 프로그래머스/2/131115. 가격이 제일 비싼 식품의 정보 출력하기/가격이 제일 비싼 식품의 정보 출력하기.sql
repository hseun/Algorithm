SELECT *
FROM FOOD_PRODUCT
WHERE PRICE IN (SELECT MAX(PRICE) AS PRICE FROM FOOD_PRODUCT)