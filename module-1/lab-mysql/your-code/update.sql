USE lab_mysql;

UPDATE salespersons SET store = 'Miami' WHERE staff_id = 00005;

UPDATE customers SET cust_email = ('ppicasso@gmail.com') WHERE customer_id = 10001;
UPDATE customers SET cust_email = ('lincoln@us.gov') WHERE customer_id = 20001;
UPDATE customers SET cust_email = ('hello@napoleon.me') WHERE customer_id = 30001;