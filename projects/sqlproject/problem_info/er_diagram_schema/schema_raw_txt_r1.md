
`FK → Customer.customer_id`
Means this column is a foreign key referencing the customer_id column of the Customer table`

`PK -> Primary Key`

---

Entity: shipper_t
    shipper_id (INTEGER) [PK]
    shipper_name (VARCHAR(50))
    shipper_contact_details (VARCHAR(30))

Entity: product_t
    product_id (INTEGER) [PK]
    vehicle_maker (VARCHAR(60))
    vehicle_model (VARCHAR(60))
    vehicle_color (VARCHAR(60))
    vehicle_model_year (INTEGER)
    vehicle_price (DECIMAL(14,2))

Entity: order_t
    order_id: (VARCHAR(25))
    customer_id (varchar(25)) [FK -> customer_t.customer_id]
    shipper_id (INTEGER) [FK -> shipper_t.shipper_id]
    product_id (INTEGER) [FK -> product_t.product_id]
    quantity (INTEGER)
    vehicle_price (Decimal(10,2))
    order_date (DATE)
    ship_date (DATE)
    discount (DECIMAL(4,2))
    ship_mode (VARCHAR(25))
    shipping (VARCHAR(30))
    customer_feedback (VARCHAR(20))
    quarter_number (INTEGER)

Entity: customer_t
    customer_id (varchar(25)) [PK]
    customer_name (varchar(25))
    gender (varchar(15))
    job_title (varchar(50))
    phone_number (varchar(20))
    email_address (varchar(50))
    city (varchar(25))
    country (varchar(40))
    state (varchar(40))
    customer_address (varchar(50))
    postal_code (INTEGER)
    credit_card_type (varchar(40))
    credit_card_number (BIGINT)

Relationships:
- customer_t (1) to (many) order_t
  - customer_t.customer.id -> order_t.customer_id
- shipper_t (1) to (many) order_t
  - shipper_t.shipper.id -> order_t.shipper_id
- product_t (1) to (many) order_t
  - product_t.product_id -> order_t.product_id