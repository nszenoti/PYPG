shipper_t
---------
shipper_id               INTEGER         [PK]
shipper_name             VARCHAR(50)
shipper_contact_details  VARCHAR(30)

product_t
---------
product_id               INTEGER         [PK]
vehicle_maker            VARCHAR(60)
vehicle_model            VARCHAR(60)
vehicle_color            VARCHAR(60)
vehicle_model_year       INTEGER
vehicle_price            DECIMAL(14,2)

order_t
-------
order_id                 VARCHAR(25)
customer_id              VARCHAR(25)     [FK → customer_t.customer_id]
shipper_id               INTEGER         [FK → shipper_t.shipper_id]
product_id               INTEGER         [FK → product_t.product_id]
quantity                 INTEGER
vehicle_price            DECIMAL(10,2)
order_date               DATE
ship_date                DATE
discount                 DECIMAL(4,2)
ship_mode                VARCHAR(25)
shipping                 VARCHAR(30)
customer_feedback        VARCHAR(20)
quarter_number           INTEGER

customer_t
----------
customer_id              VARCHAR(25)     [PK]
customer_name            VARCHAR(25)
gender                   VARCHAR(15)
job_title                VARCHAR(50)
phone_number             VARCHAR(20)
email_address            VARCHAR(50)
city                     VARCHAR(25)
country                  VARCHAR(40)
state                    VARCHAR(40)
customer_address         VARCHAR(50)
postal_code              INTEGER
credit_card_type         VARCHAR(40)
credit_card_number       BIGINT

Relationships:
-------------
customer_t.customer_id  → order_t.customer_id      (1-to-many)
shipper_t.shipper_id    → order_t.shipper_id       (1-to-many)
product_t.product_id    → order_t.product_id       (1-to-many)
