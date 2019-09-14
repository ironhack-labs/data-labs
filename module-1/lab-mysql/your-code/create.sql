USE lab_mysql;
CREATE TABLE cars (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    VIN VARCHAR(25) NOT NULL,
    manufacturer VARCHAR(20),
    model VARCHAR(15),
    year VARCHAR(4),
    color VARCHAR(10)
    )
;

CREATE TABLE salespersons (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    staff_id VARCHAR(10) NOT NULL,
    sales_name VARCHAR(30),
    store VARCHAR(20)
    )
;

CREATE TABLE invoices (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    invoice_number INTEGER(15) NOT NULL,
    invoice_date VARCHAR(20),
    car VARCHAR(25) NOT NULL,
    customer_id VARCHAR(25) NOT NULL,
    staff_id VARCHAR(10) NOT NULL
)
;

CREATE TABLE customers (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    customer_id VARCHAR(25) NOT NULL,
    cust_name VARCHAR(30),
    cust_phone VARCHAR(30),
    cust_email VARCHAR(40),
    cust_address VARCHAR(50),
    cust_city VARCHAR(30),
    cust_state VARCHAR(20),
    cust_country VARCHAR(30),
    cust_postal VARCHAR(15)
)
;