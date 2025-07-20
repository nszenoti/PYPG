# Insights and Recommendations

## 1. total revenue

```sql
SELECT
    ROUND(SUM(quantity * vehicle_price * (1 - discount / 100.0)), 2) AS total_revenue
FROM order_t;
```
> 124714086.32

## 2. total orders

```sql
SELECT
	COUNT(*) AS total_orders
FROM order_t;
```
> 1000

## 3. total customers

```sql
SELECT
    COUNT(*) as total_customers,
    COUNT(DISTINCT o.customer_id) as customers_with_orders
FROM customer_t c
LEFT JOIN order_t o ON c.customer_id = o.customer_id;
```
> total: 1000
> having orders: 994

NOTE: This ensures only customers with actual orders are counted. (ie customers active for business)

When calculating business metrics (like Total Customers), we usually focus on customers who have placed at least one order, because:
- They contributed to revenue and activity.
- It reflects engaged users, not just sign-ups or entries in a database.
- Most downstream metrics (like retention, conversion, CLV) are based on purchasing behavior.

## 4. Average Ratings

```sql
SELECT
    ROUND(AVG(CASE
        WHEN customer_feedback = 'Very Good' THEN 5
        WHEN customer_feedback = 'Good' THEN 4
        WHEN customer_feedback = 'Okay' THEN 3
        WHEN customer_feedback = 'Bad' THEN 2
        WHEN customer_feedback = 'Very Bad' THEN 1
    END), 2) as avg_rating
FROM order_t
WHERE customer_feedback IS NOT NULL;
```
> 3.14

## 5. Last Quarter Revenue

```sql
SELECT
    ROUND(SUM(quantity * vehicle_price * (1 - discount/100)), 2) as last_quarter_revenue
FROM order_t
WHERE quarter_number = 4;
```
> 23346779.63

## 6. Last Quarter Orders

```sql
SELECT
    COUNT(*) as last_quarter_orders
FROM order_t
WHERE quarter_number = 4;
```
> 199

## 7. Average Days to Ship

```sql
SELECT
    ROUND(AVG(DATEDIFF(ship_date, order_date)), 0) AS avg_days_to_ship
FROM order_t
WHERE ship_date IS NOT NULL AND order_date IS NOT NULL;
```
> 98

## 8. % Good Feedback

```sql
SELECT
    ROUND(
        COUNT(CASE WHEN customer_feedback IN ('Good', 'Very Good') THEN 1 END) * 100.0 /
        COUNT(customer_feedback)
    , 2) as good_feedback_percentage
FROM order_t
WHERE customer_feedback IS NOT NULL;
```
> 44.10

---

**Summary**

```
| Metric                   | Value           |
|--------------------------|-----------------|
| Total Revenue            | 124,714,086.32  |
| Total Orders             | 1,000           |
| Total Active Customers   | 994             |
| Average Ratings          | 3.14            |
| Last Quarter Revenue     | 23,346,779.63   |
| Last Quarter Orders      | 199             |
| Average Days to Ship     | 98              |
| % Good Feedback          | 44.10%          |
```
