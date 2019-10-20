/* Assignment #1 - INST327 - Answer Key - DO NOT DISTRIBUTE */

/*Answer 1*/
USE om;
SELECT CONCAT(customer_last_name, ', ', customer_first_name) AS 'Customer Name',
CONCAT('Contact #: ', right(customer_phone,3) , "-" , mid(customer_phone,4,3) , "-", right(customer_phone,4)) AS 'Customer Contact Number',
CONCAT(customer_address, ', ', customer_city, ', ', customer_state, ' ', customer_zip) AS 'Customer Address'
FROM customers
WHERE customer_last_name > "B" AND customer_last_name < "H"
ORDER BY customer_last_name, customer_state;


/*Answer 2*/
USE om;
SELECT order_id AS 'Order ID', CONCAT(customer_first_name, ' ', customer_last_name) AS 'Customer Name',
	order_date, shipped_date
	FROM orders JOIN customers USING(customer_id)
	WHERE shipped_date IS NOT NULL AND (order_id > 750 AND order_id < 900)
UNION
SELECT order_id AS 'Order ID', CONCAT(customer_first_name, ' ', customer_last_name) AS 'Customer Name', 
	order_date, 'Not Yet Shipped' AS shipped_date
	FROM orders JOIN customers USING(customer_id)
	WHERE shipped_date IS NULL AND (order_id > 750 AND order_id < 900)
ORDER BY order_date, shipped_date;


/*Answer 3*/
USE ap;
SELECT vendor_name AS 'Vendor Name', CONCAT(first_name, ' ', last_name) AS 'Contact Full Name', 
	invoice_id AS 'Invoice ID', (invoice_total - payment_total - credit_total) AS 'Balance Due'
    FROM vendor_contacts
        LEFT JOIN vendors USING (vendor_id)
        LEFT JOIN invoices USING (vendor_id)
ORDER BY vendor_name, (invoice_total - payment_total - credit_total);


/*Answer 4*/
USE ap;
SELECT terms_description, vendor_state, vendor_name, vendor_id
FROM vendors v
	JOIN terms t ON v.default_terms_id = t.terms_id
WHERE vendor_state > "N" AND vendor_state < "Q"
ORDER BY terms_description, vendor_state;

