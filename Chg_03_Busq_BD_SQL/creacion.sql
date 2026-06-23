CREATE TABLE customers(
    customer_id int primary key, 
    full_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    phone int NOT NULL, 
    city varchar(50) NOT NULL,
    segment varchar(63) NOT NULL,
    created_at timestamp NOT NULL,
    is_active tinyint(1) NOT NULL, 
    deleted_at timestamp
);

CREATE TABLE products (
    product_id int primary key,
    sku varchar(15) unique NOT NULL, 
    product_name varchar(25) NOT NULL,
    category varchar(25) NOT NULL,
    brand varchar(25) NOT NULL,
    unit_price decimal(10, 2) NOT NULL,
    unit_cost decimal(10, 2) NOT NULL,
    created_at int NOT NULL,
    is_active tinyint NOT NULL, 
    deleted_at timestamp
);
