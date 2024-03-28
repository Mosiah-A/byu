SELECT * FROM cust_order;
SELECT * FROM store;
SELECT * FROM customer;


-- Inquiry of Orders from Santa Cruz Bikes Store in January 2016

SELECT cust_order.cust_order_id, cust_order.order_date, cust_order.shipped_date, store.store_name, customer.first_name
FROM cust_order
	JOIN store
		ON cust_order.store_id = store.store_id
	JOIN customer
		ON cust_order.customer_id = customer.customer_id
WHERE store_name = "Santa Cruz Bikes" and shipped_date is not null and shipped_date like "2016-01%"
ORDER BY first_name;

