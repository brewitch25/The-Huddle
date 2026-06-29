CREATE TABLE customers(
    customer_id int primary key, 
    full_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    phone varchar(25) NOT NULL, 
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
    customer_id int NOT NULL,
    order_datetime timestamp NOT NULL,
    channel varchar(63) NOT NULL,
    currency varchar(25) NOT NULL,
    current_status varchar(25) NOT NULL,
    order_total decimal (10, 2) NOT NULL,
    is_active tinyint(1) NOT NULL,
    deleted_at timestamp,
    constraint fk_customer foreign key (customer_id) references customers (customer_id)
);

CREATE TABLE order_items (
    order_item_id int primary key,
    order_id int not null, 
    product_id int null,
    quantity int NOT NULL,
    unit_price decimal (10, 2) NOT NULL,
    discount_rate decimal (10, 2) NOT NULL,
    line_total decimal(10,2) not null,
    constraint fk_orders_order_items foreign key (order_id) references orders (order_id),
    constraint fk_product foreign key (product_id) references products (product_id)
);

CREATE TABLE payments (
    payment_id INT primary key,
    order_id int not null,
    payment_datetime timestamp not null,
    method varchar(25) not null,
    payment_status varchar(25) not null,
    amount decimal(10, 2) CHECK (amount > 0) not null,
    currency varchar(25) not null,
    constraint fk_orders_payments foreign key (order_id) references orders (order_id)
);

CREATE TABLE order_status_history (
    status_history_id int primary key,
    order_id int not null,
    order_status varchar(25) not null, 
    changed_at timestamp not null,
    changed_by varchar(25) not null,
    reason varchar(25),
    constraint fk_orders_order_status_history foreign key (order_id) references orders (order_id)
);


CREATE TABLE order_audit (
    audit_id int primary key,
    order_id int not null,
    field_name varchar(25) not null,
    old_value varchar(25) not null,
    new_value varchar(25) not null,
    changed_at timestamp not null,
    changed_by varchar(25) not null,
    constraint fk_orders_order_audit foreign key (order_id) references orders (order_id)
);

-- Moficacion de tabla payments para agregar el CHECK (solo valores mayores a 0), en la 
-- columna amount
alter table payments 
add constraint chk_amount_positive check (amount >= 0);