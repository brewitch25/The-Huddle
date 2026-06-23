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
    is_active tinyint(1) NOT NULL, 
    deleted_at timestamp
);

CREATE TABLE orders (
    order_id int primary key,
    foreign key (customer_id) NOT NULL,
    order_datetime timestamp NOT NULL,
    channel varchar(63) NOT NULL,
    currency varchar(25) NOT NULL,
    current_status varchar(25) NOT NULL,
    order_total decimal (10, 2) NOT NULL,
    is_active tinyint(1) NOT NULL,
    deleted_at timestamp
);

CREATE TABLE order_items (
    order_item_id int primary key,
    order_id int not null, 
    product_id int null,
    quantity int NOT NULL,
    unit_price decimal (10, 2) NOT NULL,
    discount_rate decimal (10, 2) NOT NULL,
    line_total decimal(10,2) not null,
    constraint fk_order foreign key (order_id) references orders(order_id),
    constraint fk_product foreign key (product_id) references products (product_id)
);


