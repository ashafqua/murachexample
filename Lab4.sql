-- Lab 4 Summary Queries and Subqueries

-- Q2
USE ap;
SELECT 
    vendor_name,
    CONCAT('$ ', FORMAT(SUM(invoice_total), 2)) AS invoice_total_sum
FROM
    vendors
        JOIN
    invoices USING (vendor_id)
GROUP BY vendor_id
ORDER BY vendor_name;

-- Q3
USE ap;
SELECT 
    vendor_name,
    COUNT(invoice_total) AS invoice_count,
    CONCAT('$ ', FORMAT(SUM(invoice_total), 2)) AS invoice_total_sum,
    CONCAT('$ ',FORMAT(SUM(invoice_total) / COUNT(invoice_total),
                2)) AS invoice_average
FROM
    vendors
        JOIN
    invoices USING (vendor_id)
GROUP BY vendor_id
ORDER BY invoice_count DESC;

-- Q4
USE ap;
SELECT 
    vendor_name,
    COUNT(DISTINCT account_description) number_of_accounts
FROM
    vendors
        JOIN
    invoices USING (vendor_id)
        JOIN
    invoice_line_items USING (invoice_id)
        JOIN
    general_ledger_accounts USING (account_number)
GROUP BY vendor_id
HAVING number_of_accounts > 1;

-- Q5
SELECT DISTINCT vendor_name

FROM vendors 

WHERE vendor_id IN 

   (SELECT vendor_id FROM invoices) 

ORDER BY vendor_name;

-- Q6
SELECT 
    invoice_number, invoice_total
FROM
    invoices
WHERE
    payment_total > (SELECT 
            AVG(payment_total)
        FROM
            invoices
        WHERE
            payment_total > 0)
ORDER BY invoice_total DESC;