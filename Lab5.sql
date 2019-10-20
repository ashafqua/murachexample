-- Lab 5 Subqueries, Data types, and Functions

-- Q2 approach 1 JOIN inside subquery
SELECT vendor_name, vendor_state
FROM vendors 
WHERE vendor_id IN 
     (SELECT vendor_id
     FROM ap.invoice_line_items JOIN ap.invoices 
     USING (invoice_id)
     WHERE line_item_amount > 3000)
ORDER BY vendor_name;

-- Q2 approach 2 JOIN outside subquery 
SELECT DISTINCT vendor_name, vendor_state
FROM vendors JOIN invoices USING (vendor_id)
WHERE invoice_id IN 
     (SELECT invoice_id
     FROM ap.invoice_line_items
     WHERE line_item_amount > 3000)
ORDER BY vendor_name;

-- Q3
USE ap;
SELECT vendor_name AS 'Vendor Name', 
    invoice_number AS 'Invoice Number',
    CAST(invoice_date AS DATETIME) AS 'Invoice Date/Time', 
    CONCAT('$', FORMAT(invoice_total, 2)) AS 'Invoice Amount'
FROM invoices i JOIN vendors v
    ON i.vendor_id = v.vendor_id
WHERE invoice_date =
    (SELECT MAX(invoice_date)
    FROM invoices 
    WHERE vendor_id = i.vendor_id)
ORDER BY vendor_name;

-- Q4
SELECT 
    UPPER(vendor_name) AS 'Vendor Name',
    REPLACE(REPLACE(REPLACE(vendor_phone, '(', ''),
            ') ',
            '.'),
        '-',
        '.') AS 'Vendor Phone',
    DATE_FORMAT(MAX(invoice_date), '%M %d,%Y') AS 'Latest Invoice'
FROM
    vendors
        JOIN
    invoices USING (vendor_id)
GROUP BY vendor_name
ORDER BY vendor_name;
