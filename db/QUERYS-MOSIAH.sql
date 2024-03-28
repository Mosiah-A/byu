-- Use V_art db
USE v_art;

-- Insert new artits
INSERT INTO artist (fname, mname, lname, dob, dod, country, local) VALUES
	("Johannes", null, "Vermeer", 1632, 1674, "Netherlands", "n");
    
-- List All artits alphabetically by Last Name
SELECT * 
FROM artist 
ORDER BY lname ASC;

-- Edit artist information
UPDATE artist
SET dod = 1674
WHERE artist_id = 10 AND fname = "Johannes";

-- delete artist
DELETE FROM artist
WHERE  artist_id = 10 AND fname = "Johannes" ;

-- Use bike db
USE bike;

-- Select first ,last name and phone
SELECT first_name, last_name, phone 
FROM customer
WHERE phone IS NOT NULL 
AND (city = 'Houston' OR city = 'Texas')
LIMIT 9;

-- Discount price to bike high $5.000,00
SELECT product_name, list_price, list_price - 500 AS discount_price
FROM product
WHERE list_price > 5000
ORDER BY list_price DESC;

-- List emails from Store 1
SELECT first_name, last_name, email
FROM staff
WHERE store_id = 1;

-- filter product
SELECT product_name, model_year, list_price
FROM product
WHERE product_name like "%spider%";

-- bikes in range 500 - 550
SELECT product_name, list_price
FROM product 
WHERE list_price BETWEEN 500 AND 550
ORDER BY list_price ASC;

-- Show especific customers
SELECT first_name, last_name, phone, street, city, state, zip_code
FROM customer
WHERE phone IS NOT NULL 
AND (city LIKE "%ach%" or city LIKE "%och%") 
OR last_name LIKE "william"
LIMIT 5;

-- Select product name
SELECT SUBSTRING_INDEX(product_name, ' - ', 1) AS product_name
FROM product
ORDER BY product_id
LIMIT 14;

-- SELECT 2019 Product and divide price into 3 parts
SELECT product_name, concat("$", ROUND((list_price / 3),2)) AS one_of_3_payments
FROM product
WHERE product_name LIKE "%2019";

-- use magazine
USE magazine;

-- magazine with 3% off
SELECT magazineName, ROUND(magazinePrice - magazinePrice * 0.03, 2) AS dicount_price
FROM magazine;

-- SELECT PRIMARY KEY 
SELECT subscriberKey, round(DATEDIFF('2020-12-20', subscriptionStartDate) / 365 ) AS Years_since_subscription
FROM subscription;

-- select sibscription lenght
SELECT subscriptionStartDate, subscriptionLength, DATE_FORMAT(DATE_ADD(subscriptionStartDate, INTERVAL subscriptionLength YEAR), '%M %e, %Y') AS subscription_end
FROM subscription;

