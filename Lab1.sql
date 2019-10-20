-- Lab 1
-- Q2 = 7 
-- Q3 =9 
-- Q4 varchar(50)

-- Q5 
USE om;
SELECT 
    customer_last_name, customer_first_name
FROM
    customers
WHERE
    customer_state = 'DC';

-- Q6
USE ap;
SELECT 
    vendor_name, vendor_city
FROM
    vendors
WHERE
    vendor_state = 'CA'
ORDER BY vendor_city , vendor_name;

-- Q7
USE ap;
SELECT 
    invoice_number, payment_date, payment_total
FROM
    invoices
WHERE
    payment_date IS NULL;
    
-- Q8
USE om;
SELECT DISTINCT
    artist
FROM
    om.items
ORDER BY artist;

-- Q9
USE ex;
SELECT 
    CONCAT(customer_last_name,', ',customer_first_name) AS 'Full Name'
FROM
    ex.customers
ORDER BY customer_last_name , customer_first_name;

-- Q10
USE ap;
SELECT 
    invoice_number, payment_date, invoice_due_date, credit_total
FROM
    ap.invoices
WHERE
    payment_date > invoice_due_date
        AND credit_total > 0;



