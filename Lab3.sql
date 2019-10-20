-- Lab 3  INSERT / UPDATE / DELETE

-- Q3
USE om;
CREATE TABLE orders_copy AS
SELECT * 
FROM orders;
CREATE TABLE items_copy AS
SELECT * 
FROM items;

-- Q4
SET SQL_SAFE_UPDATES=0;
DELETE FROM orders_copy 
WHERE
    shipped_date IS NULL;

-- Q5
UPDATE items_copy 
SET 
    unit_price = 1.2 * unit_price
WHERE
    artist = 'Umami';
    
-- Q6
INSERT INTO items_copy
VALUES(17,'title of album','name of artist',12.17)