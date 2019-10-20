/* Assignment 3 - ANSWER KEY */
use my_guitar_shop;

/* QUESTION 1 */
SELECT product_name, COUNT(*) AS num_orders,
FORMAT(SUM(quantity), 0) AS num_products,
CONCAT('$', FORMAT(AVG(discount_amount), 2)) AS avg_discount
FROM products
JOIN order_items
	USING(product_id)
GROUP BY product_name WITH ROLLUP;

/* QUESTION 2 */
SELECT CONCAT('$', FORMAT(list_price, 2)) AS 'Product List Price', product_name AS 'Product', 
	description AS 'Description'
FROM products
WHERE list_price <=
	(SELECT AVG(list_price)
     FROM products
     JOIN categories
	 WHERE category_name = 'Guitars')
ORDER BY list_price, product_name;

/* QUESTION 3 */
SELECT CONCAT(last_name, ', ', first_name) AS 'Customer Name',
	COUNT(orders.order_id) AS num_orders,
	SUM(num_items) AS num_items, 
	CONCAT('$', FORMAT(ROUND(SUM(order_total), 2), 2)) AS order_total
FROM customers JOIN orders USING(customer_id)
	JOIN
		(SELECT order_id, 
			COUNT(item_id) AS num_items, 
			SUM((item_price - discount_amount) * quantity) AS order_total 
		FROM order_items GROUP BY order_id) t1
	USING(order_id)
WHERE ship_date IS NOT NULL    
GROUP BY CONCAT(last_name, ', ', first_name)
ORDER BY num_orders DESC, num_items DESC, SUM(order_total) DESC;


/* QUESTION 4 */
-- See the ~key_movies.pdf file